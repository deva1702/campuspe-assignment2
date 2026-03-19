#import required library
import requests

#function to query ollama model
def query_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()
        return data["response"]   # only answer

    except Exception as e:
        return f"Error: {e}"

#main function to take user input and query ollama
if __name__ == "__main__":
    prompt = input("Enter prompt: ")
    print("Querying Ollama...\n")
    print(query_ollama(prompt))
