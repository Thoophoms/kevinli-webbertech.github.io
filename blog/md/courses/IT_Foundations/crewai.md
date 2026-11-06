# CrewAI

## Overview

CrewAI is an open-source Python framework released in **2023** that structures AI agents as a **crew of collaborating workers**. Each agent has a defined **role**, **goal**, and **backstory**, and is assigned specific **tasks** within a coordinated workflow. Inspired by how human teams operate, CrewAI is built for workflow automation, research pipelines, and content generation.

- **Website:** [https://www.crewai.com](https://www.crewai.com)
- **GitHub:** [https://github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
- **Docs:** [https://docs.crewai.com](https://docs.crewai.com)

CrewAI is built for:
- **Role-based agent design** — agents are specialists (Researcher, Writer, Analyst, etc.)
- **Sequential and parallel workflows** — tasks run in order or concurrently
- **Tool assignment** — each agent gets exactly the tools it needs
- **Delegation** — agents can hand off sub-tasks to teammates
- **Memory and caching** — agents remember context within and across runs

---

## Core Concepts

| Concept | Description |
|---|---|
| `Agent` | An AI worker with a role, goal, backstory, and optional tools |
| `Task` | A specific piece of work assigned to an agent with expected output |
| `Crew` | A group of agents working together on a set of tasks |
| `Process` | Execution strategy: `sequential` (default) or `hierarchical` (manager delegates) |
| `Tool` | A function an agent can call — built-in tools or custom ones |

---

## Installation

```bash
pip install crewai crewai-tools
```

---

## Research & Writing Crew Example

```python
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()  # Requires SERPER_API_KEY env var

# --- Define Agents ---
researcher = Agent(
    role="Senior Research Analyst",
    goal="Find comprehensive and accurate information on the assigned topic",
    backstory="You are an expert researcher with 10 years of experience in technology journalism.",
    tools=[search_tool],
    verbose=True,
    llm="gpt-4o",        # Uses OPENAI_API_KEY from environment
)

writer = Agent(
    role="Content Writer",
    goal="Write engaging, well-structured articles based on research findings",
    backstory="You are a skilled tech writer who translates complex topics into readable content.",
    verbose=True,
    llm="gpt-4o",
)

editor = Agent(
    role="Editor",
    goal="Polish content for grammar, clarity, and style",
    backstory="You are a detail-oriented editor who ensures publication-quality output.",
    verbose=True,
    llm="gpt-4o",
)

# --- Define Tasks ---
research_task = Task(
    description="Research the current state of AI agents in 2025. Cover key frameworks, use cases, and trends.",
    expected_output="A detailed research report with key facts, statistics, and insights.",
    agent=researcher
)

writing_task = Task(
    description="Write a 600-word blog post based on the research report.",
    expected_output="A well-structured blog post with introduction, body, and conclusion.",
    agent=writer,
    context=[research_task]   # Receives output from research_task
)

editing_task = Task(
    description="Edit the blog post for grammar, readability, and flow.",
    expected_output="A polished, publication-ready blog post.",
    agent=editor,
    context=[writing_task]
)

# --- Assemble and Run Crew ---
crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()
print(result.raw)
```

---

## Hierarchical Process (Manager Pattern)

In hierarchical mode, a manager LLM automatically delegates tasks to the most appropriate agent:

```python
from crewai import Crew, Process

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task],
    process=Process.hierarchical,
    manager_llm="gpt-4o",
    verbose=True
)

result = crew.kickoff()
```

---

## Custom Tools

```python
import os
from crewai.tools import BaseTool
from openai import OpenAI

class SummarizeTool(BaseTool):
    name: str = "summarize_text"
    description: str = "Summarizes a long piece of text into bullet points."

    def _run(self, text: str) -> str:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Summarize the following text as bullet points."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content

summarize_tool = SummarizeTool()
```

---

## Dynamic Inputs at Runtime

Pass runtime variables to tasks using `kickoff(inputs={...})`:

```python
result = crew.kickoff(inputs={
    "topic": "AI agents in healthcare",
    "target_length": "800 words"
})
```

Reference inputs in task descriptions using `{variable_name}` syntax:

```python
research_task = Task(
    description="Research {topic} in depth. Target audience: professionals. Length: {target_length}.",
    expected_output="A comprehensive research brief.",
    agent=researcher
)
```

---

## Framework Comparison

| Feature | LangChain | LangGraph | AutoGen | CrewAI |
|---|---|---|---|---|
| Primary Abstraction | Chains / Runnables | Graphs / Nodes | Conversational Agents | Role-based Crews |
| Multi-agent | Limited | ✅ Native | ✅ Native | ✅ Native |
| State management | Manual | ✅ Typed state | Message history | Task context |
| Human-in-the-loop | Workaround | ✅ First-class | ✅ `human_input_mode` | ✅ Human agent |
| Code execution | Via tools | Via tools | ✅ Built-in sandbox | Via tools |
| Learning curve | Medium | High | Medium | Low |
| Best for | RAG, pipelines | Complex stateful agents | Code generation, debate | Workflow automation |

---

## Summary

- **CrewAI** frames multi-agent collaboration as a **crew of role-playing specialists**, making it the most intuitive framework for workflow-style automation.
- **Sequential process** is ideal for ordered pipelines (research → write → edit); **hierarchical process** adds a manager that dynamically delegates.
- **Tools** can be built-in (web search, file reading) or custom `BaseTool` subclasses.
- **Dynamic inputs** via `kickoff(inputs={...})` make crews reusable across different topics, datasets, and requirements.
- Lower learning curve than LangGraph; better suited to structured role-based workflows than AutoGen's open-ended chat model.
