# NPTEL Assistant

A FastAPI-based assistant for course PDFs.  
It supports:
- Uploading course PDF files
- Background ingestion into a vector database (pgvector)
- Question answering over ingested content using a RAG pipeline

## Tech Stack
- FastAPI + Uvicorn
- PostgreSQL + pgvector
- SQLAlchemy
- Sentence Transformers (embeddings)
- Supabase Storage (PDF hosting)
- Google Gemini (response generation)

## Prerequisites
- Python 3.11+
- Docker + Docker Compose (for containerized run)
- A `.env` file at project root with required keys

Required environment variables:
- `SUPABASE_URL`
- `SUPABASE_KEY`
- `BUCKET_NAME`
- `GEMINI_API_KEY`
- `PG_DATABASE_URL`

## Run Locally (Python)
From project root:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirments.txt
cd backend
uvicorn main:app --reload
```

Open:
- `http://127.0.0.1:8000`

## Run with Docker Compose
From project root:

```bash
docker compose up --build -d
```

This starts:
- App service on `http://127.0.0.1:8000`
- pgvector database on host port `5433`

Stop services:

```bash
docker compose down
```

## Notes
- In Docker Compose, `PG_DATABASE_URL` is overridden to use the `pgvector` service internally.
- Database schema/extension are initialized from `backend/db/schema.sql`.
- The app performs model initialization on startup, so first boot may take longer.
