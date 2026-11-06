# How to Get an OpenAI API Key

## Overview

An OpenAI API key allows you to programmatically access OpenAI's models (GPT-4, GPT-3.5, DALL·E, Whisper, etc.) from your own applications, scripts, and tools.

---

## Step 1: Create an OpenAI Account

1. Go to [https://platform.openai.com](https://platform.openai.com)
2. Click **Sign Up** if you don't have an account, or **Log In** if you do.
3. Complete the registration using your email, Google, or Microsoft account.

---

## Step 2: Navigate to the API Keys Page

1. After logging in, click on your **profile icon** (top-right corner).
2. Select **"Your profile"** or go directly to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys).
3. You will see the **API Keys** management page.

---

## Step 3: Create a New API Key

1. Click **"+ Create new secret key"**.
2. Optionally give it a name (e.g., `my-project-key`).
3. Click **Create secret key**.
4. **Copy the key immediately** — it will only be shown once.

> ⚠️ **Important:** Store your API key in a safe place. You cannot retrieve it again after closing the dialog. If lost, you must generate a new one.

---

## Step 4: Set Up Billing (Required for API Usage)

Free-tier usage is limited. To use the API beyond free credits:

1. Go to [https://platform.openai.com/settings/organization/billing](https://platform.openai.com/settings/organization/billing).
2. Click **"Add payment method"**.
3. Enter your credit card details.
4. Set a **usage limit** to avoid unexpected charges (recommended).

---

## Step 5: Use the API Key in Your Project

### Option A: Environment Variable (Recommended)

Set the key as an environment variable so it is never hardcoded in source code.

**Linux / macOS:**
```bash
export OPENAI_API_KEY="sk-..."
```

To make it persistent, add it to your `~/.bashrc` or `~/.zshrc`:
```bash
echo 'export OPENAI_API_KEY="sk-..."' >> ~/.bashrc
source ~/.bashrc
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY = "sk-..."
```

### Option B: `.env` File (for local development)

Create a `.env` file in your project root:
```
OPENAI_API_KEY=sk-...
```

Then load it in Python using `python-dotenv`:
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

> ⚠️ **Never commit your `.env` file to Git.** Add it to `.gitignore`:
> ```
> .env
> ```

### Option C: Pass Directly in Code (NOT recommended for production)

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")  # Avoid this in production
```

---

## Step 6: Test the API Key

Install the OpenAI Python library:
```bash
pip install openai
```

Run a quick test:
```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello!"}]
)

print(response.choices[0].message.content)
```

If you see a response like `Hello! How can I help you today?`, your key is working correctly.

---

## Security Best Practices

| Practice | Description |
|---|---|
| Use environment variables | Never hardcode keys in source files |
| Restrict key permissions | Use project-scoped keys when available |
| Set spending limits | Configure monthly usage caps in the dashboard |
| Rotate keys regularly | Delete and recreate keys periodically |
| Never share keys | Do not post keys in Slack, GitHub, or email |

---

## Troubleshooting

| Error | Likely Cause | Fix |
|---|---|---|
| `401 Unauthorized` | Invalid or expired key | Regenerate the key |
| `429 Too Many Requests` | Rate limit exceeded | Wait and retry, or upgrade plan |
| `insufficient_quota` | No billing set up or credits exhausted | Add payment method |
| `KeyError: OPENAI_API_KEY` | Environment variable not set | Run `export OPENAI_API_KEY=...` |

---

## References

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [API Keys Dashboard](https://platform.openai.com/api-keys)
- [Usage & Billing](https://platform.openai.com/settings/organization/billing)
- [OpenAI Python SDK on GitHub](https://github.com/openai/openai-python)
