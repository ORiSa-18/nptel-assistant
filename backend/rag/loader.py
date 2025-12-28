import requests
import pdfplumber
import io

def load_pdf(file_url: str):
    
    response = requests.get(file_url)
    response.raise_for_status()
    
    pdf_bytes = io.BytesIO(response.content)
    
    content = []
    
    with pdfplumber.open(pdf_bytes) as pdf:
        for page_number, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                content.append(text)
                
    full_content = "\n\n".join(content)
    
    return full_content
    