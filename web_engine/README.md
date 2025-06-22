# MindMapAI Web Engine (Agent-Integrated)

This module implements a web search engine that integrates all MindMapAI agents into the crawling, analysis, and search pipeline.

## Components

- **crawler.py**: Crawls the internet, downloads web pages.
- **indexer.py**: Indexes crawled and agent-annotated content for search.
- **agent_interface.py**: Defines the interface for agents to process web content.
- **engine.py**: Coordinates crawling, agent analysis, indexing, and search.

## Usage

1. Implement `process_web_content(url, html, text)` in each agent.
2. Instantiate `MindMapAIWebEngine` with a list of agents.
3. Use `crawl_and_process(start_urls)` to crawl and process pages.
4. Use `search(query)` to search the indexed content.

## Example

```python
from web_engine.engine import MindMapAIWebEngine
from my_agents import ScienceAgent, ArtsAgent, FinanceAgent

engine = MindMapAIWebEngine([
    ScienceAgent(),
    ArtsAgent(),
    FinanceAgent(),
])

engine.crawl_and_process(["https://en.wikipedia.org/wiki/Artificial_intelligence"])
results = engine.search("machine learning")
for doc in results:
    print(doc["url"], doc["annotations"])
```

## Notes
- This is a modular, extensible foundation. You can add advanced ranking, semantic search, or mind map visualization as needed.
- Be mindful of web crawling ethics and bandwidth usage.
