import re
from typing import List

def clean_topic(topic: str) -> str:
    # Remove excessive whitespace, special characters, and deduplicate spaces
    cleaned = re.sub(r'[^\w\s\-\?]', '', topic)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def summarize_context(context: str, max_sentences: int = 5) -> str:
    # Simple heuristic: take the first N sentences, remove duplicates
    sentences = re.split(r'(?<=[.!?]) +', context)
    seen = set()
    summary = []
    for s in sentences:
        s_clean = s.strip()
        if s_clean and s_clean not in seen:
            summary.append(s_clean)
            seen.add(s_clean)
        if len(summary) >= max_sentences:
            break
    return ' '.join(summary)
