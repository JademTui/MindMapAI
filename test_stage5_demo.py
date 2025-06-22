from mindmap_ai import MindMapAI

if __name__ == "__main__":
    app = MindMapAI()
    print("\n--- Stage 5 AI Autonomous Goal Cycle Demo ---\n")
    goal_tree = app.demo_stage5_goal_cycle()
    print("\n[Goal Execution Tree]:\n", goal_tree)
    print("\n[Explainability Log]:\n", app.explain_decisions())
    print("\n[Episodic Memory]:\n", app.memory_system.recall_events())
