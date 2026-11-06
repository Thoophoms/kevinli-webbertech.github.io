# AutoGen (Microsoft) in MLOps

## Overview

AutoGen is an open-source multi-agent framework developed by Microsoft Research. It enables developers to build **conversational multi-agent systems** where agents collaborate, debate, and delegate tasks to solve complex problems. In MLOps contexts, AutoGen agents can orchestrate training pipelines, automate code generation, review outputs, and coordinate data workflows — all through structured agent conversations.

---

## Core Concepts

| Concept | Description |
|---|---|
| **ConversableAgent** | Base class for all agents; can send and receive messages |
| **AssistantAgent** | LLM-backed agent that generates responses and code |
| **UserProxyAgent** | Executes code locally and proxies human input |
| **GroupChat** | Multi-agent round-robin or selector-driven conversation |
| **GroupChatManager** | Orchestrates which agent speaks next in a group chat |
| **ReplyFunction** | Custom function to override agent reply behavior |
| **CodeExecutor** | Sandboxed environment for running generated code |

---

## Installation

```bash
pip install pyautogen
# For Docker-based code execution (recommended for production):
pip install pyautogen[docker]
# For local code execution:
pip install pyautogen[local]
```

---

## Two-Agent Conversation (Assistant + UserProxy)

The simplest AutoGen pattern: an AssistantAgent generates code and a UserProxyAgent executes it.

```python
import autogen

config_list = [{"model": "gpt-4o-mini", "api_key": "YOUR_KEY"}]

llm_config = {"config_list": config_list, "temperature": 0}

assistant = autogen.AssistantAgent(
    name="MLOps_Assistant",
    llm_config=llm_config,
    system_message=(
        "You are an MLOps expert. Write clean Python code to solve ML tasks. "
        "Always wrap code in ```python blocks."
    )
)

user_proxy = autogen.UserProxyAgent(
    name="User_Proxy",
    human_input_mode="NEVER",        # fully automated
    max_consecutive_auto_reply=5,
    code_execution_config={"work_dir": "mlops_workspace", "use_docker": False},
    is_termination_msg=lambda msg: "TERMINATE" in msg.get("content", "")
)

user_proxy.initiate_chat(
    assistant,
    message="Train a scikit-learn RandomForest on the iris dataset and report accuracy."
)
```

---

## Multi-Agent Group Chat

Group chats allow multiple specialized agents to collaborate on a single task.

```python
import autogen

config_list = [{"model": "gpt-4o-mini", "api_key": "YOUR_KEY"}]
llm_config = {"config_list": config_list}

# Specialized agents
data_engineer = autogen.AssistantAgent(
    name="Data_Engineer",
    llm_config=llm_config,
    system_message="You handle data loading, cleaning, and feature engineering."
)

model_trainer = autogen.AssistantAgent(
    name="Model_Trainer",
    llm_config=llm_config,
    system_message="You train and tune ML models. Use scikit-learn or PyTorch."
)

reviewer = autogen.AssistantAgent(
    name="Code_Reviewer",
    llm_config=llm_config,
    system_message="You review code for correctness, efficiency, and MLOps best practices."
)

user_proxy = autogen.UserProxyAgent(
    name="Orchestrator",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    code_execution_config={"work_dir": "workspace", "use_docker": False},
    is_termination_msg=lambda msg: "TERMINATE" in msg.get("content", "")
)

group_chat = autogen.GroupChat(
    agents=[user_proxy, data_engineer, model_trainer, reviewer],
    messages=[],
    max_round=12
)

manager = autogen.GroupChatManager(groupchat=group_chat, llm_config=llm_config)

user_proxy.initiate_chat(
    manager,
    message=(
        "Build an end-to-end ML pipeline: load the wine dataset, "
        "train a GradientBoosting classifier, evaluate it, and log results."
    )
)
```

---

## Custom Agent with ReplyFunction

Override how an agent responds to build a specialized MLOps monitoring agent:

```python
import autogen
import mlflow

def monitoring_reply(recipient, messages, sender, config):
    """Fetch latest model metrics and inject them into the conversation."""
    client = mlflow.tracking.MlflowClient()
    runs = client.search_runs(experiment_ids=["1"], max_results=1,
                               order_by=["start_time DESC"])
    if runs:
        metrics = runs[0].data.metrics
        report = "\n".join(f"{k}: {v:.4f}" for k, v in metrics.items())
        return True, f"Latest model metrics:\n{report}"
    return True, "No runs found in MLflow."

