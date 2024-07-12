from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

if __name__ == '__main__':
    article = "Your news article text here."
    sentiment = analyze_sentiment(article)
    print(sentiment)
