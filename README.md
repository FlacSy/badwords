# badwords (Bad Word Filter and More)

`badwords` is a versatile Python library designed to filter text, detect obscene words, perform sentiment analysis, extract keywords, check for plagiarism, and more. It supports multiple languages, including English, Polish, German, Russian, and Ukrainian, making it a valuable tool for content moderation and text analysis.

**Table of Contents:**

1. [Installation](#installation)
2. [Basic Usage](#basic-usage)
   - [1. Checking for Obscene Words](#1-checking-for-obscene-words)
   - [2. Filtering Obscene Words](#2-filtering-obscene-words)
   - [3. Sentiment Analysis](#3-sentiment-analysis)
   - [4. Keyword Extraction](#4-keyword-extraction)
   - [5. Plagiarism Checker](#5-plagiarism-checker)
3. [Advanced Usage](#advanced-usage)
   - [1. Customizing Bad Word Lists](#1-customizing-bad-word-lists)
   - [2. Loading and Unloading Word Lists](#2-loading-and-unloading-word-lists)
4. [License](#license)
5. [Author](#author)
6. [Links](#links)

## Installation

You can easily install `badwords` using `pip`:

```shell
pip install git+https://github.com/FlacSy/badwords.git
```

## Basic Usage

### 1. Checking for Obscene Words

The core functionality of `badwords` is to check for obscene words in text.

#### Example:

```python
from badwords.check import Check

# Create a filter for the Russian language
filter_ru = Check(languages=['ru'])

# Input text for checking
text = input('Enter a text: ')

# Check if the text contains obscene words in Russian
if filter_ru.filter_profanity(text, language='ru'):
    print("The text contains obscene words in Russian")
```

### 2. Filtering Obscene Words

You can filter and remove obscene words from text, or replace them with a specified replacement text.

#### Example:

```python
from badwords.delete import Delete

# Create a filter for the Russian language
filter = Delete(languages=['ru'])

# Input text for filtering
text = input('Enter a text: ')

# Filter and remove obscene words in Russian
filtered_text = filter.filter_profanity(text, language='ru')
print(filtered_text)
```

### 3. Sentiment Analysis

`badwords` includes a sentiment analysis feature for supported languages, allowing you to determine the sentiment of a given text.

#### Example:

```python
from badwords.analyzer import SentimentAnalyzer

# Create a sentiment analyzer for all supported languages
analyzer = SentimentAnalyzer(all_languages=True)

# Input text for sentiment analysis
text = input('Enter a text: ')

# Analyze sentiment in each supported language
for language in analyzer.supported_languages:
    sentiment = analyzer.analyze_sentiment(text, language=language)
    print(f"Sentiment in {language}: {sentiment}")
```

### 4. Keyword Extraction

You can extract keywords from a given text using the `KeywordExtractor` module.

#### Example:

```python
from badwords.keyword_extractor import KeywordExtractor

# Create a keyword extractor
extractor = KeywordExtractor()

# Input text for keyword extraction
text = input('Enter a text: ')

# Extract keywords from the text
keywords = extractor.extract_keywords(text)
print("Keywords:", keywords)
```

### 5. Plagiarism Checker

`badwords` provides a `PlagiarismChecker` module to check for plagiarism in online content.

#### Example:

```python
from badwords.plagiarism_checker import PlagiarismChecker

# Initialize the PlagiarismChecker with a query and the number of pages to search
query = input('Enter a search query: ')
pages = int(input('Enter the number of pages to search: '))
checker = PlagiarismChecker(query=query, page=pages)

# Check for plagiarism in online content
if checker.check_plagiarism():
    print("Plagiarism detected!")
else:
    print("No plagiarism detected.")
```

## Advanced Usage

### 1. Customizing Bad Word Lists

You can customize the list of bad words by modifying the word lists located in the `resource/bad_words` directory.

### 2. Loading and Unloading Word Lists

`badwords` allows you to load and unload word lists for customization or specific needs. Use the `Load` and `Unload` classes for this purpose.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- [FlacSy](https://github.com/FlacSy)

## Links

- [GitHub repository](https://github.com/FlacSy/badwords)
- [Discord server](https://discord.gg/c4yNwz3uqZ)

Feel free to explore and utilize the various features of `badwords` for your text processing and content moderation needs.