monitor_agent = autogen.ConversableAgent(
    name="Model_Monitor",
    human_input_mode="NEVER",
    llm_config=False  # no LLM — pure function-based
)
monitor_agent.register_reply(
    trigger=autogen.ConversableAgent,
    reply_func=monitoring_reply
)
```

---

## AutoGen with Local Code Execution (Safe Sandbox)

For production MLOps pipelines, use Docker-isolated execution:

```python
from autogen.coding import DockerCommandLineCodeExecutor
import autogen

executor = DockerCommandLineCodeExecutor(
    image="python:3.11-slim",
    timeout=60,
    work_dir="./mlops_sandbox"
)

code_exec_agent = autogen.ConversableAgent(
    name="Code_Executor",
    llm_config=False,
    code_execution_config={"executor": executor},
    human_input_mode="NEVER"
)

assistant = autogen.AssistantAgent(
    name="ML_Assistant",
    llm_config={"config_list": [{"model": "gpt-4o-mini", "api_key": "YOUR_KEY"}]}
)

code_exec_agent.initiate_chat(
    assistant,
    message="Write and run a Python script that trains a linear regression model on synthetic data."
)
```

---

## Human-in-the-Loop Mode

Set `human_input_mode="ALWAYS"` or `"TERMINATE"` for approval gates:

```python
user_proxy = autogen.UserProxyAgent(
    name="MLOps_Lead",
    human_input_mode="TERMINATE",   # human is asked only when agent wants to terminate
    max_consecutive_auto_reply=8,
    code_execution_config={"work_dir": "workspace", "use_docker": False}
)
```

| Mode | Behavior |
|---|---|
| `NEVER` | Fully automated; no human input |
| `TERMINATE` | Human is asked when agent sends termination signal |
| `ALWAYS` | Human is prompted after every agent message |

---

## MLOps Workflow Patterns with AutoGen

### Automated Retraining Trigger

```python
import autogen
import subprocess

def retrain_reply(recipient, messages, sender, config):
    result = subprocess.run(
        ["python", "retrain.py", "--model", "fraud_detection"],
        capture_output=True, text=True, timeout=300
    )
    return True, f"Retraining output:\n{result.stdout}\n{result.stderr}"

retrain_agent = autogen.ConversableAgent(
    name="Retrain_Agent",
    llm_config=False,
    human_input_mode="NEVER"
)
retrain_agent.register_reply(
    trigger=autogen.ConversableAgent,
    reply_func=retrain_reply
)
```

### Model Evaluation Agent

```python
def evaluate_model(model_name: str, threshold: float = 0.90) -> dict:
    """Evaluate a registered model version against a performance threshold."""
    client = mlflow.tracking.MlflowClient()
    model_version = client.get_latest_versions(model_name, stages=["Staging"])[0]
    run = client.get_run(model_version.run_id)
    accuracy = run.data.metrics.get("accuracy", 0)
    return {
        "model": model_name,
        "version": model_version.version,
        "accuracy": accuracy,
        "passes_threshold": accuracy >= threshold
    }
```

---

## AutoGen vs LangGraph — Key Differences

| Dimension | AutoGen | LangGraph |
|---|---|---|
| **Paradigm** | Conversational multi-agent chat | Stateful graph with explicit nodes/edges |
| **Orchestration** | Agents negotiate via message passing | Developer-defined graph topology |
| **Code execution** | Built-in (local or Docker) | Manual (add as a node) |
| **Human-in-the-loop** | `human_input_mode` flag | Interrupt + checkpointer |
| **Observability** | AutoGen Studio dashboard | LangSmith tracing |
| **Best for** | Open-ended coding/analysis tasks | Structured deterministic pipelines |

---

## AutoGen Studio (No-Code Interface)

AutoGen Studio is a web UI for prototyping multi-agent workflows without writing code:

```bash
pip install autogenstudio
autogenstudio ui --port 8081
```

Open `http://localhost:8081` to visually build agent teams, set system prompts, and run conversations.

---

## Summary

- **AutoGen** is Microsoft's framework for building **conversational multi-agent** systems where LLM-backed agents collaborate through message exchange.
- The **AssistantAgent + UserProxyAgent** duo covers most use cases: one generates code, the other executes it.
- **GroupChat** enables specialized agents (data engineer, trainer, reviewer) to work together on complex MLOps tasks.
- Built-in **code execution** (local or Docker) makes AutoGen ideal for agentic pipelines that generate and run code autonomously.
- Use `human_input_mode` to add approval gates at any point in the workflow.
- Pair with **MLflow** for experiment tracking and **AutoGen Studio** for visual prototyping.
