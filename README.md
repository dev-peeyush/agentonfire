# 🔥 Agent on Fire

> Build production-ready AI Agents with FastAPI, LangChain, LangGraph, MCP, and modern Python.

Agent on Fire is an open-source framework for building scalable AI agent applications. It provides a clean architecture for developing LLM-powered agents with authentication, memory, tools, databases, and APIs, while remaining modular and easy to extend.

---

## ✨ Features

- 🚀 FastAPI backend
- 🤖 AI Agents powered by LangChain, LangGraph
- 🧠 Support for multiple LLM providers
  - OpenAI
  - Anthropic (planned)
  - Ollama (planned)
- 🎙️ Voice AI
  - Speech-to-Text(Whisper)
  - Streaming Text-to-Speech (Kokoro, Kokoro-mlx)
- 📚 Retrieval-Augmented Generation (RAG)
- 🔍 FAISS Vector Database
- 📄 PDF Knowledge Base Ingestion
- 🧩 Modular Service-Oriented Architecture
- 🔌 MCP (Model Context Protocol) support
- 💾 LangGraph Checkpointers
  - PostgreSQL
  - Redis
- 🔐 JWT Authentication
- 🗄️ PostgreSQL + SQLAlchemy
- 🧩 Modular architecture
- 🔌 MCP (Model Context Protocol) support
- 🐳 Docker support (coming soon)
- 📚 OpenAPI / Swagger documentation

---

## Project Structure

```text
app/
├── api/
├── ai/
│   ├── agent/
│   ├── model/
│   └── tools/
├── core/
├── db/
├── models/
├── services/
└── main.py
```

---

## Getting Started

### Clone

```bash
git clone https://github.com/<username>/agentonfire.git
cd agentonfire
```

### Install dependencies

```bash
uv sync
```

### Run

```bash
uv run python main.py
```

or

```bash
uv run uvicorn app.main:app --reload
```

---

## Roadmap

### Core Platform

- [x] FastAPI Foundation
- [x] JWT Authentication
- [x] PostgreSQL
- [x] SQLAlchemy
- [x] OpenAPI / Swagger

### AI Agent

- [x] LangChain Integration
- [x] LangGraph Integration
- [x] PostgreSQL Checkpointer
- [x] Redis Checkpointer
- [x] Memory Persistence

### Retrieval-Augmented Generation

- [x] PDF Loader
- [x] Recursive Text Chunking
- [x] OpenAI Embeddings
- [x] FAISS Vector Store
- [x] Document Ingestion Pipeline
- [ ] Multiple Vector Databases

### Voice AI

- [x] Streaming Text-to-Speech(Kokoro)
- [x] Speech-to-Text
- [ ] Real-time Voice Conversations(Speech-to-Speech)

### Future

- [ ] MCP Support
- [ ] Multi-Agent Support
- [ ] Docker
- [ ] Kubernetes
- [ ] CI/CD
- [ ] Observability

---

## Contributing

Contributions are welcome.

If you'd like to contribute, please open an issue or submit a pull request.

---

## License

MIT License
