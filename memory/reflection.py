from memory.episodic import get_recent_events

def summarize_recent_events():
    events = get_recent_events()
    return "Summary: " + ", ".join(events)
