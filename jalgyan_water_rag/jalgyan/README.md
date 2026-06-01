# 💧 Jal Gyan — Water Quality RAG Chatbot

A Python/Flask RAG chatbot for Indian water quality standards.
Knowledge base: **BIS IS 10500:2012 · CPCB · EU Directive 2020/2184 · US EPA SDWA · WHO 2022**

---

## Project Structure

```
jalgyan/
├── app.py              ← Flask backend + RAG pipeline + Anthropic API
├── rag_knowledge.py    ← Knowledge base (12 chunks, keyword retrieval)
├── requirements.txt    ← Python dependencies
├── templates/
│   └── index.html      ← Frontend (chat UI, sidebar, streaming)
└── README.md
```

---

## Setup (5 minutes)

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Get your Anthropic API key
- Go to https://console.anthropic.com
- Create → API Keys → copy key

### 3. Set the API key
```bash
# Linux / macOS
export ANTHROPIC_API_KEY=sk-ant-your-key-here

# Windows (Command Prompt)
set ANTHROPIC_API_KEY=sk-ant-your-key-here

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

### 4. Run the app
```bash
python app.py
```

Open http://localhost:5000 in your browser.

---

## How the RAG Works

```
User Query
    ↓
Keyword Retrieval (rag_knowledge.py)
    ↓
Top 4 matching knowledge chunks selected
    ↓
Chunks injected into Claude's system prompt as context
    ↓
Claude generates answer citing the retrieved standards
    ↓
Streaming response sent to browser via SSE
```

No vector database needed — keyword scoring works well for this
domain-specific use case.

---

## Deploy to Production

### Option A — Render.com (free)
1. Push to GitHub
2. Go to render.com → New Web Service → Connect repo
3. Build: `pip install -r requirements.txt`
4. Start: `gunicorn app:app`
5. Add env var: `ANTHROPIC_API_KEY`

### Option B — Railway.app (free tier)
1. railway.app → Deploy from GitHub
2. Add `ANTHROPIC_API_KEY` in Variables
3. Done — auto-deploys on push

### Option C — PythonAnywhere (free)
1. Upload files to pythonanywhere.com
2. Create a web app → Flask → Python 3.12
3. Set WSGI file to point to `app.py`
4. Set `ANTHROPIC_API_KEY` in environment

### For Render/Railway — add gunicorn:
```bash
pip install gunicorn
```
Start command: `gunicorn app:app --worker-class=gthread --threads=4`

---

## Extending the Knowledge Base

To add more water quality data, edit `rag_knowledge.py`:

```python
KNOWLEDGE_CHUNKS.append({
    "id": "your_new_chunk",
    "source": "Your Source Name",
    "category": "Category description",
    "keywords": ["keyword1", "keyword2", "keyword3"],
    "content": """
Your detailed content here...
"""
})
```

For production-scale RAG with semantic search:
- Use `sentence-transformers` to embed chunks
- Store in `chromadb` or `faiss`
- Replace `retrieve_chunks()` with vector similarity search

---

## Knowledge Base Coverage

| Source | Topics |
|--------|--------|
| BIS IS 10500:2012 | Physical, chemical, heavy metals, microbiology, radioactivity |
| CPCB | River classification (A–E), effluent standards, groundwater |
| US EPA SDWA | MCLs, action levels, DBPs, surface water treatment |
| EU 2020/2184 | Parametric values including PFAS, bisphenol A, microcystins |
| WHO 2022 | Cross-reference guidelines |
| Indian Legislation | Jal Jeevan Mission, Namami Gange, Water Act 1974 |
