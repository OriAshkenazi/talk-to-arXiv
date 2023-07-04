import openai
import streamlit as st
import os
from PyPDF2 import PdfReader
from tenacity import retry, wait_random_exponential, stop_after_attempt

openai.api_key = os.getenv('OPENAI_API_KEY')
model = os.getenv('GPT_MODEL')
embedding_model = os.getenv('EMBEDDING_MODEL')

st.title("talk-to-arXiv")

uploaded_file = st.file_uploader("Upload an article", type=("txt", "md"))

@retry(wait=wait_random_exponential(min=1, max=40), stop=stop_after_attempt(3))
def embedding_request(text):
    response = openai.Embedding.create(model=embedding_model, documents=[text])
    return response

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    if msg["role"] == "assistant":
        st.write("AI: "+msg["content"])  # Use st.write to display messages
    else:
        st.write("User: "+msg["content"])

if prompt := st.text_input("Enter your message:"):  # Use text_input for user input
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.write("User: "+prompt)
    response = openai.ChatCompletion.create(model=model, messages=st.session_state.messages)
    msg = response['choices'][0]['message']
    st.session_state.messages.append(msg)
    st.write("AI: "+msg["content"])
