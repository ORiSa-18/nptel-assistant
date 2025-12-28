from rag.loader import load_pdf
from rag.chunker import chunk_text
from rag.embedder import Embedder
from rag.retreiver import PGVectorRetreiver

embedder = Embedder()
retreiver = PGVectorRetreiver()

def ingest_document(file_url: str):
    
    print(f"[INGESTION] Starting ingestion for: {file_url}")
    
    text = load_pdf(file_url)
    
    if not text or not text.strip():
        raise ValueError("No text extracted from PDF")
    
    chunks = chunk_text(text)
    
    if not chunks:
        raise ValueError("No chunks created from the document")
    
    embeddings = embedder.embed_chunks(chunks)
    
    retreiver.store_chunks(
        file_url=file_url,
        chunks=chunks,
        embeddings=embeddings
    )
    
    print(f"[INGESTION] Completed ingestion for: {file_url}")
    