import os
import re
from typing import List, Dict

class Check:
    def __init__(self, languages: List[str] = None, all_languages: bool = False):
        self.script_dir = os.path.dirname(os.path.realpath(__file__))
        self.language_files: Dict[str, str] = self.initialize_language_files()
        self.languages = languages
        if all_languages:
            self.languages = list(self.language_files.keys())
        self.bad_words: Dict[str, List[str]] = self.initialize_bad_words(self.languages)
        self.patterns: Dict[str, re.Pattern] = self.compile_patterns()
        self.custom_bad_words: List[str] = []

    def initialize_language_files(self) -> Dict[str, str]:
        language_files = {}
        resource_dir = os.path.join(self.script_dir, 'resource\\bad_words')
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
                    bad_words[language] = [line.strip() for line in file]
        return bad_words

    def compile_patterns(self) -> Dict[str, re.Pattern]:
        patterns = {}
        for language, words in self.bad_words.items():
            patterns[language] = re.compile(r'\b(?:' + '|'.join(re.escape(word) for word in words) + r')\b', re.IGNORECASE)
        return patterns

    def add_words(self, words: List[str]):
        self.custom_bad_words.extend(words)

    def filter_profanity(self, text: str) -> bool:
        all_bad_words = set(self.custom_bad_words)
        for language in self.languages:
            all_bad_words.update(self.bad_words.get(language, []))
        
        pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, all_bad_words)) + r')\b', re.IGNORECASE)
        matches = pattern.findall(text)
        return bool(matches)
