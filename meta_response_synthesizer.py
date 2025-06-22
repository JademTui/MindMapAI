
class MetaResponseSynthesizer:
    def __init__(self, manager):
        self.manager = manager

    def synthesize(self, input_text):
        model = "mistral"
        return self.manager.run_model(model, input_text)
