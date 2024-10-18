from fastapi import APIRouter, UploadFile, File
from controllers.ocr_controller import process_ocr

router = APIRouter()

@router.post("/get_ocr_data")
async def upload_and_ocr(file: UploadFile = File(...)):
    return await process_ocr(file)
