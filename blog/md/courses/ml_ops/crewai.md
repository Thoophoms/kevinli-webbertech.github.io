# CrewAI in MLOps

## Overview

CrewAI is an open-source Python framework for orchestrating **role-playing autonomous AI agents**. Each agent is assigned a specific role, goal, and backstory, and agents collaborate as a **crew** to complete multi-step tasks. In MLOps, CrewAI crews can automate research, pipeline design, model documentation, code review, and deployment decision-making — with each agent acting as a specialized team member.

---

## Core Concepts

| Concept | Description |
|---|---|
| **Agent** | An autonomous entity with a role, goal, backstory, and optional tools |
| **Task** | A discrete unit of work assigned to an agent with a description and expected output |
| **Crew** | A collection of agents working together on a set of tasks |
| **Process** | Execution strategy — `sequential` (default) or `hierarchical` |
| **Tool** | A function or API the agent can call to gather information or take action |
| **Manager Agent** | In hierarchical mode, a supervisor agent that delegates tasks to others |
| **Memory** | Short-term and long-term memory for agents to retain context across tasks |

---

## Installation

```bash
pip install crewai crewai-tools
# Optional: for local LLM support
pip install crewai[ollama]
```

---

## Minimal Crew Example

```python
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Define agents
data_analyst = Agent(
    role="Data Analyst",
    goal="Analyze ML model performance metrics and identify issues",
    backstory=(
        "You are a senior data analyst at an MLOps team. "
        "You specialize in spotting data drift, class imbalance, and model degradation."
    ),
    llm=llm,
    verbose=True
)

report_writer = Agent(
    role="Technical Writer",
    goal="Write clear, concise MLOps status reports based on analysis findings",
    backstory=(
        "You are a technical writer who translates complex ML metrics "
        "into actionable summaries for engineering and product teams."
    ),
    llm=llm,
    verbose=True
)

# Define tasks
analyze_task = Task(
    description=(
        "Review the following model metrics and identify any performance concerns:\n"
        "accuracy: 0.81, precision: 0.78, recall: 0.69, F1: 0.73, "
        "baseline_accuracy: 0.90. Flag any degradation."
    ),
    expected_output="A bullet-point analysis of model performance issues.",
    agent=data_analyst
)

report_task = Task(
    description=(
        "Using the analysis provided, write a short MLOps status report "
        "with a recommended action (monitor / retrain / rollback)."
    ),
    expected_output="A 200-word executive summary with a recommended action.",
    agent=report_writer
)

# Assemble crew
crew = Crew(
    agents=[data_analyst, report_writer],
    tasks=[analyze_task, report_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()
print(result)
```

---

## Adding Tools to Agents

Tools let agents fetch real data, search the web, or call APIs.

```python
from crewai import Agent, Task, Crew
from crewai_tools import tool
from langchain_openai import ChatOpenAI
import mlflow

@tool("Get MLflow Metrics")
def get_mlflow_metrics(experiment_name: str) -> str:
    """Fetch the latest run metrics from an MLflow experiment."""
    client = mlflow.tracking.MlflowClient()
    experiment = client.get_experiment_by_name(experiment_name)
    if not experiment:
        return f"Experiment '{experiment_name}' not found."
    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id],
        max_results=1,
        order_by=["start_time DESC"]
    )
    if not runs:
        return "No runs found."
    metrics = runs[0].data.metrics
    return "\n".join(f"{k}: {v:.4f}" for k, v in metrics.items())

llm = ChatOpenAI(model="gpt-4o-mini")

monitor_agent = Agent(
    role="Model Monitor",
    goal="Retrieve and interpret the latest model metrics from MLflow",
    backstory="You are an ML engineer responsible for production model health monitoring.",
    tools=[get_mlflow_metrics],
    llm=llm,
    verbose=True
)

monitor_task = Task(
    description="Fetch metrics for the experiment named 'fraud_detection_v2' and summarize findings.",
    expected_output="A summary of key metrics with pass/fail assessment against production thresholds.",
    agent=monitor_agent
)

crew = Crew(agents=[monitor_agent], tasks=[monitor_task])
print(crew.kickoff())
```

---

## Hierarchical Process (Manager + Workers)

In hierarchical mode, a manager agent delegates tasks to worker agents:

```python
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

# Manager
mlops_lead = Agent(
    role="MLOps Lead",
    goal="Coordinate the ML deployment process by delegating to specialists",
    backstory="You are the MLOps team lead. You delegate to engineers and review outputs.",
    llm=llm,
    allow_delegation=True
)

# Workers
infra_engineer = Agent(
    role="Infrastructure Engineer",
    goal="Provision and configure model serving infrastructure",
    backstory="You manage Kubernetes, Docker, and cloud deployments for ML models.",
    llm=llm
)

security_engineer = Agent(
    role="Security Engineer",
    goal="Audit the ML deployment for vulnerabilities and compliance issues",
    backstory="You specialize in ML supply chain security and model serving hardening.",
    llm=llm
)

deployment_task = Task(
    description=(
        "Plan and execute the deployment of model version 3.2.1 of the recommendation engine. "
        "Ensure infrastructure is ready and security is reviewed before go-live."
    ),
    expected_output="A deployment checklist with infrastructure and security sign-offs.",
    agent=mlops_lead
)

crew = Crew(
    agents=[mlops_lead, infra_engineer, security_engineer],
    tasks=[deployment_task],
    process=Process.hierarchical,
    manager_llm=llm,
    verbose=True
)

print(crew.kickoff())
```

