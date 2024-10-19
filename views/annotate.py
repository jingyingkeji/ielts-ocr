import json

from fastapi import APIRouter, UploadFile, File, HTTPException, Form

from controllers.annotate_controller import process_annotation, process_url_annotation

router = APIRouter()


@router.post("/generate_image")
async def generate_image(file: UploadFile = File(...), annotations: str = Form(...)):
    try:
        # 解析 annotations 字符串为字典
        annotations_dict = json.loads(annotations)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON format for annotations")

    return await process_annotation(file, annotations_dict)


@router.post("/generate_url_image")
async def generate_url_image(image_url: str = Form(..., description="URL of the IMG"), annotations: str = Form(...)):
    try:
        # 解析 annotations 字符串为字典
        annotations_dict = json.loads(annotations)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON format for annotations")

    return await process_url_annotation(image_url, annotations_dict)
