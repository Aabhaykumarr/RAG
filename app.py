from src.rag.search import RAGSearch

# Example usage
if __name__ == "__main__":
    print("[INFO] Starting application...")
    
    # RAGSearch automatically handles loading or building the vector store!
    rag_search = RAGSearch()
    
    query = "What is attention mechanism?"
    print(f"[INFO] Querying: {query}")
    
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("\nSummary:\n", summary)