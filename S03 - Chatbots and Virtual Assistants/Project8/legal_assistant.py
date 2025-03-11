import requests
import gradio as gr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

# Legal Document Templates
LEGAL_TEMPLATES = {
    "rental agreement": "Generate a rental agreement between {party1} (tenant) and {party2} (landlord) for {duration} months.",
    "employment contract": "Generate an employment contract between {party1} (employee) and {party2} (employer) with a salary of {salary} per year.",
    "business partnership agreement": "Draft a business partnership agreement between {party1} and {party2}, defining responsibilities and profit-sharing terms.",
    "nda": "Generate a non-disclosure agreement (NDA) between {party1} and {party2} to protect confidential business information."
}

def generate_legal_document(doc_type, party1, party2, duration="", salary=""):
    """
    Uses DeepSeek AI to generate legal contracts.
    """
    if doc_type not in LEGAL_TEMPLATES:
        return "Invalid document type. Please choose from rental agreement, employment contract, business partnership agreement, or NDA."

    prompt = LEGAL_TEMPLATES[doc_type].format(party1=party1, party2=party2, duration=duration, salary=salary)

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No document generated.")
    else:
        return f"Error: {response.text}"

# Create Gradio interface
interface = gr.Interface(
    fn=generate_legal_document,
    inputs=[
        gr.Radio(["Rental Agreement", "Employment Contract", "Business Partnership Agreement", "NDA"], label="Document Type"),
        gr.Textbox(label="Party 1 Name"),
        gr.Textbox(label="Party 2 Name"),
        gr.Textbox(label="Duration (if applicable, in months)", placeholder="e.g., 12"),
        gr.Textbox(label="Salary (if applicable, per year)", placeholder="e.g., $50,000"),
    ],
    outputs=gr.Textbox(label="Generated Legal Document"),
    title="AI-Powered Legal Assistant",
    description="Select a document type, enter party names, and generate a professional legal contract."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()



# # Test Legal Assistant
# if __name__ == "__main__":
#     print("### AI-Generated Contract ###")
#     print(generate_legal_document("rental agreement", "John Doe", "Jane Smith", duration="12"))



