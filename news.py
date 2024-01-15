import requests

def get_news(api_key, country='ru'):
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': country,
        'apiKey': api_key
    }

    response = requests.get(url, params=params)
    news_data = response.json()

    if news_data['status'] == 'ok':
        articles = news_data['articles']
        for index, article in enumerate(articles, 1):
            print(f"\n----- Article {index} -----")
            print(f"Title: {article['title']}")
            print(f"Author: {article['author']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
    else:
        print(f"Error: {news_data['message']}")

# Replace 'YOUR_API_KEY' with your actual News API key
api_key = '07d18be5ecea459bab4cc3c3b0815603'
get_news(api_key)
