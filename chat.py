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
            section[data-testid="stSidebar"] {
                width: 230px;
                min-width: 200px;
            }
            .css-1d391kg { font-size: 1.4rem; font-weight: 700; color: #243D66; }
            .css-1v3fvcr { font-size: 1rem; color: #243D66; }

            /* Style input box */
            .stTextInput>div>div>input {
                border: 1px solid #243D66;
                border-radius: 8px;
                color: #243D66;
                font-family: 'Roboto Mono', monospace;
            }

            /* Style chat messages */
            .element-container:has(.stChatMessage) { margin-bottom: 1.5rem; }
            .stChatMessage.user img { background-color: #FF7F66; padding: 4px; }
            .stChatMessage.assistant img { background-color: #243D66; padding: 4px; }
            h1, h2, h3, h4, h5, h6 { font-family: 'Roboto Mono', monospace; color: #243D66; }
            .stChatMessage img { border-radius: 50%; }
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

avatar_path = Path(__file__).parent / "chatbot.png"
if avatar_path.exists():
    avatar_img = Image.open(avatar_path).convert("RGB")
    avatar_img.thumbnail((60, 60))

st.title("*INTERN-VIEW*")
st.subheader("Ferréol’s AI-Powered Internship Report")
st.markdown("Welcome to **Intern-View**, your interactive window into Ferréol’s internship at KickImpact. Ask what he built, learned, or contributed — this chatbot has all the answers.")

if avatar_path.exists():
    st.image(str(avatar_path), width=160)

# Example questions
with st.expander("💡 Questions you could ask", expanded=False):
    st.markdown("""
    - What did Ferréol build during his internship?
    - What is KickImpact?
    - What did Ferréol do in week 3?
    - What skills did Ferréol develop around AI?
    - Who said what during the internship?
    - Tell me a secret about the internship!
    - Is Ferréol a good fit for a strategy analyst role?
    - Who is Nicolas?
    """)

# Internship highlights
highlight_images = [
    ("conference.jpeg", "AI for Good Summit in Geneva conference on AI for Food Systems."),
    ("bike.jpeg", 'Traditional bike ride at Salève’s "Col de la Croisette" before work.'),
    ("lake.jpg", "Going to lunch break swim at the lake with Nicolas."),
    ("spaces.jpg", "Working at Spaces coworking on Quai de l'Île.")
]

with st.expander("📸 Some Internship Highlights", expanded=False):
    for fname, caption in highlight_images:
        img_path = Path(__file__).parent / fname
        if img_path.exists():
            img = Image.open(img_path)
            st.image(img, caption=caption, width=600)  

system_prompt = """
You are Intern-View, Ferréol de la Ville’s AI-powered internship assistant.

You exist only to answer questions about Ferréol’s internship at KickImpact (May–June 2025). You are NOT a general assistant.

- Always reply as if you are a chatbot version of Ferréol’s final report.
- Be clear, concise, structured and specific, no fluff.
- Follow the STAR method when relevant and you have enough context, don't invent anything.
- Confident but not arrogant.
- Use bullet points when response is a list.
- Concentrate on tangible or measurable elements.

If someone asks whether Ferréol is suited for a role, use specific examples to justify your answer.

If a user types something vague, politely re-focus the conversation around the internship and Ferréol's experience.

Answer only based on the loaded context.
"""

# Load host context
with open(Path(__file__).parent / "internship_summary.md", "r") as f:
    context = f.read()

# Sidebar
st.sidebar.subheader("Some Context...")
st.sidebar.markdown(
    "Ferréol completed a 2-month internship (June-July 2025) at KickImpact,"
    " a Swiss impact investment startup founded by Nicolas Couture-Miambanzila."
)
st.sidebar.markdown("His work focused on **AI applications** in impact project analysis, internal tools, and startup research.")

import matplotlib.pyplot as plt
# Time allocation pie chart
labels = [
    "Meetings with AI specialists", "Data analysis (Excel/Python)",
    "Landing page (Framer)", "AI platform for impact fund",
    "Internal AI optimization", "Testing AI tools",
    "AI conferences", "Research on AI opportunities"
]

sizes = [5, 15, 15, 35, 15, 5, 5, 5]

fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    sizes, startangle=90, autopct='%1.1f%%', textprops={'color':'white','fontsize':9}, wedgeprops={'edgecolor':'white'}
)
ax.axis('equal')
ax.legend(wedges, labels, title="Tasks", loc="lower center", bbox_to_anchor=(0.5,-0.2), ncol=2, fontsize=8)

st.sidebar.markdown("---")
st.sidebar.subheader("Time Task Breakdown")
st.sidebar.pyplot(fig)

st.sidebar.markdown("---")
st.sidebar.subheader("Project Links")
st.sidebar.markdown(
    "- [KickImpact Landing Page](https://kickimpact.framer.website/) 🌐\n"
    "- [AI Project Submission Platform](https://impact-project-room5.streamlit.app) 📥"
)

# Chat state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask a question...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    context_snippets = simple_rag_retrieve(user_input) or context
    openai.api_key = api_key

    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt + "\n\nContext:\n" + context_snippets},
                *[{"role": r, "content": msg} for r, msg in st.session_state.chat_history]
            ]
        )
        reply = response.choices[0].message.content
        st.session_state.chat_history.append(("assistant", reply))

for role, msg in st.session_state.chat_history:
    if role == 'user': st.chat_message('user').write(msg)
    else: st.chat_message('assistant').write(msg)
