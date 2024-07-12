import re
from bs4 import BeautifulSoup

def clean_text(text):
    # Remove HTML tags using BeautifulSoup
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Remove HTML entities
    text = re.sub(r'&\w+;', '', text)

    # Remove any non-alphanumeric characters (except spaces)
    text = re.sub(r'[^A-Za-z0-9\s]+', '', text)

    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text).strip()

    return text

if __name__ == '__main__':
    sample_text = """
    <p>This is a <b>sample</b> news article! Check out more at https://example.com</p>
    &nbsp; &copy;
    """
    clean_text_result = clean_text(sample_text)
    print(clean_text_result)
