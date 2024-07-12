import streamlit as st
from fetch_news import fetch_news
from preprocess import clean_text
from summarize import summarize_article
from sentiment import analyze_sentiment

st.title("News Article Summarization and Analysis")

# Text input for the topic
query = st.text_input("Enter a topic to search for news articles:")

if query:
    articles = fetch_news(query)['articles']
    for article in articles:
        title = article['title']
        content = article.get('content') or article.get('description') or ''

        if content:
            clean_content = clean_text(content)
            summary = summarize_article(clean_content)
            sentiment = analyze_sentiment(clean_content)

            st.subheader(title)
            st.write("**Original Article:**")
            st.write(content)
            st.write("**Cleaned Content:**")
            st.write(clean_content)
            st.write("**Summary:**")
            st.write(summary)
            st.write("**Sentiment Polarity:**")
            st.write(f"{sentiment:.2f}")
            st.write("---")
