import os
import uuid

from fastapi import HTTPException
from paddle import is_compiled_with_cuda
from paddleocr import PaddleOCR

# 检查是否支持GPU
use_gpu = is_compiled_with_cuda()

# 初始化 PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=use_gpu)

async def process_ocr(file):
    try:
        # 保存上传的文件
        file_location = f"uploads/raw/{uuid.uuid4()}.png"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

        # 进行OCR识别
        result = ocr.ocr(file_location)

        # 删除临时文件
        #os.remove(file_location)

        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
