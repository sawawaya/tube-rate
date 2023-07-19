from pydantic import BaseModel

class MostViewedVideo(BaseModel):
    most_viewed_video_url: str
    view_count: int
    like_count: int