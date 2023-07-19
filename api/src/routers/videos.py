import logging
import typing as Optional

from fastapi import APIRouter, Depends, HTTPException

from src.schemas import MostViewedVideo
from src.repository.youtube_api import YoutubeAPI

logger = logging.getLogger("uvcorn")
router = APIRouter(
    prefix="/video",
    tags=["video"],
)

@router.get('/', status_code=200, response_model=MostViewedVideo)
def most_viewed_videos(video_url: str):
    youtube_api = YoutubeAPI()
    channel_id = youtube_api.get_channel_url_from_video_url(video_url)
    most_viewed_video_id = youtube_api.get_most_viewed_video_id_in_channel(channel_id)
    view_count, like_count = youtube_api.get_viwe_count_and_like_count(most_viewed_video_id)

    most_viewed_video = MostViewedVideo(
        most_viewed_video_url=f"https://www.youtube.com/watch?v={most_viewed_video_id}",
        view_count=view_count,
        like_count=like_count,
    )
    return most_viewed_video
