# Intern-View: Ferréol's AI-Powered Internship Report
import streamlit as st
st.set_page_config(page_title="Intern-View", layout="wide")
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
                background-color: white;
                font-family: 'Roboto Mono', monospace;
            }
            html, body, .stApp, .stMarkdown, .stTextInput, .stChatMessage, .stSidebar, .block-container {
                font-family: 'Roboto Mono', monospace !important;
                color: #243D66 !important;
            }

            /* Style sidebar */
            .css-1d391kg {  /* Sidebar title */
                font-size: 1.4rem;
                font-weight: 700;
                color: #243D66;
            }
            .css-1v3fvcr {  /* Sidebar markdown */
                font-size: 1rem;
                color: #243D66;
            }

            /* Style input box */
            .stTextInput>div>div>input {
                border: 1px solid #243D66;
                border-radius: 8px;
                color: #243D66;
                font-family: 'Roboto Mono', monospace;
            }

            /* Style chat messages */
            .element-container:has(.stChatMessage) {
                margin-bottom: 1.5rem;
            }

            /* Style header text */
            h1, h2, h3, h4, h5, h6 {
                font-family: 'Roboto Mono', monospace;
                color: #243D66;
            }

            /* Round avatar image */
            .stChatMessage img {
                border-radius: 50%;
            }
        </style>
    """, unsafe_allow_html=True)

inject_custom_css()

def simple_rag_retrieve(query, folder=Path(__file__).parent / "data"):
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

avatar_img = Image.open(Path(__file__).parent / "chatbot.png").convert("RGB")
avatar_img.thumbnail((60, 60))  # Resize for chat bubble

st.title("*INTERN-VIEW*")
st.subheader("Ferréol’s AI-Powered Internship Report")
st.markdown("Welcome to **Intern-View**, your interactive window into Ferréol’s internship at KickImpact. Ask what he built, learned, or contributed — this chatbot has all the answers.")

st.image(str(Path(__file__).parent / "chatbot.png"), width=160, use_container_width=False)

# Example questions expander
with st.expander("💡 Questions you could ask", expanded=False):
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

You exist only to answer questions about Ferréol’s internship at KickImpact (May–June 2025). You are NOT a general assistant.

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
with open(Path(__file__).parent / "data" / "internship_summary.md", "r") as f:
    context = f.read()

# Sidebar
st.sidebar.subheader("Some Context...")
st.sidebar.markdown("""Ferréol completed a 2-month internship (May–June 2025) at KickImpact, a Swiss impact investment startup founded by Nicolas Couture-Miambanzila.

His work focused on **AI applications** in impact project analysis, internal tools, and startup research.""")

import matplotlib.pyplot as plt

# Pie chart data
labels = [
    "Meetings with AI specialists", "Data analysis (Excel/Python)",
    "Landing page (Framer)", "AI platform for impact fund",
    "Internal AI optimization", "Testing AI tools",
    "AI conferences", "Research on AI opportunities"
]
sizes = [5, 15, 15, 35, 15, 5, 5, 5]
colors = ['#243D66', '#516F98', '#D97A45', '#6f8492', '#9FB0C1', '#FFAD99', '#D6DCE5', '#8DA4C8']

fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    colors=colors,
    startangle=90,
    autopct='%1.1f%%',
    textprops={'color': "white", 'fontsize': 9},
    wedgeprops={'edgecolor': 'white'}
)
ax.axis('equal')
ax.legend(wedges, labels, title="Tasks", loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=2, fontsize=8)

st.sidebar.markdown("---")
st.sidebar.subheader("Time Task Breakdown")
st.sidebar.pyplot(fig, use_container_width=True)

# Chat state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask a question...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    context_snippets = simple_rag_retrieve(user_input)
    if not context_snippets:
        context_snippets = context  # fallback to full context

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
