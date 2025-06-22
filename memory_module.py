class MemoryManager:
    def __init__(self):
        self.memory_store = {}

    def remember(self, topic, info):
        if topic in self.memory_store:
            self.memory_store[topic].append(info)
        else:
            self.memory_store[topic] = [info]

    def recall(self, topic):
        return self.memory_store.get(topic, ["I don't recall anything about that."])[-1]

    def summarize_memory(self):
        return {k: v[-1] for k, v in self.memory_store.items()}