import requests
import gradio as gr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def correct_grammar(text):
    """
    Uses DeepSeek AI to correct grammar and spelling errors in the given text.
    """
    prompt = f"Correct any spelling and grammar mistakes in the following text and provide explanations:\n\n{text}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No correction generated.")
    else:
        return f"Error: {response.text}"


# Create Gradio interface
interface = gr.Interface(
    fn=correct_grammar,
    inputs=gr.Textbox(lines=5, placeholder="Enter text with grammar or spelling mistakes"),
    outputs=gr.Textbox(label="Corrected Text"),
    title="AI-Powered Grammar and Spell Checker",
    description="Enter text with errors, and DeepSeek AI will correct them."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()


# # Test Grammar Correction
# if __name__ == "__main__":
#     sample_text = "He dont like to eat apple because they taste sour."
#     print("### Corrected Text ###")
#     print(correct_grammar(sample_text))
