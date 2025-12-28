from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text 
from db.db_connection import engine

from rag.pipeline import run_rag
from rag.ingestion import ingest_document
from services.upload_service import upload_pdf

app = FastAPI()


templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str
    
# ONLY for updating schema
# @app.on_event("startup")
# def run_schema():
#     with engine.begin() as conn:
#         with open("db/schema.sql","r") as file:
#             conn.execute(text(file.read()))

@app.get("/", response_class=HTMLResponse)
async def serve_frontend(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/chat", response_model = ChatResponse)
def chat(req: ChatRequest):
    answer = run_rag(req.query)
    return {"answer": answer}

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = BackgroundTasks()
):
    
    public_url = upload_pdf(file)
    
    background_tasks.add_task(
        ingest_document,
        public_url
    )
    
    return {
        "status": "OK",
        "message": "File uploaded succesfully. Ingestion started.",
        "file_url": public_url
    }