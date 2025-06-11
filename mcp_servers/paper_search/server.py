from fastapi import FastAPI, Request
import uvicorn
import httpx
import xml.etree.ElementTree as ET

app = FastAPI()

@app.post("/search")
async def search_papers(request: Request):
    data = await request.json()
    query = data.get("query")
    max_results = data.get("max_results", 1)
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&max_results={max_results}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    root = ET.fromstring(response.text)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}

    results = []
    for entry in root.findall('atom:entry', ns):
        results.append({
            "title": entry.find('atom:title', ns).text,
            "pdf_url": entry.find('atom:id', ns).text.replace('abs', 'pdf') + ".pdf"
        })
    return results

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
