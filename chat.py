import streamlit as st
import openai
import os
from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt

# ──────────────────────────────  PAGE CONFIG  ───────────────────────────── #
st.set_page_config(page_title="Intern-View", layout="wide")

# ─────────────────────────────  CUSTOM STYLES  ──────────────────────────── #
def inject_custom_css() -> None:
    st.markdown(
        """
        <style>
        /* ─── Desktop base styles ────────────────────────────────────────── */
        .stApp{
            background-color:#fff;
            font-family:'Roboto Mono',monospace;
        }
        html,body,.stApp,.stMarkdown,.stTextInput,.stChatMessage,
        .stSidebar,.block-container{
            font-family:'Roboto Mono',monospace!important;
            color:#243D66!important;
        }
        section[data-testid="stSidebar"]{width:230px;min-width:200px;}
        .css-1d391kg{font-size:1.4rem;font-weight:700;color:#243D66;}
        .css-1v3fvcr{font-size:1rem;color:#243D66;}
        .stTextInput>div>div>input{
            border:1px solid #243D66;border-radius:8px;color:#243D66;
        }
        .element-container:has(.stChatMessage){margin-bottom:1.5rem;}
        .stChatMessage.user img{background:#FF7F66;padding:4px;}
        .stChatMessage.assistant img{background:#243D66;padding:4px;}
        h1,h2,h3,h4,h5,h6{color:#243D66;}
        .stChatMessage img{border-radius:50%;}

        /* ─── Mobile overrides ───────────────────────────────────────────── */
        @media (max-width:768px){
            section[data-testid="stSidebar"]{display:none;}
            .block-container{padding:1rem!important;}
            h1{font-size:1.6rem;}h2{font-size:1.3rem;}
            img{max-width:100%;height:auto;}
            .stTextInput>div>div>input{font-size:0.9rem;}
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

inject_custom_css()

# ───────────────────────────────  HELPERS  ──────────────────────────────── #
def simple_rag_retrieve(query:str, folder:Path=Path(__file__).parent/"data") -> str:
    """Return up to 3 snippets from local .md docs containing the query."""
    docs=[]
    for md_file in folder.glob("*.md"):
        content=md_file.read_text()
        if query.lower() in content.lower():
            docs.append(f"### {md_file.name}:\n{content[:800]}")
    return "\n\n".join(docs[:3])

# ─────────────────────────────  API & ASSETS  ───────────────────────────── #
api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("❌ OpenAI API key not found. Set it in .streamlit/secrets.toml or as an env var.")
    st.stop()

avatar_path = Path(__file__).parent/"chatbot.png"
if avatar_path.exists():
    avatar_img = Image.open(avatar_path).convert("RGB")
    avatar_img.thumbnail((60,60))

# ───────────────────────────────  HEADER  ───────────────────────────────── #
st.title("*INTERN-VIEW*")
st.subheader("Ferréol’s AI-Powered Internship Report")
st.markdown(
    "Welcome to **Intern-View**, your interactive window into Ferréol’s internship at KickImpact. "
    "Ask what he built, learned, or contributed — this chatbot has all the answers."
)
if avatar_path.exists():
    st.image(str(avatar_path), width=160)

# ───────────────────────────  SAMPLE QUESTIONS  ─────────────────────────── #
with st.expander("💡 Example of questions you could ask ", expanded=False):
    st.markdown(
        """
        - What did Ferréol build during his internship?  
        - What is KickImpact?  
        - What did Ferréol do in week 3?  
        - What skills did Ferréol develop around AI?   
        - Is Ferréol a good fit for a strategy analyst role?  
        - Who is Nicolas?  
        - Etc...
        """
    )

# ──────────────────────  INTERNSHIP HIGHLIGHT IMAGES  ───────────────────── #
highlight_images=[
    ("conference.jpeg","AI for Good Summit in Geneva – AI for Food Systems session."),
    ("bike.jpeg",'Traditional bike ride at Salève’s "Col de la Croisette" before work.'),
    ("lake.jpg","Lunch-break swim at the lake with Nicolas."),
    ("spaces.jpg","Working at Spaces coworking on Quai de l’Île."),
]

with st.expander("📸 Some Internship Highlights", expanded=False):
    for fname,caption in highlight_images:
        img_path=Path(__file__).parent/fname
        if img_path.exists():
            st.image(Image.open(img_path),caption=caption,width=600)

# ──────────────────────────  CHATBOT INSTRUCTIONS  ──────────────────────── #
system_prompt="""
You are Intern-View, Ferréol de la Ville’s AI-powered internship assistant.

• Answer **only** about Ferréol’s internship at KickImpact (Jun-Jul 2025).  
• Be clear, concise, structured; no fluff.  
• Use bullet points for lists; **bold** key info.  
• Follow STAR when relevant; cite tangible outcomes.  
• If a question is vague, politely re-focus on internship scope.  
"""

with open(Path(__file__).parent/"internship_summary.md") as f:
    context=f.read()

# ───────────────────────────────  SIDEBAR  ──────────────────────────────── #
st.sidebar.subheader("Some Context...")
st.sidebar.markdown(
    "Ferréol completed a 2-month internship (June – July 2025) at KickImpact, "
    "a Swiss impact-investment startup founded by Nicolas Couture-Miambanzila."
)
st.sidebar.markdown("His work focused on **AI applications** in impact project analysis, internal tools, and startup research.")

labels=[
    "Meetings with AI specialists","Data analysis (Excel/Python)",
    "Landing page (Framer)","AI platform for impact fund",
    "Internal AI optimisation","Testing AI tools",
    "AI conferences","Research on AI opportunities",
]
sizes=[5,15,15,35,15,5,5,5]
fig,ax=plt.subplots(figsize=(6,6))
wedges,_,_=ax.pie(sizes,startangle=90,autopct='%1.1f%%',
                  textprops={'color':'white','fontsize':9},
                  wedgeprops={'edgecolor':'white'})
ax.axis('equal')
ax.legend(wedges,labels,title="Tasks",loc="lower center",
          bbox_to_anchor=(0.5,-0.2),ncol=2,fontsize=8)
st.sidebar.markdown("---")
st.sidebar.subheader("Time Task Breakdown")
st.sidebar.pyplot(fig)
st.sidebar.markdown("---")
st.sidebar.subheader("Project Links")
st.sidebar.markdown(
    "- [KickImpact Landing Page](https://kickimpact.framer.website/) 🌐  \n"
    "- [AI Project Submission Platform](https://impact-project-room5.streamlit.app) 📥"
    "- [In progress website HTML/CSS version](https://impact-project-room-v285w031.sites.blink.new) 🖥️"
)

# ─────────────────────────────  CHAT STATE  ─────────────────────────────── #
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

# ───────────────────────────────  CHAT LOOP  ────────────────────────────── #
user_input=st.chat_input("Ask a question...")
if user_input:
    st.session_state.chat_history.append(("user",user_input))
    context_snippets=simple_rag_retrieve(user_input) or context
    openai.api_key=api_key
    with st.spinner("Thinking..."):
        response=openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role":"system","content":system_prompt+"\n\nContext:\n"+context_snippets},
                      *[{"role":r,"content":m} for r,m in st.session_state.chat_history]]
        )
        reply=response.choices[0].message.content
    st.session_state.chat_history.append(("assistant",reply))

for role,msg in st.session_state.chat_history:
    (st.chat_message(role).write(msg) if role=="user"
     else st.chat_message("assistant").write(msg))
