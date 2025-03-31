import os
import requests
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Get API key from environment variable or Streamlit secrets
def get_api_key():
    try:
        # Try to get from Streamlit secrets first (for cloud deployment)
        return st.secrets["NEWS_API_KEY"]
    except:
        # Fall back to environment variable (for local development)
        return os.getenv('NEWS_API_KEY')

API_KEY = get_api_key()
URL = 'https://newsapi.org/v2/everything'

def fetch_news(query, page=1):
    if not API_KEY:
        raise ValueError("Please set the NEWS_API_KEY in your environment variables or Streamlit secrets")
    
    params = {
        'q': query,
        'apiKey': API_KEY,
        'page': page,
        'pageSize': 5,  # Limit to 5 articles per request
        'sortBy': 'relevancy'  # Get most relevant articles first
    }
    response = requests.get(URL, params=params)
    data = response.json()
    
    if response.status_code != 200:
        raise Exception(f"Error fetching news: {data.get('message', 'Unknown error')}")
    
    # Process articles to handle truncated content
    if 'articles' in data:
        for article in data['articles']:
            # Try to get the full content from description if content is truncated
            if article.get('content') and '...' in article['content']:
                if article.get('description'):
                    article['content'] = article['description']
                else:
                    # Remove the truncated part
                    article['content'] = article['content'].split('...')[0]
    
    return data

if __name__ == '__main__':
    try:
        articles = fetch_news('technology')
        print(articles)
    except Exception as e:
        print(f"Error: {e}")
