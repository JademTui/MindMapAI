"""
Defines the interface for agents to process web content in the MindMapAI web engine.
"""
class WebContentAgent:
    def process_web_content(self, url, html, text):
        """
        Process a single web page and return agent-specific annotations or extracted facts.
        Args:
            url (str): The URL of the page.
            html (str): Raw HTML content.
            text (str): Extracted text content.
        Returns:
            dict: Agent's annotations or extracted info.
        """
        raise NotImplementedError
