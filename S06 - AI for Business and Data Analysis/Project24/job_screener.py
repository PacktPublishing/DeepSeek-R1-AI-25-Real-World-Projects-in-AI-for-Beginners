import requests
import fitz  # PyMuPDF
import gradio as gr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a resume PDF file.
    """
    text = ""
    with fitz.open(pdf_file.name) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text if text.strip() else "No text found in the PDF."

# def screen_multiple_candidates(resume_list, job_description):
#     results = [screen_candidate(resume, job_description) for resume in resume_list]
#     return "\n\n".join(results)



def screen_candidate(resume_text, job_description):
    """
    Uses DeepSeek AI to analyze a resume and compare it with a job description.
    """

    prompt = f"Analyze the following resume and compare it with the job description.\n\n" \
             f"Resume:\n{resume_text}\n\n" \
             f"Job Description:\n{job_description}\n\n" \
             "Provide a suitability score (0-100%) based on skills and experience. Highlight matches and missing criteria."

    # prompt += " Suggest ways for the candidate to improve their qualifications for this role."

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No analysis generated.")
    else:
        return f"Error: {response.text}"

# Create Gradio interface
interface = gr.Interface(
    fn=screen_candidate,
    inputs=[
        gr.Textbox(lines=5, placeholder="Candidate Information"),#gr.File(label="Upload PDF File")
        gr.Textbox(lines=5, placeholder="Paste Job Description Here"),
    ],
    outputs=gr.Textbox(label="AI Screening Report"),
    title="AI-Powered Job Application Screener",
    description="Upload a resume and provide a job description to evaluate candidate suitability."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()

# # Test AI Job Screener
# if __name__ == "__main__":
#     test_resume = "Name: John Doe, Experience: 1 years in Web Development, Skills: Java, Education: B.Sc. in Mechanical Engineering"
#     test_job_description = "Role: Backend Engineer, Required Skills: Python, Flask, SQL, API Development, Experience: 3+ years"
    
#     print("### AI Screening Report ###")
#     print(screen_candidate(test_resume, test_job_description))