---

## Memory and Context Retention

CrewAI supports short-term, long-term, and entity memory:

```python
from crewai import Crew, Agent, Task, Process
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

agent = Agent(
    role="ML Research Assistant",
    goal="Track and summarize ML research findings across multiple sessions",
    backstory="You are a research assistant who remembers prior discussions and builds on them.",
    llm=llm,
    memory=True   # enables short-term memory within the crew run
)

task = Task(
    description="Summarize the key advantages of transformer-based models for tabular data.",
    expected_output="A concise summary referencing prior context if available.",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    memory=True,         # enables crew-level memory (short-term + long-term)
    verbose=True
)

print(crew.kickoff())
```

---

## Dynamic Kickoff with Inputs

Pass runtime variables to tasks using `kickoff(inputs={...})`:

```python
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

analyst = Agent(
    role="MLOps Analyst",
    goal="Evaluate model performance for the given model and version",
    backstory="You are an MLOps analyst who performs model health checks on demand.",
    llm=llm
)

task = Task(
    description=(
        "Evaluate model '{model_name}' version '{version}'. "
        "Check accuracy, latency, and drift status. Provide a go/no-go recommendation."
    ),
    expected_output="A go/no-go recommendation with supporting metrics.",
    agent=analyst
)

crew = Crew(agents=[analyst], tasks=[task])

result = crew.kickoff(inputs={
    "model_name": "churn_predictor",
    "version": "v4.1"
})
print(result)
```

---

## MLOps Crew Patterns

### End-to-End Pipeline Review Crew

```python
agents = [
    Agent(role="Data Quality Auditor", goal="Detect data issues in the training set", ...),
    Agent(role="Model Trainer", goal="Train and tune the ML model", ...),
    Agent(role="Evaluator", goal="Measure model performance against baselines", ...),
    Agent(role="Deployment Approver", goal="Approve or reject model for production", ...)
]

tasks = [
    Task(description="Audit the dataset for missing values, drift, and label noise.", agent=agents[0], ...),
    Task(description="Train a XGBoost model on the audited dataset.", agent=agents[1], ...),
    Task(description="Evaluate the trained model. Compare against production baseline.", agent=agents[2], ...),
    Task(description="Review evaluation results. Approve or reject deployment.", agent=agents[3], ...)
]

crew = Crew(agents=agents, tasks=tasks, process=Process.sequential)
crew.kickoff()
```

### Research Crew for Model Selection

```python
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

researcher = Agent(
    role="ML Researcher",
    goal="Find the best model architecture for time-series anomaly detection in 2025",
    backstory="You research and synthesize the latest ML papers and benchmarks.",
    tools=[search_tool],
    llm=llm
)

summarizer = Agent(
    role="Decision Maker",
    goal="Recommend a model architecture based on the research",
    backstory="You make practical model selection decisions based on research summaries.",
    llm=llm
)
```

---

## CrewAI vs AutoGen vs LangGraph

| Dimension | CrewAI | AutoGen | LangGraph |
|---|---|---|---|
| **Paradigm** | Role-playing agent crew | Conversational multi-agent chat | Stateful directed graph |
| **Orchestration** | Sequential or hierarchical process | Round-robin / selector group chat | Developer-defined nodes and edges |
| **Agent definition** | Role + goal + backstory | System message + reply functions | Python functions as nodes |
| **Code execution** | Via tools | Built-in UserProxyAgent | Manual (add as node) |
| **Human-in-the-loop** | Callbacks / manual review | `human_input_mode` flag | Interrupt + checkpointer |
| **Best for** | Team-style role delegation | Open-ended coding tasks | Structured deterministic pipelines |
| **Observability** | CrewAI traces + LangSmith | AutoGen Studio | LangSmith tracing |

---

## Observability and Tracing

CrewAI integrates with LangSmith out of the box:

```bash
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=your_key
export LANGCHAIN_PROJECT=crewai-mlops
```

All agent actions, tool calls, and LLM requests are traced automatically.

---

## Summary

- **CrewAI** frames multi-agent collaboration as a **crew of role-playing specialists** — each with a unique role, goal, and backstory.
- Use **sequential process** for ordered pipelines (data → train → evaluate → deploy) and **hierarchical process** for manager-delegated workflows.
- **Tools** extend agents with real-world capabilities: MLflow queries, web search, file I/O, and custom APIs.
- **Memory** enables agents to retain context across tasks within a run.
- **Dynamic inputs** via `kickoff(inputs={...})` make crews reusable across different models, datasets, and environments.
- Pair with **MLflow** for experiment tracking and **LangSmith** for full observability of agent reasoning chains.
