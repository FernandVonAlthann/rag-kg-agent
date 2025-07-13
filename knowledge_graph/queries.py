from knowledge_graph.graph_db import get_graph

def query_knowledge_graph(term):
    graph = get_graph()
    result = graph.run("MATCH (e:Entity)-[r]->(t:Entity) "
                       "WHERE e.name CONTAINS $term "
                       "RETURN e.name, type(r), t.name", term=term)
    return list(result)
