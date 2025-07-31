from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

import os

load_dotenv()

key = os.getenv("openai_api_key")

chat_model = ChatOpenAI(openai_api_key=key)

result = chat_model.predict("What is the capital of France?")

print(result)