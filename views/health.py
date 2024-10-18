from fastapi import APIRouter
from controllers.health_controller import health_check

router = APIRouter()

@router.get("/health")
async def health():
    return await health_check()
