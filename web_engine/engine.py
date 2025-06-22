"""
Main engine for agent-integrated web search in MindMapAI.
Coordinates crawling, agent analysis, indexing, and query answering.
"""
from .crawler import WebCrawler
from .indexer import WebIndexer
from .agent_interface import WebContentAgent

class MindMapAIWebEngine:
    def __init__(self, agents, index_path="web_index.json"):
        self.crawler = WebCrawler()
        self.indexer = WebIndexer(index_path)
        self.agents = agents  # List of agent instances

    def crawl_and_process(self, start_urls, max_pages=20, agent_select_link=None, agent_revert_decision=None):
        """
        Crawl and process pages. Agents can select which link to follow next, and decide to revert to previous pages.
        agent_select_link: function (url, links) -> next_url or None
        agent_revert_decision: function (current_page, agent_annotations) -> bool (True to revert)
        """
        pages = self.crawler.crawl(start_urls, max_pages=max_pages, agent_select_link=agent_select_link)
        for page in pages:
            agent_annotations = {}
            for agent in self.agents:
                try:
                    annotation = agent.process_web_content(page["url"], page["html"], page["text"])
                    agent_annotations[agent.__class__.__name__] = annotation
                except Exception as e:
                    agent_annotations[agent.__class__.__name__] = {"error": str(e)}
            doc = {
                "url": page["url"],
                "text": page["text"],
                "annotations": agent_annotations
            }
            self.indexer.add_document(doc)
            # Agent-driven revert: ask if an agent wants to revert
            if agent_revert_decision and agent_revert_decision(page, agent_annotations):
                prev_page = self.crawler.revert_to_previous_page()
                if prev_page:
                    print(f"[WebEngine] Reverted to previous page: {prev_page['url']}")

    def search(self, query):
        results = self.indexer.search(query)
        # Optionally, pass results through agents for ranking/synthesis
        return results
