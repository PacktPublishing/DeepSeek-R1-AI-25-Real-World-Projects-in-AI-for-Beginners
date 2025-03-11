import requests
import gradio as gr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_email_response(email_content, tone="Formal"):
    """
    Uses DeepSeek AI to generate an appropriate email response.
    """
    prompt = f"Generate an {tone} email as a response from the cutomer support team to the customer for the following email:\n\n{email_content}\n\n" \
             "Ensure the response is polite, clear, and professional."

    # prompt = f"Write an email response in {language}:\n\n{email_content}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No response generated.")
    else:
        return f"Error: {response.text}"

# Create Gradio interface
interface = gr.Interface(
    fn=generate_email_response,
    inputs=[
        gr.Textbox(lines=5, placeholder="Paste the email content here"),
        gr.Radio(["Formal", "Casual", "Friendly"], label="Tone"),
    ],
    outputs=gr.Textbox(label="AI-Generated Email Response"),
    title="AI-Powered Email Responder",
    description="Paste an email and let AI generate a professional response."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()

# # Test AI Email Responder
# if __name__ == "__main__":
#     test_email = "
"
#     print("### AI-Generated Email Response ###")
#     print(generate_email_response(test_email))
