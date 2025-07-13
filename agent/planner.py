def plan_task(query):
    if "summarize" in query:
        return ["retrieve_context", "summarize"]
    else:
        return ["retrieve_context"]
