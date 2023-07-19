import os
import re

from apiclient.discovery import build
from fastapi import HTTPException, status

DEVELOPER_KEY = os.environ.get("DEVELOPER_KEY")

class YoutubeAPI():
    def __init__(self) -> None:
        self.youtube = build("youtube", "v3", developerKey=DEVELOPER_KEY)

    def get_channel_url_from_video_url(self, url):
        video_pattern = r"^(https?://)?(www\.)?youtube\.com/watch\?v=[\w-]+$"
        is_video_url =  re.match(video_pattern, url)
        if not is_video_url:
            raise Exception(f"Please set a video url(Invalid URL:{url })")
        video_id = url.split("/")[-1].split("=")[1]
        video_response = self.youtube.videos().list(
            part="snippet",
            id=video_id
        ).execute()
        channel_id = video_response["items"][0]["snippet"]["channelId"]
        return channel_id

    def get_most_viewed_video_id_in_channel(self, channel_id):
        videos_response = self.youtube.search().list(
            part="snippet",
            channelId=channel_id,
            order="viewCount",
            type="video",
        ).execute()
        video_id = videos_response["items"][0]["id"]["videoId"]
        return video_id


    def get_viwe_count_and_like_count(self, video_id):
        video_response = self.youtube.videos().list(
            part="statistics",
            id=video_id,
        ).execute()
        view_count = int(video_response["items"][0]['statistics']["viewCount"])
        like_count = int(video_response["items"][0]['statistics']["likeCount"])
        return view_count, like_count