from sentence_transformers import SentenceTransformer
from typing import List

class Embedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
    
    def embed_chunks(self,
                     chunks: List[str]) -> List[str] :
        
        embeddings = self.model.encode(
            chunks,
            show_progress_bar = True,
            convert_to_numpy = True,
            normalize_embeddings = True
        )
        
        return embeddings.tolist()