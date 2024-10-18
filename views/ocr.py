from fastapi import APIRouter, UploadFile, File
from controllers.ocr_controller import process_ocr

router = APIRouter()

@router.post("/upload-and-ocr/")
async def upload_and_ocr(file: UploadFile = File(...)):
    return await process_ocr(file)
