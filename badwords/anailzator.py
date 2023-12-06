import os
from typing import List, Dict

class SentimentAnalyzer:
    def __init__(self, languages: List[str] = None, all_languages: bool = False):
        # Get the path to the current script
        self.script_dir = os.path.dirname(os.path.realpath(__file__))

        # Initialize a dictionary containing paths to files with keywords for different languages
        self.language_files: Dict[str, str] = self.initialize_language_files()

        # Get a list of supported languages
        self.supported_languages: List[str] = list(self.language_files.keys())

        # If no languages are specified, use Russian as the default
        if not languages:
            languages = ['ru']

        # If all_languages is set to True, use all supported languages
        if all_languages:
            languages = self.supported_languages

        # Check that the specified languages are supported
        for language in languages:
            if language not in self.supported_languages:
                raise ValueError(f'Unsupported language: {language}')

        # Initialize a dictionary for bad keywords
        self.bad_keywords: Dict[str, List[str]] = self.initialize_keywords(languages)

        # Initialize a dictionary for good keywords
        self.good_keywords: Dict[str, List[str]] = self.initialize_good_keywords(languages)

    def initialize_language_files(self) -> Dict[str, str]:
        language_files = {}
        resource_dir = os.path.join(self.script_dir, 'resource\\bad_words')

        # Get a list of files with keywords for different languages
        for filename in os.listdir(resource_dir):
            language_code = os.path.splitext(filename)[0]
            file_path = os.path.join(resource_dir, filename)
            language_files[language_code] = file_path
        return language_files

    def initialize_keywords(self, languages: List[str]) -> Dict[str, List[str]]:
        bad_keywords = {}
        for language in languages:
            file_path = self.language_files.get(f"{language}.bdw")

            if file_path is not None:
                with open(file_path, 'r', encoding='utf-8') as file:
                    bad_keywords[language] = file.read().splitlines()
        return bad_keywords

    def initialize_good_keywords(self, languages: List[str]) -> Dict[str, List[str]]:
        good_keywords = {}
        for language in languages:
            file_path = self.language_files.get(language)

            if file_path is not None:
                good_file_path = file_path.replace("bad_words", "good_words")

                if os.path.isfile(good_file_path):
                    with open(good_file_path, 'r', encoding='utf-8') as file:
                        good_keywords[language] = file.read().splitlines()
                else:
                    good_keywords[language] = []
        return good_keywords

    def analyze_sentiment(self, text: str, language: str = 'ru') -> str:
        if language not in self.supported_languages:
            raise ValueError(f'Unsupported language: {language}')

        text = text.lower()
        words = text.split()

        positive_score = sum(self.get_word_sentiment(word, language) for word in words)

        if positive_score > 0:
            return 'positive'
        elif positive_score < 0:
            return 'negative'
        else:
            return 'neutral'

    def get_word_sentiment(self, word: str, language: str) -> int:
        positive_score = 0
        negative_score = 0

        if language in self.good_keywords:
            positive_score += self.good_keywords[language].count(word)
        if language in self.bad_keywords:
            negative_score += self.bad_keywords[language].count(word)

        return positive_score - negative_score
