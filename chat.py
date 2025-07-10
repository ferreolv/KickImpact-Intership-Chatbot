# app.py
import streamlit as st
import openai
import os

api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Ferréol's Internship Bot", layout="wide")

st.title("🤖 Ferréol's Internship Chatbot")
st.markdown("Ask anything about Ferréol’s internship at Kick Impact. This bot replies based on real internship documents.")

# Load system prompt
with open("system_prompt.txt", "r") as f:
    system_prompt = f.read()

# Load context file
with open("data/internship_summary.md", "r") as f:
    context = f.read()

# Sidebar
st.sidebar.title("About")
st.sidebar.markdown("This chatbot replaces a traditional internship report. Ask about what I learned, built, or contributed to Kick Impact.")

# Chat state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask a question...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt + "\n\nContext:\n" + context},
            *[{"role": role, "content": msg} for role, msg in st.session_state.chat_history],
        ],
    )

    reply = response['choices'][0]['message']['content']
    st.session_state.chat_history.append(("assistant", reply))

# Display chat
for role, msg in st.session_state.chat_history:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)