import logging
import requests
from evolution_trigger import EvolutionTrigger

# Multi-Agent Hierarchy
from modules.multi_agent_hierarchy import (
    OrganizationDirector, ScienceManager, TechnologyManager, EngineeringManager, MathematicsManager,
    ArtsManager, HistoryManager, HealthManager, OperationsManager, FinanceManager, KnowledgeManager
)
# Additional agent managers
from agents.agent_science import ScienceAgent
from agents.agent_technology import TechnologyAgent
from agents.agent_engineering import EngineeringAgent
from agents.agent_mathematics import MathematicsAgent
from agents.agent_arts import ArtsAgent
from agents.agent_history import HistoryAgent
from agents.agent_economics import EconomicsAgent
from agents.agent_education import EducationAgent
from agents.agent_infrastructure import InfrastructureAgent
from agents.agent_health import HealthAgent
from agents.agent_operations import OperationsAgent
from agents.agent_finance import FinanceAgent
from agents.agent_knowledge import KnowledgeAgent
from data_ingestor import DataIngestor

# Additional agent managers
from agents.agent_economics import EconomicsAgent
from agents.agent_education import EducationAgent
from agents.agent_infrastructure import InfrastructureAgent

# Stage 5 AI Modules
from modules.goal_manager import GoalManager
from modules.memory_system import MemorySystem
from modules.resource_allocator import ResourceAllocator
from modules.perception import VisionPerception, AudioPerception, WebPerception
from modules.action_module import WebAction, APIAction
from modules.communication import CommunicationBus
from modules.explainability import ExplainabilityLayer
from modules.world_model import WorldModel

# Core AI & Modules
from core.chat_interface import ChatInterface
from modules.llm_manager import LLMManager
from modules.feedback_monitor import FeedbackMonitor
from modules.memory_module import MemoryModule
from modules.evolution_framework import EvolutionFramework
from interface.components.ui_renderer import UIRenderer
from sandbox.internet_bridge import InternetBridge

# Meta Layers
from meta.meta_reasoner import MetaReasoner
from meta.llm_metainterface import LLMMetainterface
from meta.emotion_meta import EmotionMeta
from meta.neuralcortex_scorer import NeuralCortexScorer

# Utility Modules


from utils.deep_apologies import DeepApologies
from utils.input_cleaner import InputCleaner
from utils.response_optim import ResponseOptimizer
from utils.memory_probe import MemoryProbe



from utils.sarcasm_detector import SarcasmDetector  # Sarcasm detection utility
from utils.logic_fallback import LogicFallback  # Logic fallback utility

