# LangChain and LangGraph in MLOps

## Overview

LangChain and LangGraph are two foundational frameworks for building production-ready LLM (Large Language Model) applications. LangChain provides composable primitives — chains, tools, memory, and retrieval — while LangGraph extends that with stateful, graph-based multi-agent orchestration. Together they form the backbone of modern agentic MLOps pipelines.

---

## LangChain

### What Is LangChain?

LangChain is an open-source framework (Python and JavaScript) that simplifies building applications powered by language models. Its core idea: compose LLM calls with tools, data sources, and memory into reusable **chains**.

### Core Concepts

| Concept | Description |
|---|---|
| **LLM / ChatModel** | Wrapper around OpenAI, Anthropic, Ollama, etc. |
| **Prompt Template** | Parameterized prompt construction |
| **Chain** | Sequence of LLM calls and transformations |
| **Tool** | Function the LLM can invoke (search, calculator, API) |
| **Memory** | Conversation history storage (in-memory, Redis, etc.) |
| **Retriever** | Fetches relevant documents from a vector store |
| **Agent** | LLM that decides which tools to call and in what order |

### Installation

```bash
pip install langchain langchain-openai langchain-community
```

### Simple Chain Example

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful MLOps assistant."),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()

response = chain.invoke({"question": "What is model drift?"})
print(response)
```

### RAG (Retrieval-Augmented Generation) Pipeline

```python
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Build vector store from documents
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(
    ["MLflow tracks experiments", "Evidently detects data drift"],
    embedding=embeddings
)
retriever = vectorstore.as_retriever()

prompt = ChatPromptTemplate.from_template("""
Answer the question using only the following context:
{context}

Question: {question}
""")

llm = ChatOpenAI(model="gpt-4o-mini")

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print(rag_chain.invoke("What tools monitor ML models?"))
```

### Tool Use with LangChain Agents

```python
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

@tool
def get_model_accuracy(model_name: str) -> str:
    """Retrieve the latest accuracy for a deployed model."""
    # In production: query MLflow or your model registry
    return f"{model_name}: accuracy = 0.94"

llm = ChatOpenAI(model="gpt-4o-mini")
tools = [get_model_accuracy]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an MLOps agent. Use tools to answer questions."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

executor.invoke({"input": "What is the accuracy of the fraud_detection model?"})
```

---

## LangGraph

### What Is LangGraph?

LangGraph is a library built on top of LangChain for creating **stateful, multi-step, multi-agent workflows** modeled as directed graphs (nodes + edges). It is designed for scenarios where simple linear chains are insufficient — branching logic, cycles, human-in-the-loop approvals, and parallel agent execution.

### Key Concepts

| Concept | Description |
|---|---|
| **StateGraph** | The graph object that holds nodes and edges |
| **State** | A typed dictionary shared across all nodes |
| **Node** | A Python function that reads/writes state |
| **Edge** | A directed connection between nodes |
| **Conditional Edge** | Routes to different nodes based on state values |
| **Checkpointer** | Persists state for resumability and human-in-the-loop |
| **Subgraph** | A nested graph that acts as a single node |

### Installation

```bash
pip install langgraph langchain-openai
```

### Minimal Graph Example

```python
from typing import TypedDict
from langgraph.graph import StateGraph, END

class State(TypedDict):
    input: str
    result: str

def process(state: State) -> State:
    return {"result": f"Processed: {state['input']}"}

def review(state: State) -> State:
    print(f"Review node sees: {state['result']}")
    return state

graph = StateGraph(State)
graph.add_node("process", process)
graph.add_node("review", review)
graph.set_entry_point("process")
graph.add_edge("process", "review")
graph.add_edge("review", END)

app = graph.compile()
output = app.invoke({"input": "model metrics report"})
print(output)
```

### Conditional Routing

```python
from typing import Literal
from langgraph.graph import StateGraph, END

class State(TypedDict):
    score: float
    action: str

def evaluate(state: State) -> State:
    return {"action": "retrain" if state["score"] < 0.85 else "deploy"}

def retrain(state: State) -> State:
    print("Triggering retraining pipeline...")
    return state

def deploy(state: State) -> State:
    print("Deploying model to production...")
    return state

def route(state: State) -> Literal["retrain", "deploy"]:
    return state["action"]

graph = StateGraph(State)
graph.add_node("evaluate", evaluate)
graph.add_node("retrain", retrain)
graph.add_node("deploy", deploy)
graph.set_entry_point("evaluate")
graph.add_conditional_edges("evaluate", route)
graph.add_edge("retrain", END)
graph.add_edge("deploy", END)

app = graph.compile()
app.invoke({"score": 0.78})
```

### Human-in-the-Loop with Checkpointing

```python
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from typing import TypedDict

