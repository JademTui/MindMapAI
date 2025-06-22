# test_semantic_memory.py
import shutil
import tempfile
from semantic_memory import SemanticMemory

# Sample documents
knowledge = [
    ("doc1", "The Eiffel Tower is located in Paris, France."),
    ("doc2", "Mount Everest is the highest mountain in the world."),
    ("doc3", "Python is a popular programming language for AI and data science."),
    ("doc4", "The Great Wall of China is visible from space."),
    ("doc5", "Paris is known as the city of lights.")
]

# Force a fresh Chroma DB for testing
def setup_memory():
    knowledge = [
        ("doc1", "The Eiffel Tower is located in Paris, France."),
        ("doc2", "Mount Everest is the highest mountain in the world."),
        ("doc3", "Python is a popular programming language for AI and data science."),
        ("doc4", "The Great Wall of China is visible from space."),
        ("doc5", "Paris is known as the city of lights.")
    ]
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        memory = SemanticMemory(persist_directory=tmpdir)
        for doc_id, text in knowledge:
            memory.add_document(doc_id, text)
        yield memory

def test_query_semantic_memory():
    for memory in setup_memory():
        results = memory.query("What city has the Eiffel Tower?", n_results=3)
        assert results is not None
        assert 'documents' in results
        assert any("Paris" in doc for doc in results['documents'][0])

def test_export_embeddings():
    for memory in setup_memory():
        embeddings, ids = memory.export_embeddings()
        assert len(embeddings) > 0
        assert embeddings.shape[1] == 384
        assert len(ids) > 0

try:
    results = memory.faiss_knn_search("famous towers in France", k=3)
    if not results:
        print("No FAISS results found.")
    else:
        for doc_id, score in results:
            print(f"Doc: {doc_id}, Score: {score}")
except Exception as e:
    print("FAISS search failed:", e)

# FAISS clustering
print("\n--- FAISS Clustering (2 clusters) ---")
try:
    clusters = memory.faiss_clustering(n_clusters=2)
    if isinstance(clusters, dict):
        for cluster_id, doc_ids in clusters.items():
            print(f"Cluster {cluster_id}: {doc_ids}")
    elif isinstance(clusters, list):
        for idx, doc_ids in enumerate(clusters):
            print(f"Cluster {idx}: {doc_ids}")
    else:
        print(clusters)
except Exception as e:
    print("FAISS clustering failed:", e)
