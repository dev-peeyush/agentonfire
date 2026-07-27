# 🔥 Agent on Fire

> Build production-ready AI Agents with FastAPI, LangGraph, MCP, and modern Python.

Agent on Fire is an open-source framework for building scalable AI agent applications. It provides a clean architecture for developing LLM-powered agents with authentication, memory, tools, databases, and APIs, while remaining modular and easy to extend.

---

## ✨ Features

- 🚀 FastAPI backend
- 🤖 AI Agents powered by LangGraph
- 🧠 Support for multiple LLM providers
  - OpenAI
  - Anthropic (planned)
  - Ollama (planned)
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

- [x] FastAPI foundation
- [x] JWT Authentication
- [ ] PostgreSQL
- [ ] LangGraph Integration
- [ ] Memory
- [ ] MCP Support
- [ ] RAG
- [ ] Docker
- [ ] Kubernetes
- [ ] CI/CD

---

## Contributing

Contributions are welcome.

If you'd like to contribute, please open an issue or submit a pull request.

---

## License

MIT License
