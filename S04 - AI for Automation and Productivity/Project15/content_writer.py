import requests
import gradio as gr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_content(topic, keywords, tone="Professional"):
    """
    Uses DeepSeek AI to generate AI-powered content based on a topic.
    """
    prompt = f"Write a blog post about '{topic}' in a {tone} tone.\n\n" \
             f"Include the following keywords: {keywords}.\n\n" \
             f"Ensure the content is well-structured with an introduction, main sections, and a conclusion."

    # prompt = f"Write a blog post about '{topic}' in {language} using a {tone} tone."

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No content generated.")
    else:
        return f"Error: {response.text}"

def generate_social_media_post(topic, platform="Twitter"):
    prompt = f"Write an engaging social media post for {platform} about '{topic}'."

    payload = {

        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No post generated.")


# Create Gradio interface
interface = gr.Interface(
    fn=generate_content,
    inputs=[
        gr.Textbox(label="Topic"),
        gr.Textbox(label="Keywords (comma-separated)"),
        gr.Radio(["Professional", "Casual", "Persuasive"], label="Tone"),
    ],
    outputs=gr.Textbox(label="Generated Content"),
    title="AI-Powered Content Writer",
    description="Enter a topic, keywords, and tone, and AI will generate a blog post or marketing content."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()


# # Test AI Content Writer
# if __name__ == "__main__":
#     test_topic = "The Future of AI"
#     test_keywords = "AI, automation, deep learning"
#     print("### AI-Generated Content ###")
#     print(generate_content(test_topic, test_keywords))








