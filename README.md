# 🦜🔗 LangChain Learning Repository

A complete **hands-on LangChain learning repository** covering core to advanced concepts including **LLMs, Chat Models, Prompts, Chains, Agents, Tools, RAG, Runnables (LCEL), and Structured Outputs**.  
This project is designed for **step-by-step learning**, experimentation, and building real-world GenAI applications.

---

## 📁 Project Structure

```bash
LANGCHAINS/
│
├── Agents_using_langchain/
│   └── AI_AGENT_USING_LANGCHAIN.ipynb
│
├── chains/
├── ChatModels/
├── Document_loader/
├── EmbeddedModels/
├── LLMS/
├── output_parsers/
├── Prompts/
├── RAG/
├── runnables/
├── structured_output/
├── tools_in_langchain/
│
├── venv/
├── .env
└── requirement.txt
📌 Folder Overview
🔹 Agents_using_langchain/
AI agent implementation using LangChain

Tool calling, reasoning, and action execution

Demonstrates autonomous agent workflows

🔹 LLMS/
Large Language Model integrations

Text generation and completion examples

Prompt-to-response pipelines

🔹 ChatModels/
Chat-based LLM usage

System, user, and assistant roles

Conversational AI flows

🔹 Prompts/
Prompt engineering fundamentals

Prompt templates and dynamic variables

Few-shot prompting techniques

🔹 chains/
LangChain chains

Simple chains, sequential chains, and router chains

Multi-step LLM workflows

🔹 runnables/
LangChain Expression Language (LCEL)

RunnableSequence and RunnableParallel

Streaming and composable pipelines

🔹 output_parsers/
Parsing raw LLM outputs

JSON, list, and schema-based parsing

Pydantic output parsers

🔹 structured_output/
Strongly-typed LLM responses

Schema-driven outputs

Reliable API-style responses

🔹 Document_loader/
Document ingestion for RAG

PDF, TXT, CSV, and web-based loaders

🔹 EmbeddedModels/
Text embedding models

Semantic search and similarity matching

Vectorization for RAG systems

🔹 RAG/
Retrieval Augmented Generation

Vector databases and retrievers

Document-based question answering

🔹 tools_in_langchain/
Built-in and custom LangChain tools

API integration tools

Function calling for agents

⚙️ Environment Setup
1️⃣ Create a Virtual Environment
python -m venv venv
2️⃣ Activate the Environment
Windows

venv\Scripts\activate
Linux / macOS

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirement.txt
4️⃣ Configure Environment Variables
Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key_here
You may also use Gemini or HuggingFace API keys depending on the implementation.

🧪 How to Run
Open notebooks using Jupyter Notebook or VS Code

Run files inside each folder independently

Start with:

Prompts

LLMS

ChatModels

chains

runnables

tools_in_langchain

Agents_using_langchain

RAG

🎯 Learning Outcomes
Understand LangChain architecture

Build LLM-powered pipelines

Create intelligent AI agents

Implement RAG systems

Generate structured, reliable outputs

Design production-ready GenAI workflows

🚀 Who Is This For?
Beginners learning LangChain

Data Scientists and ML Engineers

GenAI & LLM enthusiasts

Developers building chatbots, agents, and RAG applications

🔮 Future Enhancements
LangGraph integration

Streamlit / FastAPI deployment

MCP (Model Context Protocol) tool calling

Production-grade agent orchestration

