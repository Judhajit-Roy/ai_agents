import os
import sys
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv


load_dotenv()
# --- Setup and Configuration ---

api_key = os.getenv("GOOGLE_API_KEY")

# Check if the API key was successfully loaded.
if api_key is None:
    print("Error: GOOGLE_API_KEY environment variable is not set.")
    print("Please create a .env file with your API key, like this:")
    print("GOOGLE_API_KEY=",api_key)
    sys.exit(1)


# Initialize the LangChain chat model.
# The 'ChatGoogleGenerativeAI' class provides the LangChain interface for Gemini models.
# The model name is specified using the 'model' parameter.
model_name = "gemini-2.5-flash-lite"
llm = ChatGoogleGenerativeAI(model=model_name, google_api_key=api_key)

print(f"Chatbot initialized. Using LangChain with model: {model_name}\n")
print("Type your questions below. Type 'exit' to quit.\n")

# --- Chat Functionality ---
def chat_with_gemini(user_prompt):
    """
    Sends a prompt to the LangChain model and prints the response.obser
    """
    try:
        # LangChain's invoke method takes a message or a list of messages.
        # We wrap the user's input in a HumanMessage object.
        response = llm.invoke(user_prompt)

        # The response object from LangChain contains the content in the 'content' attribute.
        if response.content:
            print("Gemini:", response.content)
        else:
            print("Gemini: I'm sorry, I couldn't generate a response.")

    except Exception as e:
        print(f"An error occurred: {e}")

# --- Main Loop for User Interaction ---
def main():
    """
    Main loop to handle user input and chatbot interaction.
    """
    while True:
        user_input = input("You: ")
        
        # Check for the exit command.
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        chat_with_gemini(user_input)

if __name__ == "__main__":
    main()
