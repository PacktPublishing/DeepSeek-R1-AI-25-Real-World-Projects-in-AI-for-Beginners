import requests

# Define API URL (Ollama runs locally on port 11434)
OLLAMA_URL = "http://localhost:11434/api/generate"

def query_deepseek(prompt):
    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(OLLAMA_URL, json=payload)
    
    if response.status_code == 200:
        return response.json().get("response", "No output generated.")
    else:
        return f"Error: {response.text}"

# Test the model
test_prompt = "Summarize: The impact of AI in business is profound, enabling automation and enhancing decision-making."
print(query_deepseek(test_prompt))
