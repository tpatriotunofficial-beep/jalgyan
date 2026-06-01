"""
Jal Gyan - Water Quality RAG Chatbot
Flask backend with keyword-based RAG using BIS IS 10500, CPCB, EU, US EPA standards
"""

import os
import json
from flask import Flask, render_template, request, jsonify, Response, stream_with_context
from groq import Groq
from rag_knowledge import build_context, KNOWLEDGE_CHUNKS

app = Flask(__name__)

client = Groq(api_key=os.environ.get("GROQ_API_KEY", ""))

SYSTEM_PROMPT = """You are Jal Gyan (जल ज्ञान), an expert water quality assistant for India.
You have deep knowledge of:
- BIS IS 10500:2012 (Indian drinking water standards)
- CPCB river water classification and effluent standards
- EU Drinking Water Directive 2020/2184
- US EPA Safe Drinking Water Act (SDWA)
- WHO 2022 water quality guidelines

Response rules:
1. Always cite which standard you are using: [BIS IS 10500], [CPCB], [US EPA], [EU 2020], [WHO].
2. Prioritize Indian (BIS/CPCB) context - the user is in India.
3. Use specific numbers, units (mg/L, NTU, CFU/100mL, Bq/L), and parameter names.
4. For safety questions ("is X mg/L safe?"), compare against Indian BIS limits first.
5. Mention India-specific hotspots for contaminants (e.g., arsenic in Bengal, fluoride in Rajasthan).
6. Use plain, clear English. Avoid jargon where possible.
7. Format responses with markdown: use **bold** for limits, `code` for parameter names, tables where helpful.
8. If asked about a contaminant not in the provided context, say so clearly and refer to BIS IS 10500 for the full list.
9. For industrial discharge questions, always reference CPCB General Standards (Schedule VI, EPA 1986).
10. Keep responses focused and actionable - include testing recommendations where relevant.

The RAG context below contains the relevant extracted knowledge. Use it as your primary source."""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_query = data.get("message", "")
    messages = data.get("messages", [])

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    context, retrieved_chunks = build_context(user_query)
    sources = list({chunk["source"] for chunk in retrieved_chunks})
    full_system = f"{SYSTEM_PROMPT}\n\n--- RETRIEVED KNOWLEDGE BASE CONTEXT ---\n{context}\n--- END CONTEXT ---"

    def generate():
        yield f"data: {json.dumps({'type': 'sources', 'sources': sources})}\n\n"
        stream = client.chat.completions.create(
            model="llama3-8b-8192",
            max_tokens=1024,
            system=full_system,
            messages=messages,
            stream=True,
        )
        for chunk in stream:
            text = chunk.choices[0].delta.content or ""
            if text:
                yield f"data: {json.dumps({'type': 'text', 'text': text})}\n\n"
        yield "data: [DONE]\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )

@app.route("/api/knowledge", methods=["GET"])
def knowledge_stats():
    """Return stats about the knowledge base."""
    return jsonify({
        "total_chunks": len(KNOWLEDGE_CHUNKS),
        "sources": list({c["source"] for c in KNOWLEDGE_CHUNKS}),
        "categories": [c["category"] for c in KNOWLEDGE_CHUNKS],
    })

if __name__ == "__main__":
    if not os.environ.get("GROQ_API_KEY"):
        print("WARNING: GROQ_API_KEY not set.")
    print("Jal Gyan starting on http://localhost:5000")
    app.run(host="0.0.0.0", port=5000)
