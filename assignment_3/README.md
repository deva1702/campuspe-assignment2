<div align="center">

#  AI API Integration Assignment

</div>

##  Assignment Overview

This project implements integration with multiple Generative AI APIs using Python. Each API is accessed through a separate Python program, and a unified interface is provided for interacting with multiple APIs.

---

## 🔹 OpenAI API

- Implemented using OpenAI Python SDK
- Accepts user input and generates responses
- ❗ **Status:** Not working due to lack of free API credits
- Fallback message implemented to handle this case

---

## 🔹 Groq API

- Implemented using Groq client
- Uses LLaMA model for responses
- ✅ **Status:** Working correctly
- Supports prompt-based query and response

---

## 🔹 Ollama API

- Implemented using `requests` library
- Uses locally running model (`phi3`)
- ✅ **Status:** Working correctly
- Requires Ollama to be running locally

---

## 🔹 Hugging Face API

- Implemented using OpenAI-compatible client with HuggingFace router
- Uses LLaMA model
- ✅ **Status:** Working (with occasional delays due to model load)

---

## 🔹 Google Gemini API

- Implemented using `google-generativeai` library
- ❗ **Status:** Not working due to quota limitations
- Fallback message implemented

---

## 🔹 Cohere API

- Implemented using Cohere SDK
- Uses chat-based model
- ✅ **Status:** Working correctly

---

#  Extra Features

## 🔹 Multi API Query Program

- Allows user to select any API from a menu
- Provides response from selected API
- Handles unavailable APIs with fallback messages

---

## 🔹 Compare Multiple APIs

- Allows comparison of responses from:
  - Groq
  - Cohere
  - HuggingFace
- Helps analyze differences in outputs

---

## 🔹 Conversation History

- Stores user prompts and responses
- Displays full interaction history
- Works across multiple queries

---

## 🔹 Retry Logic

- Automatically retries API calls on failure
- Prevents program crashes
- Improves reliability

---

## 🔹 Streamlit GUI

- User-friendly web interface
- Dropdown for API selection
- Input box for prompt
- Displays responses dynamically

---

## 🔹 Simulated Streaming Responses

- Responses displayed word-by-word
- Mimics real-time AI output
- Improves user experience

---

# ⚙️ Setup Instructions

## 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

## 🔹 Set Environment Variables

Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key
HUGGINGFACE_API_KEY=your_key
GOOGLE_API_KEY=your_key
COHERE_API_KEY=your_key
```

## 🔹 Ollama Setup (Local Model)

- Download and install from: [https://ollama.ai](https://ollama.ai)
- Pull and run the model:
```bash
ollama run phi3
```

---

# ▶️ How to Run

## CLI Program
```bash
python multi_api_query.py
```

## Streamlit GUI
```bash
streamlit run streamlit_app.py
```

---

#  Project Structure
```
assignment_3/
│
├── openai_example.py
├── groq_example.py
├── ollama_example.py
├── huggingface_example.py
├── gemini_example.py
├── cohere_example.py
├── multi_api_query.py
├── streamlit_app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

#  Screenshots

Screenshots showing outputs from each API and the GUI are available in the [`screenshots/`](./screenshots/) folder.

---

# Conclusion

This project successfully demonstrates integration of multiple AI APIs, handling of API limitations, and implementation of additional features such as response comparison, history tracking, retry logic, simulated streaming, and a Streamlit GUI interface.
