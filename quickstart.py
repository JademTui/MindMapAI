"""
MindMapAI Quickstart: Minimal agentic AI for onboarding and demos.
Run this file for a one-file MindMapAI experience. Upgrade to full MindMapAI for advanced features.
"""
from modules.agent_plugin_system import AgentPluginSystem
from modules.user_dashboard import UserDashboard
from modules.onboarding import onboarding_wizard

if __name__ == "__main__":
    onboarding_wizard()
    dashboard = UserDashboard()
    agent_system = AgentPluginSystem()
    print("Available agents:", agent_system.list_agents())
    while True:
        cmd = input("MindMapAI> ")
        if cmd.lower() in ("exit", "quit"): break
        if cmd.startswith("agent:"):
            _, name, data = cmd.split(":", 2)
            result = agent_system.run_agent(name.strip(), data.strip())
            print(result)
        else:
            print("[Quickstart] Unknown command. Use 'agent:<name>:<data>' or 'exit'.")
