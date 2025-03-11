from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/summarize_paper/")
def summarize_paper(data: dict):
    prompt = f"Summarize research paper:\n\n{data['paper_text']}\n\nExtract key insights."

    payload = {"model": "deepseek-r1", "prompt": prompt, "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No summary available.")
