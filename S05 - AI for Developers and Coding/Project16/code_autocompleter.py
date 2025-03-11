import requests
import gradio as gr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def debug_code(code_snippet, language="Python"):
    prompt = f"Debug and optimize the following {language} code:\n\n{code_snippet}\n\n" \
             "Provide a fixed version with explanations."

    # prompt = f"Explain the following {language} code in simple terms:\n\n{code_snippet}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No debugging suggestions available.")


def complete_code(code_snippet, language="Python"):
    """
    Uses DeepSeek AI to provide code completions and suggestions.
    """
    prompt = f"Complete the following {language} code snippet:\n\n{code_snippet}\n\n" \
             "Provide a clean, efficient, and correct implementation."

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No code suggestion available.")
    else:
        return f"Error: {response.text}"

# Create Gradio interface
interface = gr.Interface(
    fn=complete_code,
    inputs=[
        gr.Textbox(lines=5, placeholder="Paste incomplete code here"),
        gr.Dropdown(["Python", "JavaScript", "Java", "C++"], label="Select Language"),
    ],
    outputs=gr.Textbox(label="AI-Suggested Code"),
    title="AI-Powered Code Auto-Completer",
    description="Enter an incomplete code snippet, and AI will complete it."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()


# # Test Code Auto-Completer
# if __name__ == "__main__":
#     test_code = "def fibonacci(n):"
#     print("### AI-Suggested Code ###")
#     print(complete_code(test_code))
