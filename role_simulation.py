import json
import os

class RoleSimulation:
    """
    Simulates different roles (teacher, peer, challenger) in multi-agent/user-agent interactions. Supports export/import and analytics.
    """
    def __init__(self, config_path="memory/role_simulation.json"):
        self.config_path = config_path
        self.role_log = []
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        self._load_config()

    def _load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r") as f:
                try:
                    self.role_log = json.load(f)
                except Exception:
                    self.role_log = []

    def _save_config(self):
        with open(self.config_path, "w") as f:
            json.dump(self.role_log, f, indent=2)

    def simulate_role(self, role, context, message):
        # Simulate response based on role
        if role == "teacher":
            response = f"As a teacher: {message}"
        elif role == "peer":
            response = f"As a peer: {message}"
        elif role == "challenger":
            response = f"As a challenger: {message}"
        else:
            response = f"As {role}: {message}"
        event = {"role": role, "context": context, "message": message, "response": response}
        self.role_log.append(event)
        self._save_config()
        return response

    def export_log(self, path):
        with open(path, "w") as f:
            json.dump(self.role_log, f, indent=2)

    def import_log(self, path):
        with open(path, "r") as f:
            self.role_log = json.load(f)
