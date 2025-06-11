from fastapi import FastAPI, Request
import uvicorn
import requests
import fitz  # PyMuPDF
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../agent')))

from llm_provider import LLMWrapper


app = FastAPI()

@app.post("/summarize")
async def summarize_pdf(request: Request):
    data = await request.json()
    url = data.get("pdf_url")
    response = requests.get(url)
    with open("temp.pdf", "wb") as f:
        f.write(response.content)

    doc = fitz.open("temp.pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    llm = LLMWrapper()
    summary = llm.summarize(text[:3000])  # limit to 3K chars
    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
