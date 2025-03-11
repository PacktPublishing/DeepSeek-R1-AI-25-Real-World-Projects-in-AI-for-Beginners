from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/generate_content/")
def generate_content(data: dict):
    prompt = f"Write a {data['tone']} blog post about '{data['topic']}' including {data['keywords']}."

    payload = {"model": "deepseek-r1", "prompt": prompt, "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No content available.")

# Run with: uvicorn app:app --reload
