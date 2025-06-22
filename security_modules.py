
class ValidationGatekeeper:
    @staticmethod
    def validate_input(data):
        print(f"[ValidationGatekeeper] Validating input: {data}")

class BranchPermissionLayer:
    @staticmethod
    def check_access(branch):
        print(f"[BranchPermissionLayer] Access granted to branch: {branch}")