class State(TypedDict):
    plan: str
    approved: bool

def generate_plan(state: State) -> State:
    return {"plan": "Step 1: retrain. Step 2: evaluate. Step 3: deploy."}

def execute_plan(state: State) -> State:
    print(f"Executing: {state['plan']}")
    return state

def needs_approval(state: State) -> str:
    return "execute" if state.get("approved") else "wait"

checkpointer = MemorySaver()

graph = StateGraph(State)
graph.add_node("generate_plan", generate_plan)
graph.add_node("execute_plan", execute_plan)
graph.set_entry_point("generate_plan")
graph.add_conditional_edges("generate_plan", needs_approval, {
    "execute": "execute_plan",
    "wait": END
})
graph.add_edge("execute_plan", END)

app = graph.compile(checkpointer=checkpointer, interrupt_before=["execute_plan"])

thread = {"configurable": {"thread_id": "mlops-run-1"}}

# First run — stops before execute_plan for human review
app.invoke({"plan": "", "approved": False}, config=thread)

# Human reviews and approves, then resume
app.invoke({"approved": True}, config=thread)
```

### Multi-Agent Graph (Supervisor Pattern)

```python
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated
import operator

llm = ChatOpenAI(model="gpt-4o-mini")

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    next: str

def data_agent(state: AgentState) -> AgentState:
    response = llm.invoke("Summarize the latest data quality report.")
    return {"messages": [response.content], "next": "model_agent"}

def model_agent(state: AgentState) -> AgentState:
    context = state["messages"][-1]
    response = llm.invoke(f"Given this data summary, recommend model actions: {context}")
    return {"messages": [response.content], "next": "END"}

def route(state: AgentState) -> str:
    return state["next"]

graph = StateGraph(AgentState)
graph.add_node("data_agent", data_agent)
graph.add_node("model_agent", model_agent)
graph.set_entry_point("data_agent")
graph.add_conditional_edges("data_agent", route, {
    "model_agent": "model_agent"
})
graph.add_edge("model_agent", END)

app = graph.compile()
result = app.invoke({"messages": [], "next": ""})
print(result["messages"])
```

---

## LangChain vs LangGraph — When to Use Which

| Scenario | Use |
|---|---|
| Single LLM call or simple prompt | LangChain chain |
| RAG / document Q&A | LangChain + retriever |
| Single agent with tools | LangChain `AgentExecutor` |
| Multi-step workflow with branching | LangGraph |
| Cycles / retry loops | LangGraph |
| Human-in-the-loop approval gates | LangGraph with checkpointer |
| Multiple cooperating agents | LangGraph multi-agent graph |
| Long-running resumable pipelines | LangGraph with persistent checkpointer |

---

## MLOps Integration Patterns

### Triggering Retraining from LangGraph

```python
import subprocess

def retrain_node(state):
    result = subprocess.run(
        ["python", "train.py", "--config", "config.yaml"],
        capture_output=True, text=True
    )
    return {"retrain_log": result.stdout}
```

### Logging to MLflow Inside a Node

```python
import mlflow

def evaluate_node(state):
    with mlflow.start_run():
        mlflow.log_metric("accuracy", state["accuracy"])
        mlflow.log_param("model_version", state["version"])
    return state
```

### Connecting to a Model Registry

```python
import mlflow.pyfunc

def load_model_node(state):
    model = mlflow.pyfunc.load_model(f"models:/{state['model_name']}/Production")
    preds = model.predict(state["data"])
    return {"predictions": preds.tolist()}
```

---

## Key Tools and Ecosystem

| Tool | Purpose |
|---|---|
| **LangSmith** | Tracing, debugging, and evaluating LangChain/LangGraph runs |
| **LangServe** | Deploy chains as REST APIs (FastAPI-based) |
| **MLflow** | Experiment tracking + model registry |
| **FAISS / Chroma / Pinecone** | Vector stores for RAG |
| **Ollama** | Local LLM inference (LangChain compatible) |
| **Tavily** | Web search tool for LangChain agents |

---

## LangSmith Tracing Setup

```bash
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=your_key
export LANGCHAIN_PROJECT=mlops-project
```

All chain and graph invocations are automatically traced in the LangSmith dashboard — invaluable for debugging agentic loops.

---

## Summary

- **LangChain** is the composable building block layer: prompts, LLMs, tools, retrievers, and chains.
- **LangGraph** is the orchestration layer: stateful graphs with branching, cycles, and human-in-the-loop support.
- Together they enable end-to-end **agentic MLOps** — from data validation to retraining decisions to automated deployment, all driven by LLM reasoning.
- Pair with **MLflow** for experiment tracking and **LangSmith** for observability.
