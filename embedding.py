from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI()

text = "Tahawwur Rana extradition LIVE | 17 years later, Mumbai terror attacks co-conspirator to land in Delhi"

response = client.embeddings.create(
    input=text,
    model="text-embedding-3-small"
)

print("Vector Embeddings", response.data[0].embedding)