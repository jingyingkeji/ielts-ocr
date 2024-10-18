from fastapi import HTTPException

async def health_check():
    try:
        return "health"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
