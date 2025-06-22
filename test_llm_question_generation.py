from agents.agent_engineering import EngineeringAgent

if __name__ == "__main__":
    agent = EngineeringAgent("EngineeringAgent")
    # Minimal world state
    world_state = {}
    # Call reason to trigger LLM-based question generation
    agent.reason(world_state)
    # Print out the learning queue after LLM generation
    print("Learning queue (post-LLM generation):")
    print(agent.learning_queue)
