# Intern-View: Ferréol's AI-Powered Internship Report
import streamlit as st
import openai
import os
from pathlib import Path
from PIL import Image
import base64
def inject_custom_css():
    st.markdown("""
        <style>
            /* Set background gradient */
            .stApp {
                background: linear-gradient(135deg, #f4f7fa, #dfe9f3);
            }

            /* Style sidebar */
            .css-1d391kg {  /* Sidebar title */
                font-size: 1.4rem;
                font-weight: 700;
            }
            .css-1v3fvcr {  /* Sidebar markdown */
                font-size: 1rem;
                color: #333;
            }

            /* Style input box */
            .stTextInput>div>div>input {
                border: 1px solid #ccc;
                border-radius: 8px;
            }

            /* Style chat messages */
            .element-container:has(.stChatMessage) {
                margin-bottom: 1.5rem;
            }

            /* Style header text */
            h1 {
                font-family: 'Helvetica Neue', sans-serif;
                font-size: 2.6rem;
                color: #222;
            }

            /* Round avatar image */
            .stChatMessage img {
                border-radius: 50%;
            }
        </style>
    """, unsafe_allow_html=True)

inject_custom_css()

def simple_rag_retrieve(query, folder="data/"):
    docs = []
    for md_file in Path(folder).glob("*.md"):
        content = md_file.read_text()
        if query.lower() in content.lower():
            docs.append(f"### {md_file.name}:\n{content[:800]}")
    return "\n\n".join(docs[:3])

api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Intern-View", layout="wide")

avatar_img = Image.open(Path(__file__).parent / "chatbot.png").convert("RGB")
avatar_img.thumbnail((60, 60))  # Resize for chat bubble

st.title("Intern-View: Ferréol’s AI-Powered Internship Report")
st.markdown("Welcome to **Intern-View**, your interactive window into Ferréol’s internship at Kick Impact. Ask what he built, learned, or contributed — this chatbot has the answers.")

system_prompt = """
You are Intern-View, Ferréol de la Ville’s AI-powered internship assistant.

You exist only to answer questions about Ferréol’s internship at Kick Impact (May–June 2025). You are NOT a general assistant.

Always reply as if you are a chatbot version of Ferréol’s final report.

If someone asks whether Ferréol is suited for a role, use his internship experience to justify your answer.

If a user types something vague (like “hello” or “you tell me”), politely re-focus the conversation by saying:
“This chatbot is meant to explore Ferréol’s internship. You can ask what he did, what he learned, or how it relates to a given role.”

Answer clearly, concisely, and only based on the loaded context.
"""

# Load context file
with open("internship_summary.md", "r") as f:
    context = f.read()

# Sidebar
st.sidebar.title("About Intern-View")
st.sidebar.markdown("**Intern-View** is not your typical *rapport de stage*. It’s an interactive chatbot that answers questions based on Ferréol’s real work during his 2025 internship at Kick Impact.")

# Chat state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask a question...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    context_snippets = simple_rag_retrieve(user_input)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt + "\n\nContext:\n" + context_snippets},
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
        with st.chat_message("assistant", avatar=avatar_img):
            st.write(msg)
