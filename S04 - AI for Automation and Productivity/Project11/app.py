from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/email/")
def generate_email(email_content: str, tone: str = "Formal"):
    payload = {"model": "deepseek-r1", "prompt": f"Write a {tone} email response:\n\n{email_content}", "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No response available.")

# Run with: uvicorn app:app --reload
