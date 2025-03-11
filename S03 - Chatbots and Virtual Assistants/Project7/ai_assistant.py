import requests
import gradio as gr
import speech_recognition as sr
import pyttsx3

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

# Text-to-Speech Engine
engine = pyttsx3.init()

def ai_assistant(text):
    """
    Uses DeepSeek AI to respond to queries.
    """
    prompt = f"Respond to this query as a personal AI assistant:\n\n{text}"

    # prompt = f"Act as a personal AI assistant. If the user asks for weather, fetch data. Otherwise, respond naturally:\n\n{text}"

    # p
    rompt = f"Respond in {language}:\n\n{text}"


    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        ai_response = response.json().get("response", "I'm sorry, I don't have an answer for that.")
        
        # Convert text to speech
        engine.say(ai_response)
        engine.runAndWait()
        
        return ai_response
    else:
        return "Sorry, I couldn't process your request."

# Voice Command Function
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"User: {command}")
        return command
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        return "Speech recognition service is unavailable."

# Create Gradio interface
interface = gr.Interface(
    fn=ai_assistant,
    inputs=gr.Textbox(lines=3, placeholder="Ask anything..."),
    outputs="text",
    title="AI-Powered Personal Assistant",
    description="Type a query or use voice commands to interact with the assistant.",
    live=True
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()



# # Test AI Assistant
# if __name__ == "__main__":
#     sample_query = "Tell me a fun fact about space."
#     print("### AI Assistant Response ###")
#     print(ai_assistant(sample_query))

# while True:
#     command = listen_command()
#     if "hey ai" in command.lower():
#         response = ai_assistant(command)
#         print(response)






