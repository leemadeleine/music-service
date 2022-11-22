from fastapi import APIRouter

router = APIRouter(
    prefix="/simple",
)

@router.get('/happy')
async def get_happy():
    return {"mood": "Woo"}

@router.get('/sad')
async def get_sad():
    return {"mood": "Boo"}