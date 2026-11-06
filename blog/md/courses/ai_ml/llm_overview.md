# Large Language Models (LLMs) — Overview & Comparison

## What Is an LLM?

A Large Language Model (LLM) is a deep learning model trained on massive text corpora to understand and generate human language. Built on the **Transformer architecture** (introduced in "Attention Is All You Need," 2017), LLMs predict the next token in a sequence and can be fine-tuned for tasks like coding, reasoning, summarization, and conversation.

Key specs that define an LLM:
- **Parameters** — the number of learnable weights (billions/trillions)
- **Context window** — how many tokens the model can "see" at once
- **Training tokens** — volume of data the model was trained on
- **Benchmark scores** — standardized tests measuring reasoning, coding, knowledge

---

## Major Players in the Market

| Company | Country | Notable Models |
|---|---|---|
| **OpenAI** | 🇺🇸 USA | GPT-3, GPT-4, GPT-4o, o1, o3 |
| **Google DeepMind** | 🇺🇸 USA | PaLM, Gemini 1.0/1.5/2.0, Gemma |
| **Anthropic** | 🇺🇸 USA | Claude 1/2/3/3.5/3.7 |
| **Meta AI** | 🇺🇸 USA | LLaMA 1/2/3/3.1/3.3 (open-weight) |
| **Mistral AI** | 🇫🇷 France | Mistral 7B, Mixtral 8x7B, Mistral Large |
| **xAI** | 🇺🇸 USA | Grok-1, Grok-2, Grok-3 |
| **Cohere** | 🇨🇦 Canada | Command R, Command R+ |
| **Alibaba** | 🇨🇳 China | Qwen 1/2/2.5/3 |
| **DeepSeek** | 🇨🇳 China | DeepSeek V2/V3, DeepSeek-R1 |
| **Baidu** | 🇨🇳 China | ERNIE 3.0/4.0 |
| **Microsoft** | 🇺🇸 USA | Phi-1/2/3/4 (small models) |
| **Amazon** | 🇺🇸 USA | Titan, Nova |

---

## LLM Timeline & Model Comparison

### OpenAI

| Model | Released | Parameters | Context Window | Key Highlights |
|---|---|---|---|---|
| GPT-2 | 2019 | 1.5B | 1,024 tokens | First large public LLM |
| GPT-3 | 2020 | 175B | 4,096 tokens | Breakthrough in few-shot learning |
| GPT-3.5 (ChatGPT) | Nov 2022 | ~175B | 4,096 tokens | Sparked mainstream AI adoption |
| GPT-4 | Mar 2023 | ~1.8T (MoE, est.) | 8K–32K tokens | Multimodal; best reasoning at launch |
| GPT-4o | May 2024 | Undisclosed | 128K tokens | Omni model: text, image, audio, real-time voice |
| o1 | Sep 2024 | Undisclosed | 128K tokens | Chain-of-thought reasoning; PhD-level benchmarks |
| o3 | Dec 2024 | Undisclosed | 200K tokens | Top ARC-AGI score (87.5%) |

---

### Google DeepMind

| Model | Released | Parameters | Context Window | Key Highlights |
|---|---|---|---|---|
| BERT | 2018 | 340M | 512 tokens | Bidirectional encoder; revolutionized NLP |
| PaLM | Apr 2022 | 540B | 8K tokens | 780B tokens training data |
| PaLM 2 | May 2023 | ~340B | 8K tokens | Improved reasoning and multilingual |
| Gemini 1.0 Ultra | Dec 2023 | Undisclosed | 32K tokens | First to beat GPT-4 on MMLU (90.0%) |
| Gemini 1.5 Pro | Feb 2024 | Undisclosed | **1M tokens** | Longest context window at launch |
| Gemini 2.0 Flash | Dec 2024 | Undisclosed | 1M tokens | Faster, cheaper; native multimodal |
| Gemma 3 | Mar 2025 | 1B–27B | 128K tokens | Open-weight; top small model |

---

### Anthropic

| Model | Released | Parameters | Context Window | Key Highlights |
|---|---|---|---|---|
| Claude 1 | Mar 2023 | Undisclosed | 9K tokens | Safety-focused; RLHF alignment |
| Claude 2 | Jul 2023 | Undisclosed | 100K tokens | First major 100K context window |
| Claude 3 Opus | Mar 2024 | Undisclosed | 200K tokens | Beat GPT-4 on most benchmarks at launch |
| Claude 3.5 Sonnet | Jun 2024 | Undisclosed | 200K tokens | Top coding model; best $/performance |
| Claude 3.7 Sonnet | Feb 2025 | Undisclosed | 200K tokens | Extended thinking mode; frontier reasoning |

---

### Meta AI (LLaMA — open-weight)

| Model | Released | Parameters | Context Window | Key Highlights |
|---|---|---|---|---|
| LLaMA 1 | Feb 2023 | 7B–65B | 2K tokens | First major open research LLM |
| LLaMA 2 | Jul 2023 | 7B–70B | 4K tokens | Commercial license; widely adopted |
| LLaMA 3 | Apr 2024 | 8B–70B | 8K tokens | Strong coding; beat Mistral at same size |
| LLaMA 3.1 | Jul 2024 | 8B–405B | 128K tokens | 405B competes with GPT-4 |
| LLaMA 3.3 | Dec 2024 | 70B | 128K tokens | 70B matches 405B on most tasks |

---

### Mistral AI (mostly open-weight)

