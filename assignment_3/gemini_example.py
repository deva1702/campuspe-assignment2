#import required libraries
import os
from google import genai
from dotenv import load_dotenv
from pathlib import Path

#load api key from .env file
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

#initialize gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#function to query gemini model
def query_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    print("\nResult:", response.text)

#main function to take user input and query gemini
if __name__ == "__main__":
    prompt = input("Enter prompt: ")
    query_gemini(prompt)
