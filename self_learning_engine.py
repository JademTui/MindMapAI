
import json
from datetime import datetime

class SelfLearningEngine:
    def __init__(self):
        self.knowledge_base = []

    def learn_from(self, text, relevance_topic=None):
        entry = {
            "text": text,
            "topic": relevance_topic or self._infer_topic(text),
            "timestamp": datetime.now().isoformat()
        }
        self.knowledge_base.append(entry)
        self._save()

    def _infer_topic(self, text):
        # Simple topic inference (can be extended with NLP)
        if "AI" in text: return "Artificial Intelligence"
        elif "emotion" in text: return "Emotion"
        elif "ethics" in text: return "Ethics"
        elif "neural" in text: return "Neuroscience"
        elif "world" in text or "news" in text: return "Current Events"
        return "General"

    def retrieve_relevant(self, topic):
        return [k for k in self.knowledge_base if topic.lower() in k['topic'].lower()]

    def _save(self):
        try:
            with open("learned_knowledge.json", "w") as f:
                json.dump(self.knowledge_base, f, indent=4)
        except Exception as e:
            print("[Error saving knowledge]", e)

    def load_knowledge(self):
        try:
            with open("learned_knowledge.json", "r") as f:
                self.knowledge_base = json.load(f)
        except:
            self.knowledge_base = []
