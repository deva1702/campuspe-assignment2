#import required libraries
import os
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

# Load .env properly
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#Function to query Groq model
def query_groq(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# def query_groq(prompt):
#     raise Exception("Test error")

# Main function to take user input and query Groq
if __name__ == "__main__":
    prompt = input("Enter prompt: ")
    print("Querying Groq...")
    print(query_groq(prompt))
