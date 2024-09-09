 # News Article Summarization App

This project is an end-to-end AI-powered app designed to fetch, process, and summarize news articles. It leverages the NewsAPI, TextBlob, and Hugging Face Transformers to provide concise summaries of news articles entered by the user. The app is built using Streamlit for an interactive and user-friendly interface. The primary goal of this project is to enhance skills in API integration and text processing, with a focus on creating a simple yet effective summarization tool.

## Project Overview

The News Article Summarization App allows users to input specific topics or keywords, fetches relevant news articles using the NewsAPI, processes the text using TextBlob, and summarizes the articles using the Hugging Face Transformers summarization pipeline. The summarized articles are then displayed on the app interface. The project is a work in progress, with ongoing improvements needed in the text processing pipeline to enhance the quality of the summaries.

## Project Structure

- **`app.py`**: Main application file that sets up the Streamlit app and coordinates the flow between fetching, processing, and summarizing news articles.
- **`fetch_news.py`**: Contains functions to interact with NewsAPI, fetching articles based on user-inputted keywords.
- **`preprocess.py`**: Includes text preprocessing utilities to clean and prepare the news articles for summarization.
- **`summarize.py`**: Implements the summarization logic using the Hugging Face Transformers pipeline.
- **`sentiment.py`**: Provides additional sentiment analysis capabilities using TextBlob to analyze the tone of the fetched articles. 

## Future Improvements

   - Enhance text preprocessing to improve the accuracy and quality of summaries.
   - Expand the app's capabilities to support more languages and sources.
   - Refine the user interface for a more intuitive experience.
