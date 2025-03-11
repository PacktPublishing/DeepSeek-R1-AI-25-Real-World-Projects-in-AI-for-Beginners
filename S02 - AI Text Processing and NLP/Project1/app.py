from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/summarize/")
def summarize_text(text: str):
    payload = {"model": "deepseek-r1", "prompt": f"Summarize:\n\n{text}", "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No summary generated.")

# Run with: uvicorn app:app --reload
