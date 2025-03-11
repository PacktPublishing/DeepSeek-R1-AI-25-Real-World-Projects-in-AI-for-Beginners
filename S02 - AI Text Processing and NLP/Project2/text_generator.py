import requests
import gradio as gr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_text(prompt, word_limit=100, language="English"):
    """
    Uses DeepSeek AI to generate text based on a given prompt.
    """
    full_prompt = f"Write a {language}-language text to Generate a response within {word_limit} words:\n\n{prompt}"

    payload = {
        "model": "deepseek-r1",
        "prompt": full_prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No content generated.")
    else:
        return f"Error: {response.text}"

# Create Gradio interface
interface = gr.Interface(
    fn=generate_text,
    inputs=[gr.Textbox(lines=3, placeholder="Enter your prompt here"), gr.Slider(50, 500, step=50, label="Word Limit"), gr.Button("Regenrate")],
    outputs="text",
    title="AI-Powered Text Generator",
    description="Enter a prompt, select word limit, and generate AI-written content."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()


# # Test AI Generation
# if __name__ == "__main__":
#     prompt = "Write an introduction for an article about the future of AI."
#     print("### AI-Generated Content ###")
#     print(generate_text(prompt))
