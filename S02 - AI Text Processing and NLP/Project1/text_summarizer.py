import requests
import gradio as gr

# DeepSeek API Endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def summarize_text(text):
    """
    Uses DeepSeek AI to summarize a given text.
    """

    payload = {
        "model": "deepseek-r1",
        "prompt": f"Summarize the following text in **3 bullet points**:\n\n{text}",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No summary generated.")
    else:
        return f"Error: {response.text}"



# Create Gradio interface
interface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=10, placeholder="Enter text to summarize"),
    outputs=gr.Textbox(label="Summarized Text"),
    title="AI-Powered Text Summarizer",
    description="Enter a long text and DeepSeek AI will generate a concise summary."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()


# # Test Summarization
# if __name__ == "__main__":
#     sample_text = """
#     Artificial Intelligence is transforming industries across the world. AI models like DeepSeek-R1 enable businesses to automate tasks,
#     analyze large datasets, and enhance productivity. With advancements in AI, applications range from virtual assistants to predictive analytics
#     and personalized recommendations.
#     """
#     print("### Summary ###")
#     print(summarize_text(sample_text))
