from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from pgvector.sqlalchemy import Vector

Base = declarative_base()

class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id = Column(Integer, primary_key=True)
    file_url = Column(Text)
    chunk_index = Column(Integer)
    chunk_text = Column(Text)
    embedding = Column(Vector(384))
