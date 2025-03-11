import requests
import gradio as gr
from fpdf import FPDF

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_resume(name, job_role, experience, skills, education, summary):
    """
    Uses DeepSeek AI to generate a structured professional resume.
    """
    prompt = f"Generate a professional resume based on the following details:\n\n" \
             f"Name: {name}\nJob Role: {job_role}\nExperience: {experience} years\n" \
             f"Skills: {skills}\nEducation: {education}\nSummary: {summary}\n\n" \
             f"Ensure the resume is ATS-friendly, well-formatted, and professional."


    # prompt = f"Generate a resume in {language}:\n\n{name}, {job_role}, {experience} years, {skills}, {education}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No resume generated.")
    else:
        return f"Error: {response.text}"

def generate_pdf_resume(resume_text, filename="resume.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for line in resume_text.split("\n"):
        pdf.cell(200, 10, txt=line, ln=True)
    
    pdf.output(filename)
    return filename




# Create Gradio interface
interface = gr.Interface(
    fn=generate_resume,
    inputs=[
        gr.Textbox(label="Full Name"),
        gr.Textbox(label="Job Role"),
        gr.Slider(0, 50, label="Years of Experience"),
        gr.Textbox(label="Skills (comma-separated)"),
        gr.Textbox(label="Education"),
        gr.Textbox(label="Summary (Optional)"),
    ],
    outputs=gr.Textbox(label="Generated Resume"),
    title="AI-Powered Resume Generator",
    description="Enter your details to generate a professional resume."
)



# Launch the web app
if __name__ == "__main__":
    interface.launch()


# # Test Resume Generator
# if __name__ == "__main__":
#     test_resume = generate_resume("John Doe", "Software Engineer", "3", 
#                                   "Python, AI, Web Development", "B.Sc. CS", "Experienced in AI and cloud computing.")
#     print("### AI-Generated Resume ###")
#     print(test_resume)


