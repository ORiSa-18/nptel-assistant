from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import text

from db.db_connection import SessionLocal
from db.db_models import DocumentChunk
from rag.embedder import Embedder

class PGVectorRetreiver:
    def __init__(self) -> None:
        self.embedder = Embedder()
        
    def store_chunks(self,
                     file_url: str,
                     chunks: List[str],
                     embeddings: List[str]
    ):
        session : Session = SessionLocal()
        
        try:
            for idx, (chunk, embedding) in enumerate(zip(chunks,embeddings)):
                record = DocumentChunk(
                    file_url = file_url,
                    chunk_index = idx,
                    chunk_text = chunk,
                    embedding = embedding
                ) 
                session.add(record)
            session.commit()
        finally:
            session.close()
    
    def retreiver(self,
                  query: str,
                  top_k: int = 5) -> List[str]:
        session: Session = SessionLocal()
        
        try:
            query_embedding = self.embedder.embed_chunks([query])[0]
            
            sql = text("""
                    SELECT chunk_text
                    FROM document_chunks
                    ORDER BY embedding <=> (:query_embedding)::vector
                    LIMIT :top_k
                    """)
            
            
            
            results =  session.execute(
                sql,
                {
                    "query_embedding": query_embedding,
                    "top_k": top_k 
                }
            ).fetchall()
            
            return [row[0] for row in results]
        
        finally:
            session.close()