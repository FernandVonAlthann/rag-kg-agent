from py2neo import Graph

def get_graph():
    return Graph("bolt://localhost:7687", auth=("neo4j", "password"))

def add_triplet(subject, predicate, obj):
    graph = get_graph()
    graph.run("MERGE (a:Entity {name: $s}) "
              "MERGE (b:Entity {name: $o}) "
              "MERGE (a)-[:RELATION {type: $p}]->(b)",
              s=subject, p=predicate, o=obj)
