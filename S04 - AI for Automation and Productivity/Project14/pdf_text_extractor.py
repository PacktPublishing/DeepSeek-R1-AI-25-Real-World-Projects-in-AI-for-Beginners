import fitz  # PyMuPDF
import gradio as gr
import requests

from pdf2image import convert_from_path
import pytesseract
from PIL import Image

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file using PyMuPDF.
    """
    text = ""
    with fitz.open(pdf_file) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"

    return text if text.strip() else "No text found in the PDF."

def exetract_text_with_ocr(pdf_file):
    images = convert_from_path(pdf_file)
    extracted_text = "\n".join(pytesseract.image_to_string(img) for img in images)
    return extracted_text if extracted_text.strip() else "no text found in scanned PDFs"


def summarize_text(text):
    prompt = f"Summarize the following document text:\n\n{text}"
    
    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No summary available.")


# # Create Gradio interface
# interface = gr.Interface(
#     fn=extract_text_from_pdf,
#     inputs=gr.File(label="Upload PDF File"),
#     outputs=gr.Textbox(label="Extracted Text"),
#     title="AI-Powered PDF Text Extractor",
#     description="Upload a PDF file, and AI will extract its text content."
# )

# # Launch the web app
# if __name__ == "__main__":
#     interface.launch()


# Test PDF Text Extraction
if __name__ == "__main__":
    pdf_path = "sample.pdf"  # Provide a sample PDF file
    print("### Summarized Extracted Text ###")
    # print(extract_text_from_pdf(pdf_path))
    print(summarize_text(extract_text_from_pdf(pdf_path)))










