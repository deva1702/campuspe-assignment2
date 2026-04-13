import streamlit as st
import time

# Import API functions
from groq_example import query_groq
from cohere_example import query_cohere
from huggingface_example import query_huggingface
from ollama_example import query_ollama

st.title("🤖 Multi AI Model Chat")

# Dropdown
model = st.selectbox(
    "Select Model",
    ["OpenAI (Unavailable)", "Groq", "Cohere", "Gemini (Unavailable)", "Ollama", "HuggingFace", "Compare APIs"]
)

# Input
prompt = st.text_area("Enter your prompt")

# Streaming function (KEY PART)
def stream_text(text):
    output = ""
    placeholder = st.empty()

    for word in text.split():
        output += word + " "
        placeholder.write(output)
        time.sleep(0.05)   # controls speed

# Button
if st.button("Submit"):
    if not prompt:
        st.warning("Please enter a prompt")
    else:
        if model == "OpenAI (Unavailable)":
            st.info("OpenAI unavailable (API limit reached)")

        elif model == "Groq":
            response = query_groq(prompt)
            stream_text(response)

        elif model == "Cohere":
            response = query_cohere(prompt)
            stream_text(response)

        elif model == "Gemini (Unavailable)":
            st.info("Gemini unavailable (quota limit)")

        elif model == "Ollama":
            response = query_ollama(prompt)
            stream_text(response)

        elif model == "HuggingFace":
            response = query_huggingface(prompt)
            stream_text(response)

        elif model == "Compare APIs":
            st.subheader("Comparison (Streaming)")

            st.write("**Groq:**")
            stream_text(query_groq(prompt))

            st.write("**Cohere:**")
            stream_text(query_cohere(prompt))

            st.write("**HuggingFace:**")
            stream_text(query_huggingface(prompt))