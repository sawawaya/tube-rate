import os

from fastapi import FastAPI
from src.routers import videos
import uvicorn

app = FastAPI()

app.include_router(videos.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", timeout_keep_alive=180)