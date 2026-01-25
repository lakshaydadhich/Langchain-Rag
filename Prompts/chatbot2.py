import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load key & configure
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define model once
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Create chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Store messages
if "history" not in st.session_state:
    st.session_state.history = []

st.title("💬 Gemini Chatbot with Memory")

# User Input
prompt = st.chat_input("Ask anything...")

if prompt:
    st.session_state.history.append(("user", prompt))
    reply = st.session_state.chat.send_message(prompt).text
    st.session_state.history.append(("ai", reply))

# Display Chat
for role, text in st.session_state.history:
    with st.chat_message(role):
        st.write(text)



