from agent.planner import plan_task
from agent.executor import execute_plan

def run_agent_loop(query, context, kg_result):
    plan = plan_task(query)
    results = execute_plan(plan, query)
    print("Agent output:", results)
    print("KG output:", kg_result)
