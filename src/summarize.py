from transformers import pipeline

summarizer = pipeline('summarization')

def summarize_article(article):
    # Calculate appropriate lengths based on input
    input_length = len(article.split())
    max_length = min(130, input_length)  # Cap at 130 words or input length
    min_length = min(30, max(10, input_length // 3))  # At least 10 words or 1/3 of input
    
    return summarizer(article, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']

if __name__ == '__main__':
    article = ("Your long news article text here. "
               "This is just a placeholder text for testing the summarizer.")
    summary = summarize_article(article)
    print(summary)
