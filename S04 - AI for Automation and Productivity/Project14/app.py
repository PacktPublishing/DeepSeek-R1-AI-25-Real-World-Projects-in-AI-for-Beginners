from fastapi import FastAPI, UploadFile, File
import fitz

app = FastAPI()

@app.post("/extract_text/")
async def extract_text(file: UploadFile = File(...)):
    text = ""
    with fitz.open(file) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    
    return {"extracted_text": text if text.strip() else "No text found in the PDF."}

# Run with: uvicorn app:app --reload
