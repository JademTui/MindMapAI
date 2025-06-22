import requests
from bs4 import BeautifulSoup

class WebIntelAgent:
    def search(self, query):
        url = f"https://www.google.com/search?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = [a.text for a in soup.select('h3')]
        return results[:5]
