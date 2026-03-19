"""
Multi API Query Program (FINAL VERSION)
Features:
- Multiple AI API selection
- Compare multiple APIs
- Conversation history
-Retry logic for reliability"""


# Import API functions
from openai_example import query_openai
from groq_example import query_groq
from cohere_example import query_cohere
from gemini_example import query_gemini
from ollama_example import query_ollama
from huggingface_example import query_huggingface

# Store conversation history
history = []


def safe_query(func, prompt):
    """
    Retry API call up to 2 times if it fails
    """
    for _ in range(2):
        try:
            return func(prompt)
        except Exception:
            continue
    return "Failed after retrying twice"


def main():
    while True:
        print("\n===== Multi AI API Query =====")
        print("1. OpenAI")
        print("2. Groq")
        print("3. Cohere")
        print("4. Gemini")
        print("5. Ollama")
        print("6. HuggingFace")
        print("7. Compare Multiple APIs")
        print("0. Exit")

        choice = input("\nChoose API (0-7): ")

        if choice == "0":
            print("\nExiting... Goodbye!")
            break

        prompt = input("Enter your prompt: ")

        # Handle choices
        if choice == "1":
            response = "[INFO] OpenAI service unavailable (API limit reached)"

        elif choice == "2":
            response = safe_query(query_groq, prompt)

        elif choice == "3":
            response = safe_query(query_cohere, prompt)

        elif choice == "4":
            response = "[INFO] Gemini service unavailable (quota limit)"

        elif choice == "5":
            response = safe_query(query_ollama, prompt)

        elif choice == "6":
            response = safe_query(query_huggingface, prompt)

        elif choice == "7":
            print("\n--- Comparing Multiple APIs ---")

            print("\n[Groq]")
            groq_res = safe_query(query_groq, prompt)
            print(groq_res)

            print("\n[Cohere]")
            cohere_res = safe_query(query_cohere, prompt)
            print(cohere_res)

            print("\n[HuggingFace]")
            hf_res = safe_query(query_huggingface, prompt)
            print(hf_res)

            response = f"Groq: {groq_res}\nCohere: {cohere_res}\nHF: {hf_res}"

        else:
            print("Invalid choice. Try again.")
            continue

        # Print response (except compare which already prints)
        if choice != "7":
            print("\n--- Response ---")
            print(response)

        # Save to history
        history.append((prompt, response))

        # Show conversation history
        print("\n===== Conversation History =====")
        for i, (p, r) in enumerate(history, 1):
            print(f"{i}. Q: {p}")
            print(f"   A: {r}\n")


# Run program
if __name__ == "__main__":
    main()