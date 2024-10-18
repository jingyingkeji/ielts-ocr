from io import BytesIO

from fastapi import APIRouter, HTTPException, Form
from controllers.document_controller import extract_text_from_pdf, extract_text_from_word
import requests
from mimetypes import guess_type

router = APIRouter()


@router.post("/parse")
async def parse_document(resume_url: str = Form(..., description="URL of the PDF or Word document")):
    try:
        print("------------")
        print(resume_url)
        # 下载文件
        response = requests.get(resume_url)

        response.raise_for_status()  # 检查请求是否成功
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Error downloading file: {e}")

    # 获取文件MIME类型
    mime_type, _ = guess_type(resume_url)

    if mime_type == 'application/pdf':
        content = await extract_text_from_pdf(BytesIO(response.content))
    elif mime_type in ['application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/msword']:
        content = await extract_text_from_word(BytesIO(response.content))
    else:
        raise HTTPException(status_code=400,
                            detail="Unsupported file type. Please provide a URL to a PDF or Word document.")

    return {"content": content}
