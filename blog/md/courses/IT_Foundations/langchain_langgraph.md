# LangChain and LangGraph

## Overview

LangChain is an open-source framework launched in **2022** that makes it easier to build applications powered by large language models. Its core idea is the **chain** — a sequence of components (prompts, LLMs, tools, parsers) that can be composed into complex pipelines.

LangGraph is an extension of LangChain (by the same team) released in **2024** that models agentic workflows as **directed graphs** — a set of nodes (functions) connected by edges (transitions). It was designed to overcome the limitations of linear chains when building complex, stateful, multi-step agents.

- **LangChain:** [https://www.langchain.com](https://www.langchain.com) | [GitHub](https://github.com/langchain-ai/langchain) | [Docs](https://python.langchain.com)
- **LangGraph:** [https://www.langchain.com/langgraph](https://www.langchain.com/langgraph) | [GitHub](https://github.com/langchain-ai/langgraph) | [Docs](https://langchain-ai.github.io/langgraph)

---

## LangChain

### What LangChain Provides

- **Model integrations** — Works with OpenAI, Anthropic, Google, Mistral, Ollama (local), and dozens more
- **Prompt templates** — Reusable, parameterized prompts with variable injection
- **Output parsers** — Structured extraction (JSON, lists, Pydantic models) from LLM responses
- **Retrievers** — Interface to vector stores and document sources for RAG (Retrieval-Augmented Generation)
- **Agents and tools** — ReAct-style agents with built-in tool integrations

### LangChain Expression Language (LCEL)

LCEL is LangChain's modern declarative syntax for composing chains using the `|` pipe operator:

```python
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))

prompt = ChatPromptTemplate.from_template("Explain {topic} in simple terms.")
parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({"topic": "quantum computing"})
print(result)
```

### ReAct Agent

```python
import os
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
tools = [DuckDuckGoSearchRun()]

agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
result = executor.invoke({"input": "What is the latest news about AI agents?"})
print(result["output"])
```

### RAG Pipeline with LangChain

```python
import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Load and embed documents
embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
vectorstore = FAISS.from_texts(
    ["LangChain is a framework for LLM apps.", "FAISS is a vector similarity search library."],
    embedding=embeddings
)
retriever = vectorstore.as_retriever()

# Build RAG chain
llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
prompt = ChatPromptTemplate.from_template(
    "Answer the question based on the context:\n\nContext: {context}\n\nQuestion: {question}"
)

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print(rag_chain.invoke("What is LangChain?"))
```

### When to Use LangChain

| Use Case | Good Fit? |
|---|---|
| RAG / document Q&A | ✅ Excellent |
| Simple LLM chains | ✅ Excellent |
| Complex stateful agents | ⚠️ Use LangGraph instead |
| Multi-agent systems | ⚠️ Use LangGraph instead |
| Production APIs | ✅ With LangServe |

---

## LangGraph

### What is LangGraph?

LangGraph was designed to overcome the limitations of linear chains when building:

- **Multi-step agents** that loop, branch, or retry
- **Human-in-the-loop** workflows requiring approval gates
- **Multi-agent systems** where agents hand off work to one another
- **Persistent, stateful conversations** that survive across sessions

The key insight: rather than running straight from A → B → C, real agents need **cycles** — the ability to observe a result, decide what to do next, and loop back.

### Core Concepts

| Concept | Description |
|---|---|
| **State** | A typed dictionary shared across all nodes; each node reads and writes state |
| **Node** | A Python function that takes state and returns updated state |
| **Edge** | A transition between nodes; can be unconditional or conditional |
| **Conditional Edge** | A function that decides which node to go to next based on state |
| **Checkpointer** | Persists state to disk/DB, enabling long-running and resumable workflows |

### Graph Basics

```python
from langgraph.graph import StateGraph, END

graph = StateGraph(AgentState)
graph.add_node("agent", call_agent)
graph.add_node("tools", call_tools)
graph.add_edge("agent", "tools")
graph.add_conditional_edges("tools", should_continue, {"continue": "agent", "end": END})
```

### Full LangGraph Agent with Tool Calling

```python
import os
import json
from typing import TypedDict, Annotated, Sequence
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages

# --- Define state ---
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

# --- Define tools ---
@tool
def get_stock_price(ticker: str) -> str:
    """Get the current stock price for a given ticker symbol."""
    prices = {"AAPL": "$189.50", "GOOGL": "$175.20", "MSFT": "$415.80"}
    return prices.get(ticker.upper(), f"No data for {ticker}")

tools = [get_stock_price]
tools_by_name = {t.name: t for t in tools}

# --- Set up LLM ---
llm = ChatOpenAI(
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY")
).bind_tools(tools)

# --- Define nodes ---
def call_llm(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

def call_tools(state: AgentState) -> AgentState:
    last_message = state["messages"][-1]
    results = []
    for tc in last_message.tool_calls:
        tool_fn = tools_by_name[tc["name"]]
        output = tool_fn.invoke(tc["args"])
        results.append(ToolMessage(content=str(output), tool_call_id=tc["id"]))
    return {"messages": results}

def should_continue(state: AgentState) -> str:
    last = state["messages"][-1]
    return "tools" if getattr(last, "tool_calls", None) else END

# --- Build graph ---
graph = StateGraph(AgentState)
graph.add_node("llm", call_llm)
graph.add_node("tools", call_tools)
graph.set_entry_point("llm")
graph.add_conditional_edges("llm", should_continue, {"tools": "tools", END: END})
graph.add_edge("tools", "llm")

app = graph.compile()

# --- Run ---
result = app.invoke({"messages": [HumanMessage(content="What is the stock price of AAPL?")]})
print(result["messages"][-1].content)
```

### LangGraph vs LangChain

| Feature | LangChain | LangGraph |
|---|---|---|
| Execution model | Linear / sequential | Graph with cycles |
| Loops & branching | Limited | Native |
| State management | Manual | Built-in typed state |
| Human-in-the-loop | Workaround needed | First-class support |
| Multi-agent | Difficult | Native |
| Best for | RAG, simple chains | Complex agents, workflows |

---

## Installation

```bash
pip install langchain langchain-openai langchain-community
pip install langgraph
```

---

## Summary

- **LangChain** is the composable building-block layer: prompts, LLMs, tools, retrievers, and chains connected with the `|` pipe operator (LCEL).
- **LangGraph** is the orchestration layer: stateful directed graphs with native support for cycles, branching, human-in-the-loop, and multi-agent handoffs.
- Use LangChain for RAG pipelines and simple LLM chains; use LangGraph when your agent needs to loop, branch, or maintain state across multiple steps.
- Both are MIT-licensed and work with any LLM provider (OpenAI, Anthropic, Ollama, etc.).
