import requests

API_KEY = 'API_KEY'
URL = 'https://newsapi.org/v2/everything'

def fetch_news(query, page=1):
    params = {
        'q': query,
        'apiKey': API_KEY,
        'page': page,
    }
    response = requests.get(URL, params=params)
    return response.json()

if __name__ == '__main__':
    articles = fetch_news('technology')
    print(articles)
