
import os
import streamlit as st
from groq import Groq

# Get API key from Streamlit Secrets
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

st.title("⚡ Groq Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful and friendly assistant."
        }
    ]

# User input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    st.chat_message("user").write(user_input)

    # Add to history
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Get response from Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages,
        max_tokens=1024
    )

    bot_reply = response.choices[0].message.content

    # Store assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    # Display assistant response
    st.chat_message("assistant").write(bot_reply)
