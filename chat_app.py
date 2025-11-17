# import streamlit as st
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from huggingface_hub import login
# import os
# from dotenv import load_dotenv

# # ---------------------------
# # Load environment variables
# # ---------------------------
# load_dotenv()
# hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# if not hf_token:
#     st.error("❌ Hugging Face API token not found in .env file!")
#     st.stop()

# # Login to Hugging Face
# login(hf_token)

# # ---------------------------
# # Initialize model
# # ---------------------------
# llm = HuggingFaceEndpoint(
#     repo_id="mistralai/Mistral-7B-Instruct-v0.2",
#     task="text-generation"
# )
# chat = ChatHuggingFace(llm=llm)

# # ---------------------------
# # Streamlit setup
# # ---------------------------
# st.set_page_config(page_title="NovaMind Chat", page_icon="🤖", layout="centered")

# # ---------------------------
# # Custom CSS (Dark theme)
# # ---------------------------
# st.markdown("""
#     <style>
#         /* App background */
#         .stApp {
#             background-color: #0d1117;  /* dark matte */
#             color: #ffffff;
#             font-family: 'Segoe UI', sans-serif;
#         }

#         /* Chat container */
#         .chat-container {
#             max-width: 700px;
#             margin: 0 auto;
#             padding: 20px;
#         }

#         /* User messages */
#         .user-msg {
#             background: linear-gradient(135deg, #1e1e1e, #2b2b2b);
#             color: #f5f5f5;
#             padding: 12px 16px;
#             border-radius: 12px;
#             margin: 10px 0;
#             text-align: right;
#             box-shadow: 0 0 6px rgba(255,255,255,0.05);
#         }

#         /* Bot messages */
#         .bot-msg {
#             background: linear-gradient(135deg, #161b22, #0d1117);
#             color: #e0e0e0;
#             padding: 12px 16px;
#             border-radius: 12px;
#             margin: 10px 0;
#             text-align: left;
#             box-shadow: 0 0 6px rgba(0,0,0,0.3);
#         }

#         /* Input box */
#         .stChatInput textarea {
#             background-color: #1c1f24 !important;
#             color: #ffffff !important;
#             border: 1px solid #333 !important;
#             border-radius: 8px !important;
#         }

#         /* Header */
#         h1 {
#             text-align: center;
#             color: #00ffff;
#             font-weight: 600;
#         }
#         h3 {
#             text-align: center;
#             color: #999;
#             margin-top: -10px;
#         }

#         /* Hide Streamlit's watermark + menu */
#         footer {visibility: hidden;}
#         #MainMenu {visibility: hidden;}
#         header {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # ---------------------------
# # App title
# # ---------------------------
# st.markdown("<div class='chat-container'><h1>🤖 NovaMind Chat</h1><h3>Hugging Face powered AI Assistant</h3><hr></div>", unsafe_allow_html=True)

# # ---------------------------
# # Chat logic
# # ---------------------------
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# chat_box = st.container()

# # Display previous messages
# with chat_box:
#     for msg in st.session_state.messages:
#         if msg["role"] == "user":
#             st.markdown(f"<div class='user-msg'>🧑‍💻 {msg['content']}</div>", unsafe_allow_html=True)
#         else:
#             st.markdown(f"<div class='bot-msg'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

# # User input
# user_input = st.chat_input("Type your message...")

# if user_input:
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     st.markdown(f"<div class='user-msg'>🧑‍💻 {user_input}</div>", unsafe_allow_html=True)

#     with st.spinner("NovaMind is thinking..."):
#         response = chat.invoke(user_input)
#         bot_reply = response.content.strip()

#     st.session_state.messages.append({"role": "assistant", "content": bot_reply})
#     st.markdown(f"<div class='bot-msg'>🤖 {bot_reply}</div>", unsafe_allow_html=True)


import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from huggingface_hub import login
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not hf_token:
    st.error("❌ Hugging Face API token not found in .env file!")
    st.stop()

# Login to Hugging Face
login(hf_token)

# Create model
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)
chat = ChatHuggingFace(llm=llm)

# Page Config
st.set_page_config(page_title="NovaMind Chat", layout="centered")

# APP Title
st.title("🤖 NovaMind Chat")
st.write("Simple AI Chat powered by Hugging Face")

st.write("---")

# SESSION STORAGE
if "messages" not in st.session_state:
    st.session_state.messages = []

# SHOW PAST MESSAGES
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# CHAT INPUT AT BOTTOM
user_text = st.chat_input("Type your message…")

if user_text:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_text})
    st.chat_message("user").markdown(user_text)

    # Generate response
    with st.spinner("Thinking..."):
        response = chat.invoke(user_text)
        bot_reply = response.content.strip()

    # Add bot message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.chat_message("assistant").markdown(bot_reply)
