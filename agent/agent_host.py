import json
import time
from llm_provider import LLMWrapper
from logger import log_tool_call
import requests

def run_agent(user_input):
    log_tool_call("paper_search", {"query": user_input, "max_results": 3})
    papers = requests.post("http://localhost:8001/search", json={
        "query": user_input, "max_results": 3
    }).json()
    
    summaries = []
    llm = LLMWrapper()

    for paper in papers:
        pdf_url = paper["pdf_url"]
        log_tool_call("pdf_summarize", {"pdf_url": pdf_url})
        response = requests.post("http://localhost:8002/summarize", json={
            "pdf_url": pdf_url
        })
        summary = response.json()["summary"]
        summaries.append(f"{paper['title']}:\n{summary}\n")
    
    return "\n".join(summaries)
