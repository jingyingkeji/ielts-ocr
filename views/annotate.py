from fastapi import APIRouter, UploadFile, File, HTTPException
from controllers.annotate_controller import process_annotation

router = APIRouter()

@router.post("/annotate-image/")
async def annotate_image(file: UploadFile = File(...), annotations: dict = None):
    if annotations is None:
        raise HTTPException(status_code=400, detail="Annotations are required")
    return await process_annotation(file, annotations)
