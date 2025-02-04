import os
from dotenv import load_dotenv
import openai

load_dotenv() 

openai.api_key = os.getenv("OPENAI_API_KEY")
print("Loaded key:", openai.api_key)

try:
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input="Hello, world!"
    )
    print("Success!", response)
except Exception as e:
    print("Error:", e)


