from retrieval.retriever import retrieve
from memory.reflection import summarize_recent_events

def execute_plan(plan, query):
    output = []
    for step in plan:
        if step == "retrieve_context":
            output.append(retrieve(query))
        elif step == "summarize":
            output.append(summarize_recent_events())
    return output
