import string
from typing import List

class KeywordExtractor:
    def __init__(self):
        pass

    def preprocess_text(self, text: str) -> str:
        # Convert text to lowercase
        text = text.lower()

        # Remove punctuation from the text
        text = ''.join(char for char in text if char not in string.punctuation)

        return text

    def extract_keywords(self, text: str, num_keywords: int = 5) -> List[str]:
        # Preprocess the input text
        text = self.preprocess_text(text)

        # Split the preprocessed text into words
        words = text.split()

        # Initialize a dictionary to store word frequencies
        word_freq = {}

        # Calculate word frequencies in the text
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

        # Sort word frequencies in descending order
        sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

        # Extract the top 'num_keywords' words as keywords
        keywords = [word for word, _ in sorted_word_freq[:num_keywords]]

        return keywords
