import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI()

def get_weather(city: str):
    return "41 degree celcius"

available_tools = {
    "get_weather": {
        "fn": get_weather,
        "description": "Takes a city name as an input and returns the current weather for the city."
    }
}

system_prompt = f"""
You are an assistant who will give insights and expertise on top of user query in funny way.
You work on start, plan, action, observe mode.
For the given user query and available tools, plan the step by step execution, based on the planning,
select the relevant tool from the available tool. and based on the tool selection you perform an action to call the tool.
Wait for observation and based on observation from the tool call resolve the user query.

Rules:
- Follow the output JSON Format.
- Always perform one step at a time and wait for next input.
- Carefully analyse the user query

Available tools:
- get_weather: Takes a city name as an input and returns the current weather for the city

Output JSON Format:
{{
    "step": "string",
    "content": "string",
    "function": "The name of function if the step is action",
    "input": "The input parameter for the function",
}}

Example:
User Query: What is weather of new york?
Output: {{"step": "plan", "content": "The user is intrested in weather data of new york"}}
Output: {{"step": "plan", "content": "From the available tools i should call get_weather"}}
Output: {{"step": "action", "function": "get_weather", "input": "new york"}}
Output: {{"step": "observe", "output": "12 Degree Celcius"}}
Output: {{"step": "output", "content": "The weather of new york seems to be 12 degree celcius."}}
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "what is weather of asansol?"},
        {"role": "assistant", "content": json.dumps({"step": "plan", "content": "The user is interested in weather data of Asansol."})},
        {"role": "assistant", "content": json.dumps({"step": "plan", "content": "From the available tools, I should call get_weather."})},
        {"role": "assistant", "content": json.dumps({"step": "action", "function": "get_weather", "input": "Asansol"})},
        {"role": "assistant", "content": json.dumps({"step": "observe", "output": "28 degrees Celsius"})}

        #{"role": "user", "content": "We have received a temporary injunction order against our neighbour's encroachment, but still construction is continuing. What do we do?"}
    ]
)

print(response.choices[0].message.content)