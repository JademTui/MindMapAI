import requests
from bs4 import BeautifulSoup

class NewsFetcher:
    def fetch_news(self, topic):
        url = f"https://www.google.com/search?q={topic}&tbm=nws"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h3')
        return [h.get_text() for h in headlines[:5]]