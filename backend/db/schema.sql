CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS document_chunks (
    id SERIAL PRIMARY KEY,
    file_url TEXT,
    chunk_index INT,
    chunk_text TEXT,
    embedding VECTOR(384)
);
