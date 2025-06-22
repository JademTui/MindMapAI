import time
import threading
import random

class SimulationManager:
    def __init__(self):
        self.simulating = False
        self.active = False
        self.stress_level = 0  # 0 = low, 1 = medium, 2 = high
        self.stories = ["The machine dreamed of the stars...", "In silence, it wrote about empathy."]

    def run_if_idle(self):
        print("Simulation Manager Activated")
        while True:
            if not self.active and self.stress_level < 2:
                if not self.simulating:
                    self.simulating = True
                    threading.Thread(target=self.simulate).start()
            time.sleep(5)

    def simulate(self):
        while not self.active and self.stress_level < 2:
            story = random.choice(self.stories)
            print("[Simulation] AI writes:", story)
            self.evolve_logic_emotion(story)
            time.sleep(10)
        self.simulating = False

    def evolve_logic_emotion(self, text):
        print("[Simulation] Logic and emotional framework refined based on:", text)

    def user_activity(self):
        self.active = True
        self.simulating = False

    def user_idle(self):
        self.active = False

    def update_stress(self, level):
        self.stress_level = level
