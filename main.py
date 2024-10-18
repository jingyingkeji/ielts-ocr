from fastapi import FastAPI
from views import ocr_router, annotate_router

app = FastAPI()

# Include routers from views
app.include_router(ocr_router, prefix="/ocr", tags=["OCR"])
app.include_router(annotate_router, prefix="/annotate", tags=["Annotate"])
