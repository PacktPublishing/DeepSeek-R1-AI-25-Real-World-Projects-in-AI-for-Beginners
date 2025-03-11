import requests
import gradio as gr
import pandas as pd

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"


# def analyze_uploaded_financial_report(file):
#     df = pd.read_csv(file.name) if file.name.endswith(".csv") else pd.read_excel(file.name)
#     financial_data = df.to_string()
#     return analyze_financial_report(financial_data)


def analyze_financial_report(financial_data):
    """
    Uses DeepSeek AI to analyze a financial statement and extract insights.
    """
    prompt = f"Analyze the following financial report:\n\n{financial_data}\n\n" \
             "Extract key financial metrics, detect trends, and provide a structured summary."

    # prompt = f"Analyze the following financial report for anomalies:\n\n{financial_data}\n\n" \
    #      "Identify unusual revenue changes, unexpected expenses, and financial risks."


    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No financial insights generated.")
    else:
        return f"Error: {response.text}"

# Create Gradio interface
interface = gr.Interface(
    fn=analyze_financial_report,
    inputs=gr.Textbox(lines=10, placeholder="Paste financial report data here"),
    outputs=gr.Textbox(label="AI-Generated Financial Insights"),
    title="AI-Powered Financial Report Analyzer",
    description="Paste a financial statement, and AI will extract insights and detect trends."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()


# # Test AI Financial Analyzer
# if __name__ == "__main__":
#     test_financial_data = "Company: ABC Inc, Revenue: $75M, Net Profit: $12M, Expenses: $50M, Debt: $10M"
#     print("### AI Financial Analysis ###")
#     print(analyze_financial_report(test_financial_data))
