semantic_facts = {}

def store_fact(key, value):
    semantic_facts[key] = value

def recall_fact(key):
    return semantic_facts.get(key, "Unknown")
