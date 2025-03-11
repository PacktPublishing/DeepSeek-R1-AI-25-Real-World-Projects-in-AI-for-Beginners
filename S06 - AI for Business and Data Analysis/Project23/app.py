from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/analyze_financials/")
def analyze_financials(data: dict):
    prompt = f"Analyze financial report:\n\n{data['report']}\n\nProvide insights and detect trends."

    payload = {"model": "deepseek-r1", "prompt": prompt, "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No analysis available.")

# Run with: uvicorn app:app --reload
