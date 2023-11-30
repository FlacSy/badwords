import os
import re
import easyocr
from typing import List, Dict

class ProfanityFilter:
    def __init__(self):
        self.script_dir = os.path.dirname(os.path.realpath(__file__))

        # Initialize a dictionary containing paths to files with bad words for different languages
        self.language_files: Dict[str, str] = self.initialize_language_files()

        languages = list(self.language_files.keys())

        # Initialize a dictionary of bad words for the specified languages
        self.bad_words: Dict[str, set] = self.initialize_bad_words(languages)

        # Compile regular expressions for matching bad words
        self.patterns: Dict[str, re.Pattern] = self.compile_patterns()

        # Lazy-loading of OCR reader
        self.reader = None

    def initialize_language_files(self) -> Dict[str, str]:
        language_files = {}
        resource_dir = os.path.join(self.script_dir, 'resource\\bad_words')

        # Get a list of files containing bad words for different languages
        for filename in os.listdir(resource_dir):
            language_code = os.path.splitext(filename)[0]
            file_path = os.path.join(resource_dir, filename)
            language_files[language_code] = file_path
        return language_files

    def initialize_bad_words(self, languages: List[str]) -> Dict[str, set]:
        bad_words = {}
        for language in languages:
            file_path = self.language_files.get(language)
            if file_path is not None:
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Store bad words as a set of strings, removing leading/trailing whitespaces
                    bad_words[language] = {line.strip() for line in file}
        return bad_words

    def compile_patterns(self, case_insensitive: bool = True) -> Dict[str, re.Pattern]:
        patterns = {}
        flags = re.IGNORECASE if case_insensitive else 0
        for language, words in self.bad_words.items():
            patterns[language] = re.compile(r'(?:^|\s)(?:' + '|'.join(re.escape(word) for word in words) + r')(?=\s|$)', flags)
        return patterns

    def lazy_load_ocr_reader(self, languages: List[str]):
        if self.reader is None:
            self.reader = easyocr.Reader(languages)

    def filter_profanity_from_image(self, image_path: str, language: str = 'ru') -> bool:
        if language not in self.language_files:
            raise ValueError(f'Unsupported language: {language}')

        # Lazy-load OCR reader
        self.lazy_load_ocr_reader([language])

        # Use easyocr to recognize text from the image
        results = self.reader.readtext(image_path)

        # Combine recognized text from multiple results
        text = ' '.join([result[1] for result in results])

        # Check for profanity using compiled patterns
        if language in self.patterns and self.patterns[language].search(text):
            return True
        return False
