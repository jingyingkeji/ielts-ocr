import requests
import pdfplumber
from fastapi import HTTPException


async def parse_pdf_from_url(pdf_url: str):
    try:
        # 下载PDF文件
        response = requests.get(pdf_url)
        response.raise_for_status()  # 检查请求是否成功

        # 使用pdfplumber解析PDF内容
        with pdfplumber.open(response.content) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"

        return {"content": text}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Error downloading PDF: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {e}")
