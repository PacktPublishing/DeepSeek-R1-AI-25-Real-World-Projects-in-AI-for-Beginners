import requests
import gradio as gr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def debug_code(code_snippet, language="Python"):
    """
    Uses DeepSeek AI to analyze code and suggest bug fixes.
    """
    prompt = f"Analyze and debug the following {language} code:\n\n{code_snippet}\n\n" \
             "Identify issues, suggest fixes, and return the corrected code along with explanations."

    # prompt = f"Optimize the following {language} code for better performance and efficiency:\n\n{code_snippet}\n\n" \
    #          "Suggest improvements and return the optimized code."


    # prompt = f"Explain the following {language} error message and how to fix it:\n\n{error_message}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No debugging suggestions available.")
    else:
        return f"Error: {response.text}"

# Create Gradio interface
interface = gr.Interface(
    fn=debug_code,
    inputs=[
        gr.Textbox(lines=10, placeholder="Paste your buggy code here"),
        gr.Dropdown(["Python", "JavaScript", "Java", "C++"], label="Select Language"),
    ],
    outputs=gr.Textbox(label="AI Debugging Output"),
    title="AI-Powered Code Debugger",
    description="Paste buggy code, and AI will analyze and suggest fixes."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()


# # Test Code Debugger
# if __name__ == "__main__":
#     test_code = "def add_numbers(a, b): return a + b\nprint(add_numbers(5))"
#     print("### AI Debugging Output ###")
#     print(debug_code(test_code))
