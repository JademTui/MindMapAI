class EvolvingMemory:
    def __init__(self):
        self.interactions = []

    def store_interaction(self, user_input):
        self.interactions.append(user_input)

    def recall(self):
        return self.interactions[-5:] if self.interactions else []
