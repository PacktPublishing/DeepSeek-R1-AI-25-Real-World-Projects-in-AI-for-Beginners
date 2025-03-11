from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/medical/")
def analyze_symptoms(symptoms: str):
    payload = {"model": "deepseek-r1", "prompt": f"Medical symptom analysis:\n\n{symptoms}", "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No information available.")

# Run with: uvicorn app:app --reload
