import os
import re
from typing import List, Dict

class Replace:
    def __init__(self, languages: List[str] = None, all_languages: bool = False):
        # Get the path to the directory of the current script
        self.script_dir = os.path.dirname(os.path.realpath(__file__ ))
        
        # Initialize a dictionary containing paths to files with bad words for different languages
        self.language_files: Dict[str, str] = self.initialize_language_files()

        # If no languages are specified, use 'ru' (Russian) as the default
        if not languages:
            languages = ['ru']

        # If 'all_languages' is set to True, use all available languages
        if all_languages:
            languages = list(self.language_files.keys())

        # Initialize a dictionary of bad words for the specified languages
        self.bad_words: Dict[str, List[str]] = self.initialize_bad_words(languages)

        # Compile regular expressions for matching bad words
        self.patterns: Dict[str, re.Pattern] = self.compile_patterns()

    def initialize_language_files(self) -> Dict[str, str]:
        language_files = {}
        resource_dir = os.path.join(self.script_dir, 'resource/bad_words')

        # Get a list of files containing bad words for different languages
        for filename in os.listdir(resource_dir):
            language_code = os.path.splitext(filename)[0]
            file_path = os.path.join(resource_dir, filename)
            language_files[language_code] = file_path
        return language_files

    def initialize_bad_words(self, languages: List[str]) -> Dict[str, List[str]]:
        bad_words = {}
        for language in languages:
            file_path = self.language_files.get(language)
            if file_path is not None:
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Store bad words as a list of strings, removing leading/trailing whitespaces
                    bad_words[language] = [line.strip() for line in file]
        return bad_words

    def compile_patterns(self, case_insensitive: bool = True) -> Dict[str, re.Pattern]:
        patterns = {}
        flags = re.IGNORECASE if case_insensitive else 0
        for language, words in self.bad_words.items():
            patterns[language] = re.compile(r'(?:^|\s)(?:' + '|'.join(re.escape(word) for word in words) + r')(?=\s|$)', flags)
        return patterns

    def filter_profanity(self, text: str, language: str = 'ru', replacement_text: str = '[FILTERED]') -> str:
        if language not in self.language_files:
            raise ValueError(f'Unsupported language: {language}')
        if language not in self.patterns:
            return text

        # Replace bad words in the text with the specified replacement text
        filtered_text = self.patterns[language].sub(replacement_text, text)
        return filtered_text
