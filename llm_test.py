from langchain_ollama import ChatOllama 
from dotenv import load_dotenv
import os

# Optional: load env if using any variables
load_dotenv()

# Initialize Ollama chat model (adjust model name as needed)
chat_model = ChatOllama(model="llama2")

# Simple call using a string
response = chat_model.invoke("How to write code in Python?")

# Print the result
print(response.content)
