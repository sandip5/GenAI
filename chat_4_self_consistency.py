import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

#Self-Consistency Prompting - When we want to solve any arithmetic or reasoning based question then we run multiple iteration
# of Chain of Thoughts Technique and we aggregate results and try to see which results we are getting most of time. So, that is our
# Answer and we concluded Chain of Thoughts Self Consistency Prompting

system_prompt = """
You are an AI assistant where you need to give multiple answers for one question with context behind that answer.


"""