from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/legal/")
def generate_legal(text: str):
    payload = {"model": "deepseek-r1", "prompt": f"Generate a legal document:\n\n{text}", "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No contract generated.")

# Run with: uvicorn app:app --reload
