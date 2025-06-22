import requests
from bs4 import BeautifulSoup

class SmartScraper:
    def fetch_and_parse(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                return soup.get_text()
        except Exception as e:
            return str(e)