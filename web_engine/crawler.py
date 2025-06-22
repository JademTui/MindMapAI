"""
Web crawler for MindMapAI web engine. Crawls the internet, extracts content, and passes it to agents.
"""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

class WebCrawler:
    def __init__(self, user_agent="MindMapAIWebCrawler/1.0", delay=1):
        self.visited = set()
        self.user_agent = user_agent
        self.delay = delay
        self.page_stack = []  # Stack to support revert/back functionality

    def crawl(self, start_urls, max_pages=50, agent_select_link=None):
        """
        Crawl starting from start_urls, optionally letting an agent select which link to follow next.
        If agent_select_link is provided, it should be a function: (url, links) -> next_url or None.
        """
        queue = list(start_urls)
        pages = []
        while queue and len(pages) < max_pages:
            url = queue.pop(0)
            if url in self.visited:
                continue
            try:
                headers = {"User-Agent": self.user_agent}
                resp = requests.get(url, headers=headers, timeout=10)
                if resp.status_code == 200:
                    soup = BeautifulSoup(resp.text, "html.parser")
                    text = soup.get_text(" ", strip=True)
                    page = {"url": url, "html": resp.text, "text": text}
                    pages.append(page)
                    self.page_stack.append(page)  # Push current page to stack
                    # Extract links
                    links = []
                    for link in soup.find_all("a", href=True):
                        abs_url = urljoin(url, link["href"])
                        if urlparse(abs_url).scheme in ["http", "https"]:
                            links.append(abs_url)
                    # Agent can select which link(s) to follow next
                    if agent_select_link:
                        next_url = agent_select_link(url, links)
                        if next_url and next_url not in self.visited:
                            queue.insert(0, next_url)  # Prioritize agent-selected link
                    else:
                        for abs_url in links:
                            if abs_url not in self.visited:
                                queue.append(abs_url)
                self.visited.add(url)
                time.sleep(self.delay)
            except Exception as e:
                print(f"[Crawler] Error fetching {url}: {e}")
        return pages

    def revert_to_previous_page(self):
        """
        Pops the last page from the stack and returns it, allowing agents to go back.
        """
        if self.page_stack:
            return self.page_stack.pop()
        return None
