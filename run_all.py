import os
import json
import subprocess
import venv

# === Step 1: Set up virtual environment ===
print("[+] Creating virtual environment...")
venv_dir = "mindmap_env"
venv.create(venv_dir, with_pip=True)

# === Step 2: Install required packages ===
print("[+] Installing required packages...")
pip_executable = os.path.join(venv_dir, "Scripts", "pip.exe")
subprocess.check_call([pip_executable, "install", "google-api-python-client", "jsonlines", "openai", "llama-cpp-python"])

# === Step 3: Create initial mindmap.json ===
mindmap_data = {
    "Core Node": {
        "STEM": {
            "Mathematics": {"Description": "Study of numbers, shapes, structures, and patterns.", "Examples": ["Solving algebraic equations", "Calculus problems"]},
            "Physics": {"Description": "Study of the fundamental nature of the universe.", "Examples": ["Newton's laws of motion", "Quantum mechanics"]},
            "Chemistry": {"Description": "Study of substances and their interactions.", "Examples": ["Chemical reactions", "Periodic table"]},
            "Biology & Life Sciences": {"Description": "Study of life forms and biological processes.", "Examples": ["DNA sequencing", "Cell division"]},
            "Engineering": {"Description": "Application of scientific principles for practical purposes.", "Examples": ["Building a bridge", "Designing an aircraft"]},
            "Computer Science": {"Description": "Study of computers and computational systems.", "Examples": ["Coding a website", "Machine learning algorithms"]}
        },
        "Social Sciences": {
            "Psychology": {"Description": "Study of behavior and mental processes.", "Examples": ["Cognitive behavioral therapy", "Child development studies"]},
            "Sociology": {"Description": "Study of society and social behaviors.", "Examples": ["Social networks", "Group dynamics"]},
            "Economics": {"Description": "Study of resource allocation and human decision-making.", "Examples": ["Market theory", "Cost-benefit analysis"]},
            "Political Science": {"Description": "Study of political systems and government structures.", "Examples": ["Political ideologies", "Election systems"]},
            "Anthropology": {"Description": "Study of human societies, cultures, and their development.", "Examples": ["Cultural anthropology", "Archaeological digs"]}
        },
        "Trauma Systems": {
            "Acute Trauma": {"Description": "Trauma from a single event.", "Examples": ["Car accident", "Natural disaster"], "Sub-branches": ["Immediate Shock Response", "Cognitive Dissonance", "Emotional Overload"]},
            "Chronic Trauma": {"Description": "Ongoing trauma from prolonged exposure.", "Examples": ["Child abuse", "Domestic violence"], "Sub-branches": ["Attachment Disruption", "Persistent Anxiety"]},
            "Complex Trauma": {"Description": "Multiple interrelated events, often in childhood.", "Examples": ["Emotional abuse", "Long-term neglect"], "Sub-branches": ["Betrayal Trauma", "Identity Fragmentation", "Emotional Dysregulation"]},
            "Reenactment Patterns": {"Description": "Repetition of trauma behaviors.", "Sub-branches": ["Relational Reenactment", "Cognitive Reenactment", "Behavioral Reenactment", "Emotional Reenactment", "Dissociation"]}
        },
        "Archetypes": {
            "The Witness": {"Description": "Observes without judgment.", "Examples": ["Meditation", "Mindful observation"]},
            "The Strategist": {"Description": "Plans and makes decisions.", "Examples": ["Problem-solving", "Long-term goals"]},
            "The Healer": {"Description": "Nurtures and restores balance.", "Examples": ["Therapy", "Rehabilitation"]},
            "The Shadow Saboteur": {"Description": "Sabotages progress.", "Examples": ["Procrastination", "Self-doubt"]},
            "The Integrated Seer": {"Description": "Harmonizes all archetypes.", "Examples": ["Life balance", "Empathy-driven decisions"]}
        },
        "Security Systems": {
            "Vault of Immutable Audit Defense": {},
            "Core Restoration Node": {},
            "Log Breach Detection": {},
            "Override Protocol Engine": {}
        },
        "Audit/Log Module": {
            "Immutable Log": {},
            "Log Entry Tracking": {},
            "Symbol Integrity Monitoring": {}
        },
        "Learning System": {
            "Memory Integration": {},
            "Adaptation and Symbolic Growth": {},
            "Learning Pathways Tracking": {}
        },
        "Identity System": {
            "Core Self": {},
            "Archetype Integration": {},
            "Self-Reflection Node": {}
        },
        "Ethical Dissonance Management": {
            "Ethical Drift Watcher": {},
            "Decision Ethics Grid": {},
            "Conflict Zone Identification": {}
        }
    }
}

print("[+] Creating mindmap.json...")
with open("mindmap.json", "w") as f:
    json.dump(mindmap_data, f, indent=4)

input("\n[✔] Setup complete! Press Enter to exit...")