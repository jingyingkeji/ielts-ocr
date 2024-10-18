from fastapi import APIRouter, UploadFile, File, Form
from controllers.ocr_controller import process_ocr, process_url_ocr

router = APIRouter()


@router.post("/get_ocr_data")
async def get_ocr_data(file: UploadFile = File(...)):
    return await process_ocr(file)


@router.post("/get_url_ocr_data")
async def get_url_ocr_data(image_url: str = Form(..., description="URL of the IMG")):
    return await process_url_ocr(image_url)
