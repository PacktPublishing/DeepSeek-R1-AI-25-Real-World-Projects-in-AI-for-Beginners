from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/chatbot/")
def chatbot_response(query: str):
    payload = {"model": "deepseek-r1", "prompt": f"Answer customer query:\n\n{query}", "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No answer available.")

# Run with: uvicorn app:app --reload
