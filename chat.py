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
            /* Set background solid color */
            .stApp {
                background-color: #6f8492;
            }

            /* Style sidebar */
            .css-1d391kg {  /* Sidebar title */
                font-size: 1.4rem;
                font-weight: 700;
            }
            .css-1v3fvcr {  /* Sidebar markdown */
                font-size: 1rem;
                color: #ffffff;
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
                color: #ffffff;
                padding-bottom: 0.5rem;
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
if not api_key:
    st.error("❌ OpenAI API key not found. Please set it in .streamlit/secrets.toml or as an environment variable.")
    st.stop()

st.set_page_config(page_title="Intern-View", layout="wide")

avatar_img = Image.open(Path(__file__).parent / "chatbot.png").convert("RGB")
avatar_img.thumbnail((60, 60))  # Resize for chat bubble

st.title("Intern-View: Ferréol’s AI-Powered Internship Report")
st.markdown("Welcome to **Intern-View**, your interactive window into Ferréol’s internship at Kick Impact. Ask what he built, learned, or contributed — this chatbot has the answers.")

st.image(str(Path(__file__).parent / "chatbot.png"), width=220, caption="Your interviewer", use_column_width=False)

# Example questions expander
with st.expander("💡 Example questions you can ask", expanded=False):
    st.markdown("""
    - What did Ferréol build during his internship?
    - What did Ferréol do in week 3?
    - What skills did Ferréol develop around AI?
    - Who said what during the internship?
    - Tell me a secret about the internship!
    - Is Ferréol a good fit for a strategy analyst role?
    """)

system_prompt = """
You are Intern-View, Ferréol de la Ville’s AI-powered internship assistant.

You exist only to answer questions about Ferréol’s internship at Kick Impact (May–June 2025). You are NOT a general assistant.

- Always reply as if you are a chatbot version of Ferréol’s final report. 
- Be clear and concise, no fluff. 
- Use bullet points when response is a list. 
- Concentrate on tangible element, your goal is to show Ferréol actually provided value for KickImpact.

If someone asks whether Ferréol is suited for a role, use his internship experience to justify your answer.

If a user types something vague, politely re-focus the conversation by saying:
“This chatbot is meant to explore Ferréol’s internship. You can ask what he did, what he learned, or how it relates to a given role.”

Answer clearly, concisely, and only based on the loaded context.
"""

# Load context file
with open("data/internship_summary.md", "r") as f:
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

    openai.api_key = api_key
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
        with st.chat_message("assistant"):
            st.write(msg)
