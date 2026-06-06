
import os
from groq import Groq
from dotenv import load_dotenv

# Step 1: Load the API key from the .env file
load_dotenv()


# Step 2: Connect to Groq
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Step 3: Set up conversation history
# The system message defines your bot's personality
conversation_history = [
    {
        "role": "system",
        "content": "You are a helpful and friendly assistant."
    }
]

print("⚡ Groq Chatbot is ready! (Type 'quit' to exit)\n")

# Step 4: Chat loop
while True:
    # Get user input
    user_input = input("You: ").strip()

    # Exit condition
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Chatbot: Goodbye! 👋")
        break

    # Skip empty input
    if not user_input:
        continue

    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    # Send to Groq and get a reply
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",   # Fast, capable model on Groq
        messages=conversation_history,      # Full history = bot remembers context
        max_tokens=1024
    )

    # Extract the reply
    bot_reply = response.choices[0].message.content

    # Save bot's reply to history so it remembers what it said
    conversation_history.append({
        "role": "assistant",
        "content": bot_reply
    })

    # Show the reply
    print(f"\nChatbot: {bot_reply}\n")