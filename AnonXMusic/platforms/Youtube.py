import asyncio
import os
import re
from typing import Union, Tuple, List
from googleapiclient.discovery import build
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from AnonXMusic.utils.formatters import time_to_seconds

# Initialize YouTube API client
API_KEY = "YOUR_API_KEY"
youtube = build("youtube", "v3", developerKey=API_KEY)

class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.status = "https://www.youtube.com/oembed?url="
        self.listbase = "https://youtube.com/playlist?list="
        self.reg = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    async def exists(self, link: str, videoid: Union[bool, str] = None) -> bool:
        if videoid:
            link = self.base + link
        return re.search(self.regex, link) is not None

    async def url(self, message_1: Message) -> Union[str, None]:
        messages = [message_1]
        if message_1.reply_to_message:
            messages.append(message_1.reply_to_message)
        for message in messages:
            if message.entities:
                for entity in message.entities:
                    if entity.type in [MessageEntityType.URL, MessageEntityType.TEXT_LINK]:
                        return message.text[entity.offset: entity.offset + entity.length]
        return None

    async def details(self, link: str) -> Tuple[str, str, int, str, str]:
        video_id = self.extract_video_id(link)
        video = youtube.videos().list(part="snippet,contentDetails", id=video_id).execute()
        result = video["items"][0]
        title = result["snippet"]["title"]
        duration_min = result["contentDetails"]["duration"]
        thumbnail = result["snippet"]["thumbnails"]["high"]["url"]
        vidid = result["id"]
        duration_sec = int(time_to_seconds(duration_min)) if duration_min != "None" else 0
        return title, duration_min, duration_sec, thumbnail, vidid

    async def title(self, link: str) -> str:
        video_id = self.extract_video_id(link)
        video = youtube.videos().list(part="snippet", id=video_id).execute()
        return video["items"][0]["snippet"]["title"]

    async def duration(self, link: str) -> str:
        video_id = self.extract_video_id(link)
        video = youtube.videos().list(part="contentDetails", id=video_id).execute()
        return video["items"][0]["contentDetails"]["duration"]

    async def thumbnail(self, link: str) -> str:
        video_id = self.extract_video_id(link)
        video = youtube.videos().list(part="snippet", id=video_id).execute()
        return video["items"][0]["snippet"]["thumbnails"]["high"]["url"]

    async def extract_video_id(self, link: str) -> str:
        match = re.search(r"v=([^&]+)", link)
        if match:
            return match.group(1)
        return link

    async def playlist(self, link: str, limit: int) -> List[str]:
        playlist_id = self.extract_playlist_id(link)
        request = youtube.playlistItems().list(part="contentDetails", playlistId=playlist_id, maxResults=limit)
        response = request.execute()
        return [item["contentDetails"]["videoId"] for item in response["items"]]

    async def track(self, link: str) -> Tuple[dict, str]:
        video_id = self.extract_video_id(link)
        video = youtube.videos().list(part="snippet", id=video_id).execute()
        result = video["items"][0]
        track_details = {
            "title": result["snippet"]["title"],
            "link": f"https://www.youtube.com/watch?v={video_id}",
            "vidid": video_id,
            "duration_min": result["contentDetails"]["duration"],
            "thumb": result["snippet"]["thumbnails"]["high"]["url"],
        }
        return track_details, video_id

    async def formats(self, link: str) -> Tuple[List[dict], str]:
        # Note: YouTube Data API does not provide detailed format info
        return [], link

    async def slider(self, link: str, query_type: int) -> Tuple[str, str, str, str]:
        # You can modify this based on your needs
        return "", "", "", ""

    async def download(
        self,
        link: str,
        mystic,
        video: Union[bool, str] = None,
        songaudio: Union[bool, str] = None,
        songvideo: Union[bool, str] = None,
        format_id: Union[bool, str] = None,
        title: Union[bool, str] = None,
    ) -> Tuple[str, bool]:
        # YouTube Data API does not handle downloads
        return "", False