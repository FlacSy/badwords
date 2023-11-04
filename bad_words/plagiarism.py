import requests
from bs4 import BeautifulSoup
from googlesearch import search

class PlagiarismChecker:
    def __init__(self, query, page=5, text_to_check='', print_links=False):
        # Initialize the PlagiarismChecker with query, number of pages to search, text to check for plagiarism, and printing option
        self.query = query
        self.page = page
        self.text_to_check = text_to_check
        self.print_links = print_links

    def url_list(self):
        # Generate a list of URLs from a Google search query, limited to a specified number of pages
        urls = []
        for url in search(self.query, num_results=10):
            urls.append(url)
        return urls[:int(self.page)]

    def check_website_for_plagiarism(self, website_url):
        try:
            # Send an HTTP GET request to the website and parse the HTML content
            response = requests.get(website_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            page_text = soup.get_text()
            # Check if the provided text is present in the website's content
            if self.text_to_check in page_text:
                return True
        except Exception as e:
            print(f"Error checking website: {website_url}\n{str(e)}")

        return False

    def check_plagiarism(self):
        # Iterate through the list of URLs and check each one for plagiarism
        for i, link in enumerate(self.url_list(), start=1):
            if self.print_links:
                print(f"Checking Link {i}: {link}")
            if self.check_website_for_plagiarism(link):
                return True
        return False
