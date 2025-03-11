from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/generate/")
def generate_text(prompt: str, word_limit: int = 100):
    payload = {"model": "deepseek-r1", "prompt": f"Generate {word_limit} words:\n\n{prompt}", "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No content generated.")

# Run with: uvicorn app:app --reload
