# archetypes/sentinel_guardian.py
class Sentinel:
    def __init__(self):
        self.active = False

    def evaluate_risk(self, logs):
        # Basic heuristic for demo
        return any("critical" in log['action'].lower() for log in logs)

    def activate_protocol(self):
        self.active = True
        print("[SENTINEL] Emergency protocol initiated. Resetting system...")
