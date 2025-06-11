
# 🧠 Scientific Paper Scout

**Scientific Paper Scout** is a local AI assistant that summarizes scientific papers (PDFs) using powerful LLMs like Groq's LLaMA 3. It features a FastAPI backend where you can upload a PDF and get a concise, meaningful summary of its content.

---

## 🚀 Features

- 🔍 Extracts and parses scientific paper PDFs
- 🧠 Summarizes papers using Groq’s LLaMA 3 (`llama3-8b-8192`)
- ⚡ FastAPI backend with interactive Swagger UI
- 🔐 Secure, modular, and `.env`-configurable

---
```markdown

## 📁 Project Structure

scientific-paper-scout/
├── agent/
│   ├── main.py               # Entry point for agents
│   ├── agent_host.py         # Hosts the agent for orchestrating tasks
│   ├── llm_provider.py       # LLM integration logic (Groq by default)
│   ├── logger.py             # Centralized logging setup
│   └── .env                  # Environment configuration (not committed)
├── mcp_servers/
│   ├── paper_search/
│   │   └── server.py         # (Optional) Endpoint for paper search (future scope)
│   └── pdf_summarize/
│       └── server.py         # Main FastAPI server for PDF summarization
├── shared/
│   └── utils.py              # Common helper functions
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/scientific_paper_scout.git
cd scientific_paper_scout
```

### 2. Set up a virtual environment

```bash
# On Linux/macOS
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory with the following content:

```env
LLM_PROVIDER=groq
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Server

Start the PDF summarization server using:

```bash
uvicorn mcp_servers.pdf_summarize.server:app --reload
```

Then open your browser to the Swagger UI:

👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧠 LLM Support

Currently supported:

* ✅ **Groq** (`llama3-8b-8192`)

> You can easily extend support to other providers like OpenAI or Anthropic by modifying `agent/llm_provider.py`.

---

## 📝 Example API Response

```json
{
  "summary": "This paper explores the use of deep learning methods in protein structure prediction..."
}
```

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use, modify, and distribute it.

---

## ✨ Acknowledgements

* [FastAPI](https://fastapi.tiangolo.com/)
* [Groq](https://groq.com/)
* [PyMuPDF](https://pymupdf.readthedocs.io/)
```

