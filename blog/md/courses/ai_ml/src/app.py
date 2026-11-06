import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("QWEN_API_KEY")
BASE_URL = os.getenv("QWEN_BASE_URL")
MODEL = os.getenv("QWEN_MODEL")

if not API_KEY or not BASE_URL or not MODEL:
    raise RuntimeError("Missing QWEN_API_KEY, QWEN_BASE_URL, or QWEN_MODEL in .env")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

st.set_page_config(page_title="Qwen Small App", layout="centered")
st.title("Qwen Small Chat App")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

user_input = st.chat_input("Ask something...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_text = ""

        try:
            stream = client.chat.completions.create(
                model=MODEL,
                messages=st.session_state.messages,
                temperature=0.3,
                max_tokens=500,
                stream=True,
            )

            for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    full_text += delta
                    placeholder.write(full_text)

            if not full_text:
                full_text = "(No content returned)"
                placeholder.write(full_text)

            st.session_state.messages.append({"role": "assistant", "content": full_text})

        except Exception as e:
            placeholder.error(f"Request failed: {e}")
