import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Get API key from environment
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Error: GEMINI_API_KEY not found in .env file.")
    exit(1)

# Configure the Gemini API
genai.configure(api_key=API_KEY)

def main():
    print("=== Gemini Context-Aware Chatbot ===")
    print("Type 'exit' or 'quit' to end the chat.\n")

    # Ask user for temperature value
    try:
        temp_input = input("Set temperature (0.0 to 1.0, default = 0.7): ")
        temperature = float(temp_input) if temp_input.strip() else 0.7
    except ValueError:
        print("Invalid input. Using default temperature (0.7).")
        temperature = 0.7

    # Create model with temperature setting
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={"temperature": temperature}
    )

    chat = model.start_chat()
    turn = 1

    while True:
        user_message = input(f"\nYou ({turn}): ").strip()
        if user_message.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        response = chat.send_message(user_message)
        print(f"Gemini: {response.text}")
        turn += 1

if __name__ == "__main__":
    main()
