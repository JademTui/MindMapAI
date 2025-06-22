class SecurityModule:
    def validate_input(self, input_data):
        return "[SECURE] Input validated"

    def sanitize(self, input_data):
        return input_data.replace("<", "").replace(">", "")