import openai
from typing import List, Dict, Any, Optional

import os


class RefactClient:
    """
    Client for interacting with a local Refact backend (REST API) for code intelligence.
    """
    def __init__(self, api_key=None):
        # Prefer environment variable, fallback to provided key
        self.api_key = api_key or os.getenv("CODEX_API_KEY") or "972a16612e4572cd6469059c3ce3b4293e534bd1"
        openai.api_key = self.api_key

    def code_search(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Semantic code search."""
        url = f"http://localhost:8080/api/search"
        resp = requests.post(url, json={"query": query, "top_k": top_k})
        resp.raise_for_status()
        return resp.json().get("results", [])

    def code_completion(self, code: str, cursor_pos: int, max_tokens: int = 64) -> str:
        """Get code completion for a given code snippet and cursor position using OpenAI Codex."""
        prompt = code[:cursor_pos]
        response = openai.Completion.create(
            engine="code-davinci-002",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.2,
            stop=None,
        )
        return response.choices[0].text.strip()


    def chat_about_code(self, message: str, context: Optional[str] = None) -> str:
        """Chat with the AI about code context."""
        url = f"{self.base_url}/api/chat"
        payload = {"message": message}
        if context:
            payload["context"] = context
        resp = requests.post(url, json=payload)
        resp.raise_for_status()
        return resp.json().get("response", "")
