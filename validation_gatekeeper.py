
class ValidationGatekeeper:
    def __init__(self):
        self.trusted_sources = ["pubmed", "arxiv", "university.edu", "official_journals"]

    def validate_source(self, source_url):
        return any(domain in source_url for domain in self.trusted_sources)

    def sanitize_data(self, data):
        # Basic sanitization stub
        return data.replace("<script>", "").replace("</script>", "")

    def approve_injection(self, source_url, data):
        if self.validate_source(source_url):
            return self.sanitize_data(data)
        return None
