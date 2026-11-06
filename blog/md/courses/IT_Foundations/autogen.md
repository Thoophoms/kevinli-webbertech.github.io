# AutoGen (Microsoft)

## Overview

AutoGen is an open-source framework developed by **Microsoft Research**, first released in **2023**. It enables building multi-agent applications through **conversational AI patterns** — agents talk to each other in structured conversations to collaboratively solve tasks.

- **Website:** [https://microsoft.github.io/autogen](https://microsoft.github.io/autogen)
- **GitHub:** [https://github.com/microsoft/autogen](https://github.com/microsoft/autogen)
- **Docs:** [https://microsoft.github.io/autogen/docs/Getting-Started](https://microsoft.github.io/autogen/docs/Getting-Started)

AutoGen's strengths:
- **Multi-agent dialogue** — agents send messages back and forth until a task is resolved
- **Code execution** — a built-in `UserProxyAgent` can execute code locally and feed results back
- **Flexible human involvement** — set `human_input_mode` to `ALWAYS`, `NEVER`, or `TERMINATE`
- **Group chat** — multiple agents in a single conversation, with a manager routing messages
- **Model agnostic** — supports OpenAI, Azure OpenAI, Gemini, Anthropic, and local models

---

## Agent Types

| Agent Type | Role |
|---|---|
| `AssistantAgent` | LLM-backed agent that generates responses and code |
| `UserProxyAgent` | Acts on behalf of the human; can execute code automatically |
| `GroupChatManager` | Routes messages to the right agent in a multi-agent group chat |
| `ConversableAgent` | Base class for custom agents with full control |

---

## Installation

```bash
pip install pyautogen
# For Docker-based code execution (recommended for production):
pip install pyautogen[docker]
```

---

## Two-Agent Code Generation

The simplest AutoGen pattern: an AssistantAgent generates code and a UserProxyAgent executes it.

```python
import os
import autogen

config_list = [{"model": "gpt-4o", "api_key": os.getenv("OPENAI_API_KEY")}]

assistant = autogen.AssistantAgent(
    name="Coder",
    llm_config={"config_list": config_list},
    system_message="You are an expert Python developer. Write clean, well-commented code."
)

user_proxy = autogen.UserProxyAgent(
    name="User",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=5,
    is_termination_msg=lambda msg: "TERMINATE" in msg.get("content", ""),
    code_execution_config={
        "work_dir": "coding_workspace",
        "use_docker": False
    }
)

user_proxy.initiate_chat(
    assistant,
    message="Write and run a Python script that fetches the current Bitcoin price from a public API and prints it."
)
```

---

## Group Chat with Multiple Agents

Group chats allow multiple specialized agents to collaborate on a single task.

```python
import os
import autogen

config_list = [{"model": "gpt-4o", "api_key": os.getenv("OPENAI_API_KEY")}]
llm_config = {"config_list": config_list}

planner = autogen.AssistantAgent("Planner", llm_config=llm_config,
    system_message="Break down tasks into clear steps.")
coder = autogen.AssistantAgent("Coder", llm_config=llm_config,
    system_message="Write Python code to implement the plan.")
reviewer = autogen.AssistantAgent("Reviewer", llm_config=llm_config,
    system_message="Review the code for bugs and improvements. Say TERMINATE when done.")
user_proxy = autogen.UserProxyAgent("User", human_input_mode="NEVER",
    code_execution_config={"work_dir": "workspace", "use_docker": False})

groupchat = autogen.GroupChat(
    agents=[user_proxy, planner, coder, reviewer],
    messages=[],
    max_round=12
)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

user_proxy.initiate_chat(manager, message="Build a CSV parser that reads sales data and outputs a summary report.")
```

---

## Human-in-the-Loop Modes

| Mode | Behavior |
|---|---|
| `NEVER` | Fully automated; no human input |
| `TERMINATE` | Human is asked when agent sends termination signal |
| `ALWAYS` | Human is prompted after every agent message |

```python
user_proxy = autogen.UserProxyAgent(
    name="MLOps_Lead",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=8,
    code_execution_config={"work_dir": "workspace", "use_docker": False}
)
```

---

## AutoGen v0.4 — AgentChat API

AutoGen v0.4 (2024) introduced a redesigned async-first API:

```python
import asyncio
import os
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY")
)

agent1 = AssistantAgent("Writer", model_client=model_client,
    system_message="Write a short blog post on the given topic.")
agent2 = AssistantAgent("Editor", model_client=model_client,
    system_message="Edit the blog post for clarity and grammar.")

team = RoundRobinGroupChat([agent1, agent2], max_turns=4)

asyncio.run(Console(team.run_stream(task="The future of AI agents in education")))
```

---

## Custom Reply Function

Override agent behavior entirely for specialized use cases:

```python
import autogen

def custom_reply(recipient, messages, sender, config):
    last_msg = messages[-1].get("content", "")
    # Custom logic — e.g., query a database, call an API, run a check
    return True, f"Custom response to: {last_msg[:50]}..."

agent = autogen.ConversableAgent(
    name="Custom_Agent",
    llm_config=False,  # no LLM — pure function-based
    human_input_mode="NEVER"
)
agent.register_reply(
    trigger=autogen.ConversableAgent,
    reply_func=custom_reply
)
```

---

## AutoGen Studio (No-Code UI)

AutoGen Studio is a web UI for prototyping multi-agent workflows without writing code:

```bash
pip install autogenstudio
autogenstudio ui --port 8081
```

Open `http://localhost:8081` to visually build agent teams, set system prompts, and run conversations.

---

## Summary

- **AutoGen** is Microsoft's framework for **conversational multi-agent** systems where LLM-backed agents collaborate through structured message exchange.
- The **AssistantAgent + UserProxyAgent** pair is the core pattern: one generates code or plans, the other executes and feeds back results.
- **GroupChat** + `GroupChatManager` enables specialized agents (planner, coder, reviewer) to work together.
- Built-in **code execution** (local or Docker) makes AutoGen ideal for tasks that generate and run code autonomously.
- Use `human_input_mode` to add human approval gates anywhere in the conversation.
- **AutoGen v0.4** introduced a modern async API (`autogen_agentchat`) with improved team orchestration primitives.
