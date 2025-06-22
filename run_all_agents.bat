@echo off
start "Health Agent" python -m agents.run_health_agent
start "Technology Agent" python -m agents.run_technology_agent
start "Arts Agent" python -m agents.run_arts_agent
start "Finance Agent" python -m agents.run_finance_agent
start "Knowledge Agent" python -m agents.run_knowledge_agent
start "Infrastructure Agent" python -m agents.run_infrastructure_agent
