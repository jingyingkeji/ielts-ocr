import pdfplumber
from docx import Document
from fastapi import HTTPException


async def extract_text_from_pdf(file_stream):
    try:
        with pdfplumber.open(file_stream) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {e}")


async def extract_text_from_word(file_stream):
    try:
        doc = Document(file_stream)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing Word document: {e}")
