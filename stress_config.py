
# stress_config.py
MODES = {
    "idle": {"cpu_limit": 30, "mem_limit": 300},
    "chat": {"cpu_limit": 60, "mem_limit": 600},
    "max_stress": {"cpu_limit": 95, "mem_limit": 1024}
}
CURRENT_MODE = "chat"
