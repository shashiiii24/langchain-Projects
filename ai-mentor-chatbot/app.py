import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate

st.sidebar.title("About")
st.sidebar.subheader("AI Chatbot Mentor")
st.sidebar.markdown(""" It's an AI-powered chatbot mentor that assists users in learning various programming and data science topics through interactive conversations. """)
st.sidebar.markdown("Developed by ShashiKiran ")


# ---------------- LOAD ENV ----------------
load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("hugging_face")


# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Chatbot Mentor", page_icon="🤖")


# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "module" not in st.session_state:
    st.session_state.module = None

if "chat" not in st.session_state:
    st.session_state.chat = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = None


# ---------------- MODULES ----------------
MODULES = [
    "Python🐍",
    "SQL🗂️",
    "EDA📊",
    "Machine Learning",
    "Deep Learning🧬",
    "LangChain⛓️",
    "Generative AI",
    "Agentic AI",
]


# ---------------- MODEL CHOICES ----------------
MODELS = {
    "Google": "google/gemma-2-9b",
    "Meta": "meta-llama/Llama-3.1-8B-Instruct",
    "DeepSeek": "deepseek-ai/DeepSeek-V3.2"
}


REJECTION_MSG = (
    "Sorry, I don’t know about this question. Please ask something related to the selected module."
)



# ===================== HOME PAGE =====================
if st.session_state.page == "home":

    st.title("📝:rainbow[AI Chatbot Mentor]")
    st.subheader(":red[Your personalized AI learning Assistant]")

    # ---- SELECT MODEL ----
    st.write("#### ✍️Select your LLM Model")
    selected_model = st.radio(
        "Choose LLM",
        list(MODELS.keys()),
        horizontal=True
    )

    if selected_model:
        st.session_state.selected_model = MODELS[selected_model]

    # ---- SELECT MODULE BUTTONS ----
    st.write("#### 👉 Select a Learning Module")
    cols = st.columns(3)
    selected_module = None

    for idx, module in enumerate(MODULES):
        if cols[idx % 3].button(module):
            selected_module = module

    if st.session_state.selected_model and selected_module:
        st.session_state.module = selected_module
        st.session_state.page = "chat"
        st.session_state.chat = []
        st.rerun()



# ===================== CHAT PAGE =====================
if st.session_state.page == "chat":

    st.title(f"🎯 {st.session_state.module} Mentor")
    st.caption(f"Model Used: {st.session_state.selected_model}")

    # ---------------- LLM ----------------
    base_llm = HuggingFaceEndpoint(
        repo_id=st.session_state.selected_model,
        task="conversational",
        temperature=0.7,
        max_new_tokens=512,
    )
    llm = ChatHuggingFace(llm=base_llm)

    # ---------------- PROMPT ----------------
    prompt_template = PromptTemplate(
        input_variables=["question"],
        template=f"""
You are a mentor ONLY for {st.session_state.module}.
Answer questions ONLY related to {st.session_state.module}.
If outside domain, reply exactly:
"{REJECTION_MSG}"

Question: {{question}}
        """
    )


    # ---------------- SHOW CHAT HISTORY ----------------
    for msg in st.session_state.chat:

        if msg["role"] == "user":
            col1, col2 = st.columns([4,4])
            with col1:
                pass
            with col2:
                with st.chat_message("user"):
                    st.write(msg["content"])

        else:
            col1, col2 = st.columns([3,1])
            with col1:
                with st.chat_message("assistant"):
                    st.write(msg["content"])
            with col2:
                pass


    # ---------------- CHAT INPUT ----------------
    user_input = st.chat_input("Ask your question...")

    if user_input:
        st.session_state.chat.append({"role":"user","content":user_input})

        formatted_prompt = prompt_template.format(question=user_input)

        response = llm.invoke(formatted_prompt)

        assistant_reply = (
            response.content
            if hasattr(response, "content")
            else str(response)
        )

        st.session_state.chat.append({"role":"assistant","content":assistant_reply})

        st.rerun()



    # ---------------- DOWNLOAD CHAT ----------------
    if st.session_state.chat:
        chat_text = ""
        for msg in st.session_state.chat:
            chat_text += f"{msg['role']}: {msg['content']}\n\n"

        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

        st.download_button(
            "📥 Download Chat History",
            chat_text,
            file_name=f"ChatHistory_{timestamp}.txt",
            mime="text/plain"
        )



    if st.button("⬅ Back to Menu"):
        st.session_state.page = "home"
        st.session_state.chat = []
        st.rerun()
