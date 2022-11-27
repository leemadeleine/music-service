from fastapi import APIRouter
from src.services.spotify import SpotifyService

router = APIRouter(
    prefix="/auth",
)


@router.get("/credentials")
async def get_spotify_credentials(code: str = None):
    """
    return client_id and client_secret for spotify app
    """
    spotify_service = SpotifyService(code, None)
    return spotify_service.get_credentials()


@router.get("/token")
async def get_spotify_token(code: str = None):
    """
    return auth token
    """
    spotify_service = SpotifyService(code, None)
    return spotify_service.get_token()
