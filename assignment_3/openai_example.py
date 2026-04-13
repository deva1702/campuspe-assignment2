#import required libraries
import os

from openai import OpenAI
from dotenv import load_dotenv

#load api key from .env file
load_dotenv(dotenv_path=".env")

#initialize openai client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#function to query openai model
def query_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

#main function to take user input and query openai
if __name__ == "__main__":
    prompt = input("Enter prompt: ")
    print(query_openai(prompt))
