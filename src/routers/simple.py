from fastapi import APIRouter
from src.services.spotify import SpotifyService

router = APIRouter(
    prefix="/simple",
)


@router.get("/happy")
async def get_happy():
    """
    Return spotify uri id matching a happy playlist
    """
    spotify_service = SpotifyService()
    return {"uri": spotify_service.get_my_playlists("Happy Music")}


@router.get("/sad")
async def get_sad():
    """
    Return spotify uri id matching a sad playlist
    """
    spotify_service = SpotifyService()
    return {"uri": spotify_service.get_my_playlists("Sad Music")}
