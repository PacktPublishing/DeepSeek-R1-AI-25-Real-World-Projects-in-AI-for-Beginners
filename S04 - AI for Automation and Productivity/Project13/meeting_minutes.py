import requests
import gradio as gr
import speech_recognition as sr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_meeting_minutes(transcript):
    """
    Uses DeepSeek AI to generate a structured meeting summary.
    """
    prompt = f"Summarize the following meeting transcript into structured meeting minutes:\n\n{transcript}\n\n" \
             "Extract key discussions, decisions made, and action items."

    # prompt = f"Summarize this meeting transcript in {language}:\n\n{transcript}"
             
    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No summary generated.")
    else:
        return f"Error: {response.text}"

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)


# Create Gradio interface
interface = gr.Interface(
    fn=generate_meeting_minutes,
    inputs=gr.Textbox(lines=5, placeholder="Paste your meeting transcript here"),
    outputs=gr.Textbox(label="Generated Meeting Minutes"),
    title="AI-Powered Meeting Minutes Generator",
    description="Paste a meeting transcript, and AI will generate a structured summary with key points and action items."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()



# # Test Meeting Minutes Generator
# if __name__ == "__main__":
#     test_transcript = "John: Q4 sales increased by 15%. Sarah: We need to increase the marketing budget. Decision: Approve higher budget."
#     print("### AI-Generated Meeting Minutes ###")
#     print(generate_meeting_minutes(test_transcript))