| Model | Released | Parameters | Context Window | Key Highlights |
|---|---|---|---|---|
| Mistral 7B | Sep 2023 | 7B | 8K tokens | Beat LLaMA 2 13B at half the size |
| Mixtral 8x7B | Dec 2023 | 46.7B active (MoE) | 32K tokens | First major open MoE model |
| Mistral Large 2 | Jul 2024 | 123B | 128K tokens | Top European closed model |
| Codestral | May 2024 | 22B | 32K tokens | Code-specialized; 80+ languages |

---

### DeepSeek (China — open-weight)

| Model | Released | Parameters | Context Window | Key Highlights |
|---|---|---|---|---|
| DeepSeek V2 | May 2024 | 236B (21B active MoE) | 128K tokens | Ultra-low cost: $0.14/M tokens |
| DeepSeek V3 | Dec 2024 | 685B (37B active MoE) | 128K tokens | Matches GPT-4o; trained for $5.6M |
| DeepSeek-R1 | Jan 2025 | 671B (reasoning) | 128K tokens | Matches o1; fully open-weight |

---

### xAI

| Model | Released | Parameters | Context Window | Key Highlights |
|---|---|---|---|---|
| Grok-1 | Nov 2023 | 314B (MoE) | 8K tokens | Open-weight; integrated into X |
| Grok-2 | Aug 2024 | Undisclosed | 128K tokens | Multimodal; beats Claude 3 Opus |
| Grok-3 | Feb 2025 | Undisclosed | 131K tokens | Trained on 200K H100s; top reasoning |

---

### Alibaba (Qwen — open-weight)

| Model | Released | Parameters | Context Window | Key Highlights |
|---|---|---|---|---|
| Qwen 2 | Jun 2024 | 0.5B–72B | 128K tokens | Top open model on MMLU, HumanEval |
| Qwen 2.5 | Sep 2024 | 0.5B–72B | 128K tokens | Top open-source on coding and math |
| Qwen 3 | Apr 2025 | 0.6B–235B | 128K tokens | Hybrid thinking mode; MoE variant |

---

## Benchmark Performance Comparison (2024–2025)

Higher is better. Scores are approximate based on public disclosures.

| Model | MMLU (Knowledge) | HumanEval (Coding) | MATH | GPQA (PhD Science) |
|---|---|---|---|---|
| o3 (high) | **93.3%** | **95.0%** | **97.8%** | **87.7%** |
| Grok-3 | 92.0% | 88.0% | 93.0% | 84.0% |
| o1 | 92.3% | 92.4% | 94.8% | 78.3% |
| DeepSeek-R1 | 90.8% | 92.6% | 97.3% | 71.5% |
| Claude 3.7 Sonnet | 90.5% | 93.7% | 86.8% | 68.0% |
| Gemini 2.0 Flash | 89.0% | 89.0% | 82.0% | 62.1% |
| GPT-4o | 88.7% | 90.2% | 76.6% | 53.6% |
| LLaMA 3.1 405B | 88.6% | 89.0% | 73.8% | 51.1% |
| DeepSeek V3 | 88.5% | 91.6% | 84.0% | 59.1% |
| Claude 3.5 Sonnet | 88.3% | 92.0% | 71.1% | 59.4% |
| Qwen 2.5 72B | 86.0% | 86.6% | 83.1% | 49.0% |
| Mistral Large 2 | 84.0% | 92.1% | 69.0% | 45.2% |

---

## Cost Comparison (API Pricing, Approximate 2025)

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|---|---|---|
| o1 | $15.00 | $60.00 |
| Claude 3.7 Sonnet | $3.00 | $15.00 |
| Claude 3.5 Sonnet | $3.00 | $15.00 |
| GPT-4o | $2.50 | $10.00 |
| Mistral Large 2 | $2.00 | $6.00 |
| o3-mini | $1.10 | $4.40 |
| DeepSeek-R1 | $0.55 | $2.19 |
| DeepSeek V3 | $0.27 | $1.10 |
| Gemini 2.0 Flash | $0.075 | $0.30 |
| LLaMA 3.3 70B (self-hosted) | ~$0.05 | ~$0.05 |

---

## Key Trends

### Mixture of Experts (MoE)
Only a fraction of parameters activate per token — dramatically cutting compute cost while maintaining large model capacity. Used by DeepSeek, Mixtral, GPT-4 (reportedly), and Qwen 3.

### Reasoning Models
A new class using extended chain-of-thought (CoT) before answering: o1, o3, DeepSeek-R1, Claude 3.7 (extended thinking), Grok-3 Think, Qwen 3. Trade speed for accuracy on hard math, science, and coding tasks.

### Open vs. Closed Models
Open-weight models (LLaMA, DeepSeek, Qwen, Mistral) closed the quality gap from 8% to just 1.7% vs. closed models in 2024.

### Context Window Growth

| Era | Max Context |
|---|---|
| 2022 (GPT-3.5) | 4K tokens |
| 2023 (Claude 2) | 100K tokens |
| 2024 (Gemini 1.5) | 1M tokens |

### Multimodality
Most frontier models now accept text + images + audio + video: GPT-4o, Gemini 2.0, Claude 3.5/3.7, LLaMA 3.2, Qwen 2.5-VL, Grok-2.

---

## Resources

- [LMSYS Chatbot Arena](https://chat.lmsys.org/) — Live human-preference rankings
- [Open LLM Leaderboard (HuggingFace)](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) — Open model benchmarks
- [Artificial Analysis](https://artificialanalysis.ai/) — Speed, cost, quality comparisons
- [Stanford AI Index 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report) — Comprehensive AI landscape report
