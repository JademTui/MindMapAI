class MemoryRecallModule:
    def __init__(self):
        self.memory = []

    def remember(self, statement):
        self.memory.append(statement)

    def recall(self):
        return self.memory