#import required libraries
import os
import cohere
from dotenv import load_dotenv
from pathlib import Path

#load api key from .env file
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

#initialize cohere client
co = cohere.Client(os.getenv("COHERE_API_KEY"))

#function to query cohere model
def query_cohere(prompt):
    try:
        response = co.chat(
            model="command-a-03-2025",
            message=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

#main function to take user input and query cohere
if __name__ == "__main__":
    prompt = input("Enter prompt: ")
    print("Querying Cohere...")
    print(query_cohere(prompt))
