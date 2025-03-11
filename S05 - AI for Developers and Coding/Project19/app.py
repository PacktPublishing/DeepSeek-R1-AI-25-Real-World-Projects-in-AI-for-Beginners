from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/generate_docs/")
def generate_docs(data: dict):
    payload = {"model": "deepseek-r1", "prompt": f"Generate documentation:\n\n{data['code_snippet']}", "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No documentation available.")

# Run with: uvicorn app:app --reload
