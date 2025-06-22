class RefinementEngine:
    def summarize(self, text):
        sentences = text.split('. ')
        return '. '.join(sentences[:3]) + '...' if len(sentences) > 3 else text