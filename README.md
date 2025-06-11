Absolutely! Here's a clean, professional `README.md` for your **Scientific Paper Scout** project, explaining what it does, how to install and run it, and how to use the summarization endpoint:

---

````markdown
# 🧠 Scientific Paper Scout

Scientific Paper Scout is a local AI assistant that summarizes scientific papers (PDFs) using powerful LLMs like Groq's LLaMA 3. The project provides a FastAPI backend where you can upload a PDF and get a concise summary of the content.

---

## 🚀 Features

- 🔍 Extracts and reads content from scientific PDFs
- 🧠 Summarizes papers using LLaMA 3 via Groq API
- ⚡ FastAPI backend with interactive `/docs` UI
- 🔐 Secure and modular codebase with `.env` support

---

## 📁 Project Structure

scientific-paper-scout/
├── agent/
│ ├── main.py
│ ├── agent_host.py
│ ├── llm_provider.py
│ ├── logger.py
│ └── .env
├── mcp_servers/
│ ├── paper_search/
│ │ └── server.py
│ └── pdf_summarize/
│ └── server.py
├── shared/
│ └── utils.py
└── README.md

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/scientific_paper_scout.git
cd scientific_paper_scout
```
````

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Linux/macOS
venv\Scripts\activate           # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
LLM_PROVIDER=groq
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Server

```bash
uvicorn mcp_servers.pdf_summarize.server:app --reload
```

Visit the interactive API docs at:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🧠 LLM Support

Currently supports:

- ✅ [Groq](https://groq.com/) (LLaMA 3 via `llama3-8b-8192` model)

You can easily extend support to Anthropic, OpenAI, etc., by updating `llm_provider.py`.

---

## 📝 Example API Response

```json
{
  "summary": "This paper explores the use of deep learning methods in protein structure prediction..."
}
```

## 📜 License

MIT License – feel free to use and modify this project.

---

## ✨ Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Groq](https://groq.com/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)

```

---


```
