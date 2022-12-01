from fastapi import APIRouter
from src.services.spotify import SpotifyService

router = APIRouter()


@router.get("/recommendations")
async def get_recos(token: str = None, mood: str = None):
    """
    get recommendations based on mood argument
    """
    spotify_service = SpotifyService(None, token)
    return {"data": spotify_service.get_recommendations(mood)}
