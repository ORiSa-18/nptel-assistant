from db.supabse_client import supabase, SUPABASE_KEY, SUPABASE_URL
from fastapi import UploadFile
import os

BUCKET_NAME = os.getenv("BUCKET_NAME")

def upload_pdf(file: UploadFile):
    file_bytes = file.file.read()

    supabase.storage.from_(BUCKET_NAME).upload(
        path=file.filename,
        file=file_bytes,
        file_options={"content-type": "application/pdf"}
    )

    public_url = supabase.storage.from_(BUCKET_NAME).get_public_url(
        file.filename
    )
    
    return public_url
