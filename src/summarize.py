from transformers import pipeline

summarizer = pipeline('summarization')

def summarize_article(article):
    return summarizer(article, max_length=1300, min_length=30, do_sample=False)[0]['summary_text']

if __name__ == '__main__':
    article = ("Your long news article text here. "
               "This is just a placeholder text for testing the summarizer.")
    summary = summarize_article(article)
    print(summary)
