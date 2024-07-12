import requests

API_KEY = '71c468443a43428c99a99e9646e2751a'
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
