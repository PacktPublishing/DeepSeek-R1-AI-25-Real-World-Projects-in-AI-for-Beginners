from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/generate_sql/")
def generate_sql(data: dict):
    prompt = f"Convert this query into SQL:\n\n{data['natural_query']}\n\nAssume database schema: {data.get('schema', 'unknown')}"
    
    payload = {"model": "deepseek-r1", "prompt": prompt, "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No SQL query available.")

# Run with: uvicorn app:app --reload
