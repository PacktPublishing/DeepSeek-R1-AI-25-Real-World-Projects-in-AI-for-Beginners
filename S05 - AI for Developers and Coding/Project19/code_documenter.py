import requests
import gradio as gr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_readme(project_description):
    prompt = f"Generate a professional README file for the following project:\n\n{project_description}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No README generated.")

def document_api(code_snippet):
    prompt = f"Generate API documentation for the following code:\n\n{code_snippet}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No API documentation available.")



def generate_documentation(code_snippet, language="Python"):
    """
    Uses DeepSeek AI to generate documentation for a given code snippet.
    """
    prompt = f"Generate detailed documentation for the following {language} code:\n\n{code_snippet}\n\n" \
             "Add appropriate docstrings, comments, and explanations."

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No documentation generated.")
    else:
        return f"Error: {response.text}"

# Create Gradio interface
interface = gr.Interface(
    fn=generate_documentation,
    inputs=[
        gr.Textbox(lines=10, placeholder="Paste your code here"),
        gr.Dropdown(["Python", "JavaScript", "Java", "C++"], label="Select Language"),
    ],
    outputs=gr.Textbox(label="AI-Generated Documentation"),
    title="AI-Powered Documentation Generator",
    description="Paste your code, and AI will generate detailed documentation."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()


# # Test AI Documentation Generator
# if __name__ == "__main__":
#     test_code = "def add(a, b): return a + b"
#     print("### AI-Generated Documentation ###")
#     print(generate_documentation(test_code))
