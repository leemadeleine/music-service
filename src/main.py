from fastapi import FastAPI
from src.routers import simple
from src.middleware import middleware


app = FastAPI(
    title="music-service",
    description="",
    version="1.0.0",
    contact={"name": "Client", "url": "http://localhost:3000"},
    middleware=middleware
)

app.include_router(simple.router)
