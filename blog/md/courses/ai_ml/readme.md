# Qwen Small App Run Guide

This folder now contains a runnable small app under `src/app.py`.
The lesson content remains in `qwen_small_app_example.md`.

## Goal
Run a simple Streamlit chat app that calls a Qwen model through an OpenAI-compatible API.

## Files
- `src/app.py`: Streamlit app code
- `qwen_small_app_example.md`: learning notes and full walkthrough
- `.env`: your API configuration (you create this locally)

## Setup

### 1) Open this folder
```bash
cd /home/kevinli/git/kevinli-webbertech.github.io/blog/md/courses/ai_ml
```

### 2) Create and activate virtual environment
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
```bash
cat > .env << 'EOF'
QWEN_API_KEY=your_real_api_key
QWEN_BASE_URL=https://your-openai-compatible-endpoint/v1
QWEN_MODEL=your-qwen-model-id
EOF
```

## How to Run

### Start the app
```bash
streamlit run src/app.py
```

### Open in browser
- `http://localhost:8501`

## Quick Checks
- If you see "Missing QWEN_API_KEY, QWEN_BASE_URL, or QWEN_MODEL in .env", check variable names and `.env` location.
- If you get 401, verify `QWEN_API_KEY`.
- If you get model-not-found, verify `QWEN_MODEL`.
- If connection fails, verify `QWEN_BASE_URL` and network access.
