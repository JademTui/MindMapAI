import os
import json
from datetime import datetime

class UserDashboard:
    def __init__(self, logs_dir="logs", evolution_dir="evolution_logs"):
        self.logs_dir = logs_dir
        self.evolution_dir = evolution_dir
        os.makedirs(self.logs_dir, exist_ok=True)
        os.makedirs(self.evolution_dir, exist_ok=True)
        self.settings_file = os.path.join(self.logs_dir, "user_settings.json")
        self.settings = self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r") as f:
                return json.load(f)
        # Default settings
        return {
            "risk_tolerance": "medium",
            "mutation_aggressiveness": 1,
            "reasoning_depth": 1
        }

    def save_settings(self, settings):
        with open(self.settings_file, "w") as f:
            json.dump(settings, f, indent=2)
        self.settings = settings

    def set_setting(self, key, value):
        self.settings[key] = value
        self.save_settings(self.settings)

    def get_setting(self, key):
        return self.settings.get(key)

    def list_evolution_logs(self):
        logs = []
        for fname in os.listdir(self.evolution_dir):
            if fname.endswith(".json"):
                with open(os.path.join(self.evolution_dir, fname), "r") as f:
                    entry = json.load(f)
                    logs.append(entry)
        return sorted(logs, key=lambda x: x.get("timestamp", ""), reverse=True)

    def explain_code_change(self, mutation_id):
        path = os.path.join(self.evolution_dir, f"evolution_{mutation_id}.json")
        if not os.path.exists(path):
            return f"No log found for mutation {mutation_id}"
        with open(path, "r") as f:
            entry = json.load(f)
        reason = entry.get("reason", "No reason given.")
        summary = entry.get("summary", {})
        validation_log = entry.get("validation_log", "")
        return f"Reason: {reason}\nSummary: {summary}\nValidation: {validation_log}"

    def undo_last_mutation(self):
        logs = self.list_evolution_logs()
        if not logs:
            return "No mutations to undo."
        last = logs[0]
        backup_file = last.get('backup_file')
        target_file = last.get('target_file')
        if not backup_file or not target_file:
            return f"No backup/target info to undo mutation {last.get('mutation_id')}"
        try:
            with open(backup_file, 'r', encoding='utf-8') as bf:
                backup_content = bf.read()
            with open(target_file, 'w', encoding='utf-8') as tf:
                tf.write(backup_content)
            return f"Successfully reverted mutation {last.get('mutation_id')} on {target_file} using backup."
        except Exception as e:
            return f"Failed to undo mutation {last.get('mutation_id')}: {e}"

    def view_reasoning_chain(self, mutation_id):
        path = os.path.join(self.evolution_dir, f"evolution_{mutation_id}.json")
        if not os.path.exists(path):
            return f"No log found for mutation {mutation_id}"
        with open(path, "r") as f:
            entry = json.load(f)
        return entry.get("reasoning_chain", "No reasoning chain available.")

    def view_search_results(self):
        search_log_dir = os.path.join(self.logs_dir, "search_logs")
        if not os.path.exists(search_log_dir):
            return "No search logs found."
        results = []
        for fname in sorted(os.listdir(search_log_dir), reverse=True):
            if fname.endswith(".json"):
                try:
                    with open(os.path.join(search_log_dir, fname), 'r', encoding='utf-8') as f:
                        entry = json.load(f)
                        results.append({
                            'timestamp': entry.get('timestamp'),
                            'query': entry.get('query'),
                            'sources': entry.get('sources'),
                            'results': entry.get('results')[:3] if isinstance(entry.get('results'), list) else entry.get('results')
                        })
                except Exception as e:
                    results.append({'error': f'Failed to read {fname}: {e}'})
        if not results:
            return "No search results available."
        return results

# Example usage
if __name__ == "__main__":
    dash = UserDashboard()
    print("User settings:", dash.settings)
    print("Recent mutations:", dash.list_evolution_logs()[:2])
