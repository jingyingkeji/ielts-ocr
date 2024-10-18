import os
import uuid
from fastapi import HTTPException, UploadFile

# 确保目录存在
os.makedirs("uploads/images", exist_ok=True)

async def save_uploaded_image(file: UploadFile):
    try:
        # 生成唯一的文件名
        file_extension = file.filename.split('.')[-1]
        file_name = f"{uuid.uuid4()}.{file_extension}"
        file_location = f"uploads/images/{file_name}"

        # 保存上传的文件
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

        return {"filename": file_name, "url": f"/ielts/uploads/images/{file_name}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {e}")
