import os
import uuid
import requests
import wget

from fastapi import HTTPException
from paddle import is_compiled_with_cuda
from paddleocr import PaddleOCR

# 检查是否支持GPU
use_gpu = is_compiled_with_cuda()

# 初始化 PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=use_gpu)

os.makedirs("uploads/raw", exist_ok=True)


async def process_url_ocr(image_url: str):
    try:
        # Generate a unique file path
        file_location = f"uploads/raw/{uuid.uuid4()}.png"

        # Download the image using requests
        response = requests.get(image_url, verify=False)
        with open(file_location, 'wb') as f:
            f.write(response.content)
        print(f"Image successfully downloaded to {file_location}")

        # Perform OCR on the saved image
        result = ocr.ocr(file_location)

        # Optionally delete the temporary file
        os.remove(file_location)

        return {"result": result}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Error downloading image: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def process_ocr(file):
    try:
        # 保存上传的文件
        file_location = f"uploads/raw/{uuid.uuid4()}.png"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

        # 进行OCR识别
        result = ocr.ocr(file_location)

        # 删除临时文件
        # os.remove(file_location)

        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
