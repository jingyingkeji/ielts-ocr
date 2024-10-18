from fastapi import APIRouter, UploadFile, File, HTTPException
from controllers.uploads_controller import save_uploaded_image

router = APIRouter()

@router.post("/image/")
async def upload_image(file: UploadFile = File(...)):
    if file.content_type not in ['image/jpeg', 'image/jpeg', 'image/png', 'image/gif']:
        raise HTTPException(status_code=400, detail="Unsupported file type. Please upload an image file.")
    return await save_uploaded_image(file)
