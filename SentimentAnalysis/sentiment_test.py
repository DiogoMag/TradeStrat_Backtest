from textblob import TextBlob
import requests
from configy import news_apiKey

news_apiKey = '3bf9dac9c2e5482cbf2accbcb64654f9'
urlNews = f'https://newsapi.org/v2/everything?q=bitcoin&sortBy=publishedAt&apiKey={news_apiKey}'

# Get the latest BTC news articles
response = requests.get(urlNews)

if response.status_code == 200:
    articles = response.json()['articles']
    # Combine all the article descriptions into one string
    description = ' '.join([article['description'] for article in articles if 'description' in article])
    # Perform sentiment analysis using TextBlob
    sentiment = TextBlob(description).sentiment.polarity
    print(f"BTC sentiment: {sentiment}")
else:
    print("Error retrieving BTC news")
