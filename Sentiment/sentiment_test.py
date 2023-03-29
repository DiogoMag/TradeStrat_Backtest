from textblob import TextBlob
import requests

# Get the latest BTC news articles
response = requests.get('https://newsapi.org/v2/everything?q=bitcoin&sortBy=publishedAt&apiKey=YOUR_API_KEY')

if response.status_code == 200:
    articles = response.json()['articles']
    # Combine all the article descriptions into one string
    description = ' '.join([article['description'] for article in articles])
    # Perform sentiment analysis using TextBlob
    sentiment = TextBlob(description).sentiment.polarity
    print(f"BTC sentiment: {sentiment}")
else:
    print("Error retrieving BTC news")
