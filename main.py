from retrieval.retriever import retrieve
# from knowledge_graph.queries import query_knowledge_graph  # DISABLED FOR NOW
from agent.agent_loop import run_agent_loop

def mock_kg(query):
    # Fake KG result for now
    return [("John Doe", "did", "something important")]

def main():
    print("Starting RAG-KG-Agent system...")
    query = "What did John Doe do last week?"
    
    # Step 1: RAG retrieve
    context = retrieve(query)

    # Step 2: Mock KG
    kg_response = mock_kg(query)

    # Step 3: Run agent loop
    run_agent_loop(query, context, kg_response)

if __name__ == "__main__":
    main()
