# semantic_memory.py
"""
Semantic Memory module for MindMapAI
- Uses Chroma for persistent semantic storage and retrieval
- Uses FAISS for advanced batch similarity search and clustering
"""
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
import numpy as np

try:
    import faiss
except ImportError:
    faiss = None

class SemanticMemory:
    def __init__(self, persist_directory="semantic_memory"):
        self.client = chromadb.Client(Settings(persist_directory=persist_directory))
        self.embedder = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        self.collection = self.client.get_or_create_collection(
            "mindmapai_knowledge",
            embedding_function=self.embedder
        )

    def add_document(self, doc_id, text, metadata=None):
        # Ensure metadata is a non-empty dict for Chroma
        if not metadata:
            metadata = {'source': 'manual'}
        self.collection.add(
            ids=[doc_id],
            documents=[text],
            metadatas=[metadata]
        )

    def query(self, text, n_results=5):
        embedding = self.embedder([text])[0]
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results
        )
        return results

    def export_embeddings(self):
        # Export all embeddings and ids for FAISS use
        all = self.collection.get(include=["embeddings", "metadatas"])
        embeddings = all.get("embeddings", None)
        metadatas = all.get("metadatas", []) or []
        if embeddings is None:
            embeddings = []
        # Ensure embeddings is a numpy array before len()
        embeddings = np.array(embeddings, dtype=np.float32) if len(embeddings) > 0 else np.zeros((0, 384), dtype=np.float32)
        ids = [meta.get('id', str(i)) for i, meta in enumerate(metadatas)] if metadatas else [str(i) for i in range(len(embeddings))]
        if embeddings.shape[0] == 0 or len(ids) == 0:
            return np.zeros((0, 384), dtype=np.float32), []
        return embeddings, ids

    def faiss_knn_search(self, query_text, k=5):
        if faiss is None:
            raise ImportError("faiss is not installed. Please install faiss-cpu or faiss-gpu.")
        embeddings, ids = self.export_embeddings()
        if len(embeddings) == 0 or len(ids) == 0:
            return []
        dim = embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(embeddings.astype(np.float32))
        query_emb = self.embedder([query_text])[0].astype(np.float32).reshape(1, -1)
        print(f"[DEBUG] Query embedding shape: {query_emb.shape}")
        print(f"[DEBUG] FAISS index ntotal: {index.ntotal}")
        D, I = index.search(query_emb, k)
        print(f"[DEBUG] FAISS search D: {D}")
        print(f"[DEBUG] FAISS search I: {I}")
        # Return (id, distance) pairs
        return [(ids[i], float(D[0][j])) for j, i in enumerate(I[0])]

    def faiss_clustering(self, n_clusters=2):
        if faiss is None:
            raise ImportError("faiss is not installed. Please install faiss-cpu or faiss-gpu.")
        embeddings, ids = self.export_embeddings()
        if len(embeddings) == 0 or len(ids) == 0:
            return []
        dim = embeddings.shape[1]
        kmeans = faiss.Kmeans(dim, n_clusters, niter=20, verbose=False)
        kmeans.train(embeddings.astype(np.float32))
        D, I = kmeans.index.search(embeddings.astype(np.float32), 1)
        clusters = [[] for _ in range(n_clusters)]
        for idx, cluster_id in enumerate(I[:, 0]):
            clusters[cluster_id].append(ids[idx])
        return clusters

