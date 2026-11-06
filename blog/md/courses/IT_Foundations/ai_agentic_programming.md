# AI Agentic Programming

## What is an AI Agent?

An **AI agent** is an autonomous software system that perceives its environment, makes decisions, and takes actions to achieve a specified goal — often without requiring step-by-step human instruction. Unlike a simple prompt-response model, an agent:

- Maintains **memory** of prior interactions
- Has access to **tools** (web search, code execution, APIs, file systems)
- Plans and **reasons** across multiple steps
- **Iterates** until a goal is met or a stopping condition is reached

---

## Core Components of an AI Agent

| Component | Description |
|-----------|-------------|
| **LLM (Brain)** | A large language model (e.g., GPT-4o, Claude, Gemini) that reasons and generates plans |
| **Tools** | External functions the agent can call: web search, calculator, code interpreter, database queries |
| **Memory** | Short-term (in-context) and long-term (vector DB, external storage) retention of facts |
| **Planner** | Decides what action to take next, often using a ReAct or Chain-of-Thought loop |
| **Executor** | Runs the selected action and returns results to the LLM |

---

## Agent Reasoning Patterns

### 1. ReAct (Reason + Act)

The agent alternates between **Thought**, **Action**, and **Observation** steps:

```
Thought: I need to find today's top AI news.
Action: web_search("top AI news today")
Observation: [search results]
Thought: I found relevant results, let me summarize.
Final Answer: Here is a summary of today's top AI news...
```

### 2. Chain-of-Thought (CoT)

The model is prompted to "think step by step" before producing an answer. Useful for math, logic, and planning.

### 3. Plan-and-Execute

The agent first creates a **plan** (list of sub-tasks), then executes each step independently. More robust for long-horizon tasks.

### 4. Reflexion

After each attempt the agent **evaluates** its own output and retries if the result was wrong or incomplete.

---

## Agentic Programming Frameworks

The major frameworks each take a distinct approach to agent orchestration. See their dedicated pages for full coverage with code examples and comparisons:

| Framework | Approach | Page |
|---|---|---|
| **LangChain / LangGraph** | Composable chains + stateful graph orchestration | [LangChain and LangGraph](langchain_langgraph.html) |
| **AutoGen** (Microsoft) | Conversational multi-agent chat with built-in code execution | [AutoGen](autogen.html) |
| **CrewAI** | Role-based agent crews for workflow automation | [CrewAI](crewai.html) |
| **OpenAI Agents SDK** | Lightweight first-party SDK for OpenAI models | [OpenAI Agents SDK](openai_agents_sdk.html) |

---

## Tool Use and Function Calling

Tools are the "hands" of an agent. They are defined as typed functions and passed to the LLM so it can decide when and how to call them.

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "execute_python",
            "description": "Run a Python code snippet and return the output",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {"type": "string", "description": "Python code to execute"}
                },
                "required": ["code"]
            }
        }
    }
]
```

Common tool categories:

- **Search** – DuckDuckGo, Tavily, Bing Search API
- **Code execution** – Python REPL, Jupyter kernel
- **File I/O** – read/write local or cloud files
- **APIs** – weather, stocks, calendars, databases
- **Browser** – Playwright, Selenium for web automation

---

## Memory in Agents

| Memory Type | Storage | Example |
|-------------|---------|---------|
| In-context | LLM window | Last N messages in chat history |
| External short-term | Redis / SQLite | Session-level key-value store |
| Long-term semantic | Vector DB (FAISS, Chroma, Pinecone) | User facts retrieved by similarity search |
| Episodic | Structured logs | Past task outcomes for reflection |

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
chain = ConversationChain(llm=llm, memory=memory, verbose=True)
chain.predict(input="My name is Alice.")
chain.predict(input="What is my name?")  # Agent remembers "Alice"
```

---

## Multi-Agent Systems

Multiple specialized agents collaborate to solve complex tasks:

```
User Request
     │
     ▼
 Orchestrator Agent
   ├──► Research Agent  ──► web_search, summarize
   ├──► Coder Agent     ──► write_code, run_tests
   └──► Reviewer Agent  ──► check_quality, approve
     │
     ▼
  Final Response
```

