# API_KEY

import requests
import gradio as gr

# API Keys
NEWS_API_KEY = "API_KEY"
OLLAMA_URL = "http://localhost:11434/api/generate"

def fetch_latest_news(category="technology", country="us"):
    """
    Fetches the latest news articles from NewsAPI based on category and country.
    """
    url = f"https://newsapi.org/v2/top-headlines?category={category}&country={country}&apiKey={NEWS_API_KEY}"
    
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        if not articles:
            return "No news articles found."
        
        # Extract title and content from the first article
        news_title = articles[0]["title"]
        news_content = articles[0]["description"] or articles[0]["content"]

        return news_title, news_content
    else:
        return "Error fetching news."

def summarize_news(category="technology", country="us"):
    """
    Fetches and summarizes the latest news article.
    """
    news_title, news_content = fetch_latest_news(category, country)

    if news_content == "No news articles found.":
        return "No news available for this category."

    # Generate summary using DeepSeek AI
    prompt = f"Summarize the following news article:\n\nTitle: {news_title}\n\nContent: {news_content}\n\n" \
             "Provide a short and informative summary."
    
    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        summary = response.json().get("response", "No summary generated.")
    else:
        summary = "Error summarizing news."

    return f"📰 **{news_title}**\n📅 **Category:** {category.capitalize()}\n🔹 **Summary:** {summary}"

# def search_news(keyword):
#     url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={NEWS_API_KEY}"


# def fetch_news_from_source(source="nytimes", category="technology"):
#     url = f"https://api.nytimes.com/svc/topstories/v2/{category}.json?api-key=your_nytimes_api_key"


# Create Gradio interface
interface = gr.Interface(
    fn=summarize_news,
    inputs=gr.Dropdown(["technology", "business", "health", "sports", "entertainment", "science"], label="Select News Category"),
    outputs=gr.Textbox(label="AI-Generated News Summary"),
    title="AI-Powered News Summarizer",
    description="Select a category to fetch and summarize the latest news."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()


# # Test AI News Summarizer
# if __name__ == "__main__":
#     print("### AI News Summary ###")
#     print(summarize_news("technology"))





