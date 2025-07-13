episodic_memory = []

def store_event(event):
    episodic_memory.append(event)

def get_recent_events(n=5):
    return episodic_memory[-n:]