**Benefits:**
- Specialization — each agent excels at one thing
- Parallelism — agents can work concurrently
- Fault isolation — one agent failing doesn't crash the system

---

## Building a Simple Agent from Scratch (Python)

```python
import openai, json, os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def search_web(query: str) -> str:
    # Stub — replace with real search API
    return f"Results for '{query}': [Article 1], [Article 2]"

tools = [{
    "type": "function",
    "function": {
        "name": "search_web",
        "parameters": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"]
        }
    }
}]

messages = [{"role": "user", "content": "What are the top 3 AI agent frameworks in 2025?"}]

while True:
    response = client.chat.completions.create(
        model="gpt-4o", messages=messages, tools=tools, tool_choice="auto"
    )
    msg = response.choices[0].message
    messages.append(msg)

    if msg.tool_calls:
        for tc in msg.tool_calls:
            args = json.loads(tc.function.arguments)
            result = search_web(**args)
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": result
            })
    else:
        print("Agent:", msg.content)
        break
```

---

## Evaluation and Safety

### Evaluation Metrics

- **Task completion rate** – Did the agent achieve the goal?
- **Tool call accuracy** – Were the right tools called with correct arguments?
- **Hallucination rate** – Did the agent fabricate facts instead of using tools?
- **Latency / cost** – How many LLM calls and tokens were consumed?

### Safety Guardrails

- **Input validation** – sanitize user requests before passing to the agent
- **Tool permissions** – restrict which tools an agent can call
- **Output filtering** – check final responses for harmful content
- **Human-in-the-loop (HITL)** – require human approval for high-risk actions (e.g., sending emails, making purchases)
- **Rate limiting** – prevent runaway agentic loops from consuming excessive API tokens

---

## Practical Use Cases

| Domain | Agent Application |
|--------|------------------|
| Software Engineering | Code generation, debugging, PR review |
| Customer Support | Autonomous ticket resolution, FAQ answering |
| Data Analysis | Query generation, chart creation, report writing |
| Research | Literature search, summarization, hypothesis generation |
| DevOps | Infrastructure provisioning, log analysis, alerting |
| Education | Personalized tutoring, assignment grading |

---

## Popular Platforms and Tools (2025)

| Tool / Platform | Released | Description | Website |
|---|---|---|---|
| **LangChain** | 2022 | Modular framework for building LLM chains and agents | [langchain.com](https://www.langchain.com) |
| **LangGraph** | 2024 | Graph-based stateful agent orchestration | [langchain.com/langgraph](https://www.langchain.com/langgraph) |
| **AutoGen** | 2023 | Multi-agent conversation framework by Microsoft | [microsoft.github.io/autogen](https://microsoft.github.io/autogen) |
| **CrewAI** | 2023 | Role-based agent crews for workflow automation | [crewai.com](https://www.crewai.com) |
| **OpenAI Agents SDK** | 2025 | Lightweight first-party SDK for OpenAI models | [openai.github.io/openai-agents-python](https://openai.github.io/openai-agents-python/) |
| **Semantic Kernel** | 2023 | Microsoft's SDK for integrating AI into apps | [learn.microsoft.com/semantic-kernel](https://learn.microsoft.com/en-us/semantic-kernel/) |
| **Haystack** | 2021 | NLP/search pipeline with agent capabilities | [haystack.deepset.ai](https://haystack.deepset.ai) |
| **Agno (Phidata)** | 2024 | Multi-modal agents with memory and storage | [agno.com](https://www.agno.com) |


## Summary

AI agentic programming represents a paradigm shift from single-turn LLM calls to **autonomous, goal-directed systems** that can plan, use tools, remember context, and collaborate. Key takeaways:

1. Agents = LLM + Tools + Memory + Planning loop
2. Choose a framework (LangGraph, AutoGen, CrewAI) based on your complexity needs
3. Design tools carefully — they are the primary way agents interact with the real world
4. Always include safety guardrails and human-in-the-loop checkpoints for production systems
5. Evaluate agents rigorously: task success rate, tool accuracy, and cost efficiency

---

*Last updated: April 2026*
