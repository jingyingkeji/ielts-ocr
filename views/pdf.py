from fastapi import APIRouter, HTTPException
from controllers.pdf_controller import parse_pdf_from_url

router = APIRouter()

@router.post("/parse-pdf/")
async def parse_pdf(url: str):
    if not url:
        raise HTTPException(status_code=400, detail="PDF URL is required")
    return await parse_pdf_from_url(url)
