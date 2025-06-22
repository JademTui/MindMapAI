from modules.web_scraper_agent import WebScraperAgent

if __name__ == "__main__":
    agent = WebScraperAgent()
    query = "AI research"
    results = agent.scrape(query)
    print(f"Results for '{query}':")
    for r in results:
        print("-", r)
