# OpenAI Agents SDK

## Overview

The OpenAI Agents SDK is a lightweight, first-party Python library released by OpenAI in **2025** for building agentic applications powered by OpenAI models. It provides minimal, low-ceremony primitives — agents, tools, handoffs, and a runner — that make it easy to go from zero to a working agent with very little boilerplate.

- **Website:** [https://openai.github.io/openai-agents-python](https://openai.github.io/openai-agents-python/)
- **GitHub:** [https://github.com/openai/openai-agents-python](https://github.com/openai/openai-agents-python)
- **Docs:** [https://openai.github.io/openai-agents-python/docs](https://openai.github.io/openai-agents-python/docs)

Design philosophy:
- **Minimal surface area** — few abstractions, close to the raw API
- **First-party support** — built and maintained by OpenAI for their own models
- **Tool calling by decorator** — define tools with `@function_tool`
- **Agent handoffs** — agents can transfer control to other agents
- **Tracing built-in** — automatic run traces visible in the OpenAI dashboard

---

## Installation

```bash
pip install openai-agents
```

Set your API key:

```bash
export OPENAI_API_KEY=your_key_here
```

---

## Minimal Agent Example

```python
from agents import Agent, Runner, function_tool

@function_tool
def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"The weather in {city} is sunny and 72°F."

agent = Agent(
    name="WeatherBot",
    instructions="Answer weather questions using the get_weather tool.",
    tools=[get_weather]
)

result = Runner.run_sync(agent, "What's the weather in New York?")
print(result.final_output)
```

---

## Multi-Tool Agent

```python
import os
from agents import Agent, Runner, function_tool

@function_tool
def search_web(query: str) -> str:
    """Search the web for information."""
    # Replace with real search API (e.g., Tavily, Serper)
    return f"Top results for '{query}': [Result 1], [Result 2]"

@function_tool
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression safely."""
    try:
        # Only allow simple arithmetic
        allowed = set("0123456789+-*/(). ")
        if not all(c in allowed for c in expression):
            return "Invalid expression."
        return str(eval(expression))  # noqa: S307
    except Exception as e:
        return f"Error: {e}"

agent = Agent(
    name="ResearchAssistant",
    instructions=(
        "You are a helpful research assistant. "
        "Use the search tool to find information and the calculator for math."
    ),
    tools=[search_web, calculate],
    model="gpt-4o"
)

result = Runner.run_sync(agent, "What is 15% of 847, and who invented Python?")
print(result.final_output)
```

---

## Agent Handoffs

Agents can hand off control to specialized sub-agents:

```python
from agents import Agent, Runner

# Specialized agents
billing_agent = Agent(
    name="BillingAgent",
    instructions="Handle billing questions, refunds, and subscription changes.",
    model="gpt-4o-mini"
)

tech_support_agent = Agent(
    name="TechSupportAgent",
    instructions="Handle technical issues, bugs, and how-to questions.",
    model="gpt-4o-mini"
)

# Triage agent that routes to the right specialist
triage_agent = Agent(
    name="TriageAgent",
    instructions=(
        "You are a customer service triage agent. "
        "Route billing questions to BillingAgent and technical questions to TechSupportAgent."
    ),
    handoffs=[billing_agent, tech_support_agent],
    model="gpt-4o"
)

result = Runner.run_sync(triage_agent, "My invoice shows the wrong amount.")
print(result.final_output)
```

---

## Async Streaming

For real-time output streaming:

```python
import asyncio
from agents import Agent, Runner

agent = Agent(
    name="Storyteller",
    instructions="You are a creative storyteller.",
    model="gpt-4o"
)

async def main():
    async with Runner.run_streamed(agent, "Tell me a short story about a robot.") as stream:
        async for event in stream:
            if hasattr(event, "delta") and event.delta:
                print(event.delta, end="", flush=True)
    print()

asyncio.run(main())
```

---

## Guardrails

Add input and output guardrails to validate agent behavior:

```python
from agents import Agent, Runner, GuardrailFunctionOutput, input_guardrail
from pydantic import BaseModel

class SafetyCheck(BaseModel):
    is_safe: bool
    reason: str

@input_guardrail
async def check_input(ctx, agent, input_text):
    # Simple keyword check — replace with LLM-based classifier for production
    blocked_words = ["hack", "exploit", "bypass"]
    for word in blocked_words:
        if word in input_text.lower():
            return GuardrailFunctionOutput(
                output_info=SafetyCheck(is_safe=False, reason=f"Blocked keyword: {word}"),
                tripwire_triggered=True
            )
    return GuardrailFunctionOutput(
        output_info=SafetyCheck(is_safe=True, reason="Input passed safety check"),
        tripwire_triggered=False
    )

safe_agent = Agent(
    name="SafeAgent",
    instructions="Answer general knowledge questions.",
    input_guardrails=[check_input],
    model="gpt-4o-mini"
)
```

---

## Built-in Tracing

Every agent run is automatically traced and visible in the **OpenAI Dashboard** under the Traces section — no additional setup required. Traces show:
- The agent's reasoning steps
- Tool calls and their inputs/outputs
- Handoffs between agents
- Token usage per step

Disable tracing if needed:

```python
from agents import RunConfig

result = Runner.run_sync(
    agent,
    "Hello",
    run_config=RunConfig(tracing_disabled=True)
)
```

---

## OpenAI Agents SDK vs Other Frameworks

| Dimension | OpenAI Agents SDK | LangGraph | AutoGen | CrewAI |
|---|---|---|---|---|
| **Maintained by** | OpenAI | LangChain AI | Microsoft | CrewAI Inc. |
| **Released** | 2025 | 2024 | 2023 | 2023 |
| **Abstraction level** | Low (minimal) | Medium | Medium | Low-Medium |
| **Multi-agent** | Via handoffs | ✅ Native graph | ✅ GroupChat | ✅ Crew |
| **Code execution** | Via tools | Via tools | ✅ Built-in | Via tools |
| **State management** | Minimal | ✅ Typed state | Message history | Task context |
| **Tracing** | ✅ Built-in (OpenAI) | LangSmith | AutoGen Studio | LangSmith |
| **Model support** | OpenAI only | Any | Any | Any |
| **Best for** | OpenAI-native apps, rapid prototyping | Complex stateful agents | Code-gen, debate | Workflow automation |

---

## Summary

- The **OpenAI Agents SDK** is the fastest path from idea to working agent if you are using OpenAI models — minimal boilerplate, built-in tracing, and a decorator-based tool system.
- Use `@function_tool` to expose Python functions as agent tools.
- **Handoffs** enable routing between specialized agents without building an explicit orchestration graph.
- **Guardrails** provide a structured way to validate inputs and outputs before and after LLM calls.
- **Tracing** is automatic and visible in the OpenAI Dashboard — no LangSmith or external tool required.
- The main limitation: it is **OpenAI-model-only**, unlike LangChain, LangGraph, AutoGen, and CrewAI which are model-agnostic.
