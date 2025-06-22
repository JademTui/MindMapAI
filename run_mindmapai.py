# run_mindmapai.py
"""
Entry point for MindMapAI: initializes all modules, agents, and runs the main loop.
"""
from core.semantic_memory import SemanticMemory
from core.reasoning_engine import ReasoningEngine
from core.self_improvement_engine import SelfImprovementEngine
from core.world_model import WorldModel
from core.data_ingestion import DataIngestion

from agents.agent_economics import EconomicsAgent
from agents.agent_health import HealthAgent
from agents.agent_education import EducationAgent
from agents.agent_infrastructure import InfrastructureAgent

from interface.dashboard import Dashboard
from interface.api import MindMapAIApi
from interface.explainability import Explainability


def main():
    # Initialize core modules
    memory = SemanticMemory()
    world_model = WorldModel()
    self_improver = SelfImprovementEngine(codebase_path=".", test_suite="tests/")
    data_ingestor = DataIngestion()

    # Fetch real-world data and update world model
    gdp_data = data_ingestor.fetch_worldbank_gdp(country_code="NZL", year="2022")
    covid_data = data_ingestor.fetch_covid_cases(country_slug="new-zealand")
    world_model.state.update({"gdp": gdp_data, "covid": covid_data})

    # Initialize agents
    agents = [
        EconomicsAgent("Economics", data_ingestor=data_ingestor),
        HealthAgent("Health"),
        EducationAgent("Education"),
        InfrastructureAgent("Infrastructure")
    ]

    # Initialize reasoning engine
    reasoner = ReasoningEngine(memory, agents)

    # Initialize interfaces
    dashboard = Dashboard()
    api = MindMapAIApi()
    explain = Explainability()

    # Example main loop (placeholder)
    world_state = world_model.state
    while True:
        reasoner.step(world_state)
        dashboard.display(world_state)
        self_improver.feedback_loop()  # Evolution and self-coding enabled

if __name__ == "__main__":
    main()
