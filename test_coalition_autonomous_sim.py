"""
Test script to run 20 simulations of autonomous goal generation, coalition-building, and meta-reasoning in MindMapAI.
"""
from modules.multi_agent_hierarchy import OrganizationDirector, BaseManager
from modules.memory_system import MemorySystem
import random

class DummyManager(BaseManager):
    def __init__(self, subject):
        super().__init__(subject)
        self.subject = subject
    def __repr__(self):
        return f"DummyManager({self.subject})"

# Setup
subjects = [f"Agent{i}" for i in range(6)]
managers = {s: DummyManager(s) for s in subjects}
memory = MemorySystem()
director = OrganizationDirector()
for name, mgr in managers.items():
    director.register_manager(name, mgr)

def simulate_once(sim_id):
    # Autonomous goal generation (compound or atomic)
    goal = director.generate_autonomous_goal(world_state={"sim_id": sim_id})
    print(f"[Sim {sim_id}] Autonomous goal: {goal}")
    # Propose a coalition for the goal
    coalition_size = random.randint(2, 4)
    coalition_members = random.sample(list(managers.keys()), coalition_size)
    coalition_id = director.propose_coalition(coalition_members, purpose=f"Achieve {goal}")
    print(f"[Sim {sim_id}] Coalition {coalition_id} formed: {coalition_members}")
    # Assign roles and vote on a proposal
    coalition = director.coalition_manager.coalitions[coalition_id]
    coalition.assign_roles()
    proposal = f"pursue_{goal}"
    for m in coalition.members:
        coalition.vote(proposal, m, random.choice(["yes", "no", "abstain"]))
    print(f"[Sim {sim_id}] Coalition roles: {coalition.roles}")
    print(f"[Sim {sim_id}] Voting result: {coalition.voting_result(proposal)}")
    # Decompose goal (recursive, compound)
    subtasks = director.goal_generator.decompose_goal(goal)
    print(f"[Sim {sim_id}] Subtasks: {subtasks}")
    # Run coalition cycle (merging/splitting/competition)
    director.run_coalition_cycle()
    # Print all active coalitions
    active_coals = director.coalition_manager.get_active_coalitions()
    for c in active_coals:
        print(f"[Sim {sim_id}] Active coalition {c.id}: members={list(c.members)}, utility={c.utility:.2f}, roles={c.roles}")
    # Meta-reasoning (simulate logs, coalitions, goals)
    logs = [f"Sim {sim_id} log entry."]
    mods = director.meta_reasoner.analyze_performance(logs, memory, coalitions=active_coals, goals=[goal])
    print(f"[Sim {sim_id}] Meta-reasoning suggestions: {mods}")

if __name__ == "__main__":
    for i in range(1, 21):
        simulate_once(i)
