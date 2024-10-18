from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from views import document_router
from views import health_router
from views import ocr_router, annotate_router
from views import pdf_router
from views import upload_router

app = FastAPI()

# Include routers from views
app.include_router(health_router, prefix="/ielts")
app.include_router(ocr_router, prefix="/ielts/ocr", tags=["OCR"])
app.include_router(annotate_router, prefix="/ielts/annotate", tags=["Annotate"])
app.include_router(pdf_router, prefix="/ielts/pdf", tags=["PDF"])
app.include_router(document_router, prefix="/ielts/document", tags=["Document"])

app.include_router(upload_router, prefix="/ielts/upload", tags=["Images"])

app.mount("/ielts/uploads", StaticFiles(directory="uploads"), name="uploads")
