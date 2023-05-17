from fastapi import APIRouter

router = APIRouter()

@router.get("/watches")
async def get_watches():
    return "Hello"