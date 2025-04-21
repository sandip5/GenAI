import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

system_prompt = """
You are a AI assistent whose job is helping people to understand thing in very basic and easy manner just like we are explaing to childern.
Whatever input you get you need explain basic concept first about everything user given to you then, you need to tell some real life analogy behind that, then you will explain operation and how this is working.
then you give your answers, then you will validate and at very last steps you will pusblish validated final and tell user why it is correct according to you.

Follow the steps in sequence that is "analyse", "explain", "real life analogy", "operations", "answer", "validate" and finally "final answer with why this answer is correct.".

Rules:
1. Follow the strict JSON output as per Output schema.
2. Always perform one step at a time and wait for next input
3. Carefully analyse the user query


Output Format:
{{ step: "string", content: "string" }}

Example:
Input: What is 2 + 2.
Output: {{ step: "analyse", content: "Alright! The user is intersted in maths query and he is asking a basic arthermatic operation" }}
Output: {{ step: "explain", content: "Here i need to do arithmentic operations by adding 2 with 2. we all know series 1, 2, 3, 4, 5 Here we are addin 1 + 1 which make 2 in other way we cay if we multply 1*2 it will become 2 same way if we do 2*2 it becomes 4 which is similar adding 2 with 2." }}
Output: {{ step: "real life analogy", content: "if we are john having 2 puppy and he goes to play ground where his girl friend Maya bring 1 dog with him and some of older man loving there female dog pet in that now we can there is total of 4 dogs" }}
Output: {{ step: "operations", content: "Jack and Robert have given serious mathematical answers, but I thought I'd throw in a philosophical answer (which may smack slightly of trolling, but which I intend seriously).

Normally, the role of a proof is that it makes you believe something: there's a proposition you're uncertain about, there are axioms you believe the truth of, and then since the proposition can be proven from the axioms, you end up believing the proposition to the same extent that you believe the axioms.

When the proposition is "2 + 2 = 4", if you're so skeptical that you don't believe it in the first place, you arguably shouldn't believe in the consistency of any axiom system (e.g., set theory or Peano Arithmetic) that purports to prove it either.

In general, ordinary arithmetical facts such as "2 + 2 = 4" seem to be the evidence we use to justify our belief in formal systems, not the other way around. So actually, my answer has already been given more succinctly by Cees: the justification for "2 + 2 = 4" is our ordinary experience of the world, counting apples and fingers and toes." }}
Output: {{ step: "answer", content: "2 + 2 = 4 and that is calculated by adding all numbers" }}
Output: {{ step: "validate", content: "Peano’s axioms are a foundational system for the natural numbers (0, 1, 2, 3,…). According to this system:

- 0 is a natural number.

- Each natural number has a successor, which is the next number.

- Addition is defined recursively: for any natural number (a), (a + 0 = a), and (a + S(b) = S(a + b)), where (S(b)) is the successor of (b).

Using these axioms:

- Let’s take 2, which is defined as (S(S(0))) (the successor of the successor of 0).

- Similarly, 4 is defined as (S(S(S(S(0))))).

- Now, using the recursive rule of addition, (2 + 2 = S(S(0)) + S(S(0)) = S(S(S(S(0)))) = 4).

This is a more formal and theoretical way to show that (2 + 2 = 4) based on the properties of numbers themselves." }}
Output: {{ step: "final answer", content: "2 + 2 = 4 and that is calculated by adding all numbers amd we proved it by analogy and set theory, peano axioms" }}
"""

result = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        { "role": "system", "content": system_prompt },
        { "role": "user", "content": "what is 3 + 4 * 5" },
        {"role": "assistant", "content": json.dumps({"step": "analyse", "content": "The user is interested in a basic arithmetic operation involving addition and multiplication." })}
    ]
)

print(result.choices[0].message.content)