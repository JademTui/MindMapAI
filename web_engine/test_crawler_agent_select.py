"""
Test the enhanced WebCrawler with agent-driven link selection and revert functionality.
"""
from web_engine.crawler import WebCrawler

def agent_select_link(url, links):
    # For test: pick the first link containing 'theorem', else None
    for link in links:
        if 'theorem' in link.lower():
            print(f"[Agent] Selecting link: {link}")
            return link
    return None

def main():
    crawler = WebCrawler(delay=0.5)
    start_urls = ["https://en.wikipedia.org/wiki/Mathematics"]
    pages = crawler.crawl(start_urls, max_pages=3, agent_select_link=agent_select_link)
    print(f"Crawled {len(pages)} pages.")
    for i, page in enumerate(pages, 1):
        print(f"--- Page {i}: {page['url']} ---")
        print(page['text'][:300], '...')
    # Test revert
    prev_page = crawler.revert_to_previous_page()
    if prev_page:
        print(f"[Revert] Returned to: {prev_page['url']}")
    else:
        print("[Revert] No previous page to revert to.")

if __name__ == "__main__":
    main()
