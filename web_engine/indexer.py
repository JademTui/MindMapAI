"""
Indexer for MindMapAI web engine. Stores crawled and agent-annotated content for search and retrieval.
"""
import os
import json

class WebIndexer:
    def __init__(self, index_path="web_index.json"):
        self.index_path = index_path
        self.index = []
        if os.path.exists(self.index_path):
            with open(self.index_path, "r", encoding="utf-8") as f:
                self.index = json.load(f)

    def add_document(self, doc):
        self.index.append(doc)
        with open(self.index_path, "w", encoding="utf-8") as f:
            json.dump(self.index, f, ensure_ascii=False, indent=2)

    def search(self, query):
        # Simple keyword search; can be replaced with more advanced ranking
        results = []
        for doc in self.index:
            if query.lower() in doc.get("text", "").lower():
                results.append(doc)
        return results
