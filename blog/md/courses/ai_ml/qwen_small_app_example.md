# Qwen Small App Example (Python + Streamlit)

## Goal
Build a small chat app that uses a Qwen model through an OpenAI-compatible API.

This guide shows you how to:
- configure environment variables safely
- build a minimal Streamlit chat UI
- call Qwen with `client.chat.completions.create(...)`
- run and test the app locally

## Setup

### 1) Prerequisites
- Python 3.9+
- `pip`
- A valid Qwen API key and endpoint
- A model ID available in your provider account

### 2) Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies
```bash
pip install --upgrade pip
pip install streamlit openai python-dotenv
```

### 4) Create `.env`
Create a file named `.env` in the same folder as `app.py`:

```env
QWEN_API_KEY=your_real_api_key
QWEN_BASE_URL=https://your-openai-compatible-endpoint/v1
QWEN_MODEL=your-qwen-model-id
```

Notes:
- Keep `/v1` in `QWEN_BASE_URL` for OpenAI-compatible endpoints.
- Use the exact model ID from your provider dashboard.

## Project Structure
```text
qwen_small_app/
├── .env
├── app.py
└── requirements.txt
```

Optional `requirements.txt`:
```txt
streamlit
openai
python-dotenv
```

## Code
Create `app.py`:

```python
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
```

## How to Run (Detailed)

### Step 1: Go to the project directory
```bash
cd /home/kevinli/git/kevinli-webbertech.github.io/blog/md/courses/ai_ml
```

### Step 2: Create and activate the environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install packages
```bash
pip install --upgrade pip
pip install streamlit openai python-dotenv
```

### Step 4: Create `.env`
```bash
cat > .env << 'EOF'
QWEN_API_KEY=your_real_api_key
QWEN_BASE_URL=https://your-openai-compatible-endpoint/v1
QWEN_MODEL=your-qwen-model-id
EOF
```

### Step 5: Save `app.py`
Copy the code from the **Code** section into `app.py`.

### Step 6: Start the app
```bash
streamlit run app.py
```

### Step 7: Open in browser
Open:
- `http://localhost:8501`

### Step 8: Quick test prompts
- "Summarize what overfitting means in three bullet points."
- "Write a Python function to reverse a string."
- "Explain SQL JOIN types with a simple example."

## Troubleshooting

1. Error: "Missing QWEN_API_KEY, QWEN_BASE_URL, or QWEN_MODEL"
- Cause: `.env` is missing keys or not in the same folder.
- Fix: verify `.env` location and key names.

2. HTTP 401 Unauthorized
- Cause: invalid API key.
- Fix: regenerate/update `QWEN_API_KEY`.

3. Model not found
- Cause: wrong `QWEN_MODEL` value.
- Fix: copy the exact model ID from provider dashboard.

4. Connection refused / timeout
- Cause: wrong endpoint or network issue.
- Fix: verify `QWEN_BASE_URL` and endpoint health.

5. Empty output
- Cause: provider-side issue or incompatible response.
- Fix: try a simpler prompt and confirm model supports chat completions.

## Optional Improvements
- Add a sidebar for temperature and max token controls.
- Add a "Clear chat" button.
- Log prompts/responses to a local JSON file for debugging.
