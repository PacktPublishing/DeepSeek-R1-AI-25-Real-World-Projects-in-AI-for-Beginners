from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/screen_candidate/")
def screen_candidate(data: dict):
    prompt = f"Analyze resume:\n\n{data['resume']}\n\nCompare with job description:\n\n{data['job_description']}"

    payload = {"model": "deepseek-r1", "prompt": prompt, "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No analysis available.")
