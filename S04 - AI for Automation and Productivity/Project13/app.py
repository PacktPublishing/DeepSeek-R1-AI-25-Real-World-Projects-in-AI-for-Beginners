from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/meeting_minutes/")
def generate_minutes(transcript: str):
    payload = {"model": "deepseek-r1", "prompt": f"Summarize meeting:\n\n{transcript}", "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No summary available.")

# Run with: uvicorn app:app --reload