class MindMapAI:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("MindMapAI")

        # Multi-Agent Organization
        self.organization = OrganizationDirector()
        # Stage 5 Modules (initialize first)
        self.memory_system = MemorySystem()
        self.explainability = ExplainabilityLayer()
        self.vision = VisionPerception()
        self.audio = AudioPerception()
        self.web_perception = WebPerception()
        self.web_action = WebAction()
        self.api_action = APIAction()
        self.comm_bus = CommunicationBus()
        self.world_model = WorldModel()

        # DataIngestor instance for all agents
        self.data_ingestor = DataIngestor()
        # Managers - inject dependencies at creation
        self.managers = {
            "science": ScienceAgent("ScienceAgent", data_ingestor=self.data_ingestor),
            "technology": TechnologyAgent("TechnologyAgent", data_ingestor=self.data_ingestor),
            "engineering": EngineeringAgent("EngineeringAgent", data_ingestor=self.data_ingestor),
            "mathematics": MathematicsAgent("MathematicsAgent", data_ingestor=self.data_ingestor),
            "arts": ArtsAgent("ArtsAgent", data_ingestor=self.data_ingestor),
            "history": HistoryAgent("HistoryAgent", data_ingestor=self.data_ingestor),
            "health": HealthAgent("HealthAgent", data_ingestor=self.data_ingestor),
            "operations": OperationsAgent("OperationsAgent", data_ingestor=self.data_ingestor),
            "finance": FinanceAgent("FinanceAgent", data_ingestor=self.data_ingestor),
            "knowledge": KnowledgeAgent("KnowledgeAgent", data_ingestor=self.data_ingestor),
            "economics": EconomicsAgent("EconomicsAgent", data_ingestor=self.data_ingestor),
            "education": EducationAgent("EducationAgent", data_ingestor=self.data_ingestor),
            "infrastructure": InfrastructureAgent("InfrastructureAgent", data_ingestor=self.data_ingestor),
        }
        for name, mgr in self.managers.items():
            mgr.comm_bus = self.comm_bus
            mgr.memory_system = self.memory_system
            mgr.perception = {
                "vision": self.vision,
                "audio": self.audio,
                "web": self.web_perception
            }
            mgr.world_model = self.world_model
            self.organization.register_manager(name, mgr)

        self.goal_manager = GoalManager(self.managers, memory_system=self.memory_system, explainability=self.explainability)
        self.resource_allocator = ResourceAllocator(self.managers)

        # Core Systems
        self.llm = LLMManager()
        self.chat = ChatInterface()
        self.feedback = FeedbackMonitor()
        self.memory = MemoryModule()
        self.bridge = InternetBridge()
        self.evolution = EvolutionFramework()
        self.ui = UIRenderer()


        # Meta + Analysis
        self.reasoner = MetaReasoner()
        self.reflector = LLMMetainterface()
        self.emotion = EmotionMeta()
        self.scorer = NeuralCortexScorer()

        # UX + Safety
        
        self.apologies = DeepApologies()
        self.cleaner = InputCleaner()
        self.rephraser = ResponseOptimizer()
        
        self.probe = MemoryProbe()
        self.sarcasm = SarcasmDetector()
        self.fallback = LogicFallback()

        # --- Automatic Evolution Trigger ---
        self.evolution_trigger = EvolutionTrigger(self, interval=120, alignment_threshold=0.5, memory_threshold=10)
        self.evolution_trigger.start()

    # Stage 5 AI hooks
    def submit_goal(self, description):
        goal_id = self.goal_manager.submit_goal(description)
        self.explainability.record("GoalManager", f"Submitted goal: {description}")
        return goal_id

    def remember_event(self, event, outcome, context=None):
        self.memory_system.remember_event(event, outcome, context)
        self.explainability.record("MemorySystem", f"Remembered event: {event}", context)

    def optimize_resources(self):
        self.resource_allocator.optimize()
        self.explainability.record("ResourceAllocator", "Optimized resources")

    def perceive_image(self, image_bytes):
        result = self.vision.analyze_image(image_bytes)
        self.explainability.record("VisionPerception", f"Analyzed image: {result}")
        return result

    def perceive_audio(self, audio_bytes):
        result = self.audio.analyze_audio(audio_bytes)
        self.explainability.record("AudioPerception", f"Analyzed audio: {result}")
        return result

    def perceive_web(self, url):
        result = self.web_perception.scrape_url(url)
        self.explainability.record("WebPerception", f"Scraped url: {url}")
        return result

    def act_web(self, url, message):
        result = self.web_action.post_message(url, message)
        self.explainability.record("WebAction", f"Posted message to {url}")
        return result

    def act_api(self, endpoint, data):
        result = self.api_action.call_api(endpoint, data)
        self.explainability.record("APIAction", f"Called API: {endpoint}")
        return result

    def send_message(self, sender, recipient, content):
        from modules.communication import Message
        msg = Message(sender, recipient, content)
        self.comm_bus.send(msg)
        self.explainability.record("CommunicationBus", f"Sent message from {sender} to {recipient}")

    def receive_messages(self, recipient):
        msgs = self.comm_bus.receive(recipient)
        self.explainability.record("CommunicationBus", f"{recipient} received messages", msgs)
        return msgs

    def explain_decisions(self, agent=None):
        return self.explainability.explain(agent)

    def simulate_world(self, scenario):
        result = self.world_model.simulate(scenario)
        self.explainability.record("WorldModel", f"Simulated scenario: {scenario}")
        return result

    # Full Stage 5 Demo: Autonomous Goal Cycle
    def demo_stage5_goal_cycle(self):
        # 1. Submit a high-level goal
        goal_id = self.submit_goal("Negotiate and analyze pandemic response using all modalities and learning.")
        subtasks = [
            "Negotiate resource allocation for pandemic analysis",
            "Use web perception to gather pandemic data",
            "Simulate possible future pandemic outcomes",
            "Learn from past pandemic events in memory"
        ]
        subgoal_ids = self.goal_manager.decompose_goal(goal_id, subtasks)
        assignment_map = {
            subgoal_ids[0]: "science",  # Negotiation
            subgoal_ids[1]: "technology",  # Perception
            subgoal_ids[2]: "health",  # World modeling
            subgoal_ids[3]: "science"  # Learning
        }
        # Actually run the cycle with advanced logic
        # Negotiation
        science_mgr = self.managers["science"]
        negotiation_result = science_mgr.negotiate("resource", {"request": "extra_workers", "reason": "urgent pandemic analysis"})
        self.explainability.record("Negotiation", f"Science manager negotiation result: {negotiation_result}")
        # Perception
        tech_mgr = self.managers["technology"]
        perception_result = tech_mgr.perceive("web", url="https://www.who.int/emergencies/diseases/novel-coronavirus-2019")
        self.explainability.record("Perception", f"Technology manager web perception result: {perception_result}")
        # World modeling
        health_mgr = self.managers["health"]
        simulation_result = health_mgr.reason_with_world_model({"event": "future pandemic scenario"})
        self.explainability.record("WorldModel", f"Health manager simulation result: {simulation_result}")
        # Learning
        learning_result = science_mgr.learn_from_memory("pandemic")
        self.explainability.record("Learning", f"Science manager learned from memory: {learning_result}")
        # Assign and execute subtasks
        self.goal_manager.assign_subtasks(goal_id, assignment_map)
        self.goal_manager.execute_subtasks(goal_id)
        # Feedback loop: managers adapt based on outcomes
        for mgr in self.managers.values():
            mgr.feedback_loop({
                "negotiation": negotiation_result,
                "perception": perception_result,
                "simulation": simulation_result,
                "learning": learning_result
            })
        goal = self.goal_manager.goals[goal_id]
        if all(self.goal_manager.goals[sid].status == "completed" for sid in goal.subtasks):
            self.goal_manager.update_status(goal_id, "completed", result="All advanced subtasks completed.")
        return self.goal_manager.get_goal_tree(goal_id)


    def run(self):
        self.logger.info("🧠 Booting MindMapAI System...")

        # Expose a function for all managers to learn
        import json
        import os
        import time
        def all_agents_learn():
            # Example: Using the LLM question generator
            # from llm_question_generator import generate_questions_with_llm
            # questions = generate_questions_with_llm(topic="Quantum Computing", context="", num_questions=5)
            # print(questions)
            print("[MindMapAI] Continuous learning mode for all agent managers (Ctrl+C to stop)...")
            cycle = 1
            try:
                while True:
                    print(f"\n--- Learning Cycle {cycle} ---")
                    world_state = {}
                    for name, mgr in self.managers.items():
                        try:
                            if hasattr(mgr, 'reason'):
                                print(f"[Learning] {name.title()}Agent is reasoning...")
                                mgr.reason(world_state=world_state)
                            elif hasattr(mgr, 'learn'):
                                print(f"[Learning] {name.title()}Agent is learning...")
                                mgr.learn(world_state=world_state)
                            else:
                                print(f"[Learning] {name.title()}Agent has no learning method.")
                        except Exception as e:
                            print(f"[Learning Error] {name.title()}Agent: {e}")
                    print(f"[Cycle Complete] Waiting before next cycle...")
                    time.sleep(10)  # adjust interval as needed
                    cycle += 1
            except KeyboardInterrupt:
                print("\n[MindMapAI] Continuous learning stopped by user.")
            logs = world_state.get("search_logs", [])
            summary = {}
            for entry in logs:
                agent = entry.get("agent", "Unknown")
                topic = entry.get("query", "")
                results = entry.get("results", [])
                if agent not in summary:
                    summary[agent] = []
                summary[agent].append({"topic": topic, "results": results})
            print("\n[Learning Summary]")

        def all_agents_evolve():
            print("[MindMapAI] Evolving all agents and subsystems via evolve_everything()...")
            try:
                from evolve import evolve_everything
                evolve_everything()
                print("[MindMapAI] All agents and subsystems evolved.")
            except Exception as e:
                print(f"[MindMapAI] Evolution failed: {e}")
            for agent, items in summary.items():
                print(f"{agent}: {len(items)} topics learned.")
                for item in items:
                    print(f"  - {item['topic']}")
                    # Optionally print results for each topic
                    for res in item['results']:
                        print(f"      > {res}")
            if not summary:
                print("No learning topics were recorded.")
            # (You can comment out the results printing block above if you want only topics/questions to be shown.)

            # Save the search_logs to a file
            try:
                log_path = os.path.join(os.getcwd(), "learning_log.json")
                with open(log_path, "w", encoding="utf-8") as f:
                    json.dump(logs, f, indent=2, ensure_ascii=False)
                print(f"\n[Learning Log] Saved to {log_path}")
            except Exception as e:
                print(f"[Learning Log Error] Could not save learning_log.json: {e}")
        self.chat.all_agents_learn = all_agents_learn
        self.chat.all_agents_evolve = all_agents_evolve

        try:
            print("✅ MindMapAI Booted Successfully")
            print(f"💬 Use chat or command interface to interact.\n")
            self.chat.start()

        except Exception as e:
            self.logger.error(f"❌ MindMapAI failed at runtime: {e}")
            raise

    def assign_org_task(self, manager_name, task, *args, **kwargs):
        """
        Assign a task to a subject manager in the organization.
        """
        return self.organization.assign_task(manager_name, task, *args, **kwargs)

    def summarize(self):
        """
        Returns a summary of key system metrics for API endpoints.
        """
        # Defensive: Use dummy values if attributes not present
        recent_activity = None
        feedback = None
        try:
            recent_activity = getattr(self.chat, 'last_message', None) if hasattr(self, 'chat') else None
        except Exception:
            recent_activity = None
        try:
            feedback = getattr(self.feedback, 'last_feedback', None) if hasattr(self, 'feedback') else None
        except Exception:
            feedback = None
        return {
            "recent_activity": recent_activity,
            "feedback": feedback
        }

if __name__ == "__main__":
    app = MindMapAI()
    app.run()
