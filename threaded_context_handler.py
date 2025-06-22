
class ThreadedContextHandler:
    def __init__(self):
        self.history = []

    def update_context(self, user_input, ai_response):
        self.history.append({'user': user_input, 'ai': ai_response})
        if len(self.history) > 10:
            self.history.pop(0)

    def build_context(self):
        return " ".join([f"<s>[INST] {h['user']} [/INST] {h['ai']}" for h in self.history])
