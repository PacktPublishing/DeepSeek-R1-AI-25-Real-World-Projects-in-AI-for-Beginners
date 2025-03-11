from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/analyze_feedback/")
def analyze_feedback(data: dict):
    prompt = f"Analyze customer feedback:\n\n{data['feedback']}\n\nProvide sentiment and insights."

    payload = {"model": "deepseek-r1", "prompt": prompt, "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No analysis available.")

# Run with: uvicorn app:app --reload
