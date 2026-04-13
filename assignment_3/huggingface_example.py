#import required libraries
import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

#load api key from .env file
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

#initialize huggingface client
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

#create client instance
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=API_KEY
)

#function to query huggingface model
def query_huggingface(prompt):
    try:
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3-8B-Instruct",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"

#main function to take user input and query huggingface
if __name__ == "__main__":
    prompt = input("Enter prompt: ")
    print(query_huggingface(prompt))