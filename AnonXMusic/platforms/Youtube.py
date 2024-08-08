import asyncio
import os
import re
from typing import Union, Tuple, List

import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from youtubesearchpython import VideosSearch

from AnonXMusic.utils.database import is_on_off
from AnonXMusic.utils.formatters import time_to_seconds


async def shell_cmd(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, errorz = await proc.communicate()
    if errorz:
        if "unavailable videos are hidden" in (errorz.decode("utf-8")).lower():
            return out.decode("utf-8")
        else:
            return errorz.decode("utf-8")
    return out.decode("utf-8")


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
        results = VideosSearch(link, limit=1)
        result = (await results.next())["result"][0]
        title = result["title"]
        duration_min = result["duration"]
        thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        vidid = result["id"]
        duration_sec = int(time_to_seconds(duration_min)) if duration_min != "None" else 0
        return title, duration_min, duration_sec, thumbnail, vidid

    async def title(self, link: str) -> str:
        results = VideosSearch(link, limit=1)
        result = (await results.next())["result"][0]
        return result["title"]

    async def duration(self, link: str) -> str:
        results = VideosSearch(link, limit=1)
        result = (await results.next())["result"][0]
        return result["duration"]

    async def thumbnail(self, link: str) -> str:
        results = VideosSearch(link, limit=1)
        result = (await results.next())["result"][0]
        return result["thumbnails"][0]["url"].split("?")[0]

    async def video(self, link: str) -> Tuple[int, str]:
        proc = await asyncio.create_subprocess_exec(
            "yt-dlp",
            "-g",
            "-f",
            "best[height<=?720][width<=?1280]",
            link,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        if stdout:
            return 1, stdout.decode().split("\n")[0]
        else:
            return 0, stderr.decode()

    async def playlist(self, link: str, limit: int) -> List[str]:
        playlist = await shell_cmd(
            f"yt-dlp -i --get-id --flat-playlist --playlist-end {limit} --skip-download {link}"
        )
        return [item for item in playlist.split("\n") if item]

    async def track(self, link: str) -> Tuple[dict, str]:
        results = VideosSearch(link, limit=1)
        result = (await results.next())["result"][0]
        track_details = {
            "title": result["title"],
            "link": result["link"],
            "vidid": result["id"],
            "duration_min": result["duration"],
            "thumb": result["thumbnails"][0]["url"].split("?")[0],
        }
        return track_details, result["id"]

    async def formats(self, link: str) -> Tuple[List[dict], str]:
        ydl_opts = {"quiet": True}
        ydl = yt_dlp.YoutubeDL(ydl_opts)
        with ydl:
            r = ydl.extract_info(link, download=False)
            formats_available = [
                {
                    "format": fmt["format"],
                    "filesize": fmt.get("filesize"),
                    "format_id": fmt["format_id"],
                    "ext": fmt["ext"],
                    "format_note": fmt.get("format_note"),
                    "yturl": link,
                }
                for fmt in r.get("formats", [])
                if "dash" not in fmt.get("format", "").lower()
            ]
        return formats_available, link

    async def slider(self, link: str, query_type: int) -> Tuple[str, str, str, str]:
        results = VideosSearch(link, limit=10)
        result = (await results.next())["result"][query_type]
        return (
            result["title"],
            result["duration"],
            result["thumbnails"][0]["url"].split("?")[0],
            result["id"]
        )

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
        if video:
            ydl_opts = {
                "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
                "outtmpl": "downloads/%(id)s.%(ext)s",
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
            }
        elif songaudio:
            ydl_opts = {
                "format": format_id,
                "outtmpl": f"downloads/{title}.%(ext)s",
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
                "prefer_ffmpeg": True,
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
            }
        elif songvideo:
            ydl_opts = {
                "format": f"{format_id}+140",
                "outtmpl": f"downloads/{title}",
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
                "prefer_ffmpeg": True,
                "merge_output_format": "mp4",
            }
        else:
            ydl_opts = {
                "format": "bestaudio[ext=m4a]",
                "outtmpl": "downloads/%(id)s.%(ext)s",
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
            }

        ydl = yt_dlp.YoutubeDL(ydl_opts)
        loop = asyncio.get_running_loop()

        def download_file():
            info = ydl.extract_info(link, download=True)
            return os.path.join("downloads", f"{info['id']}.{info['ext']}")

        downloaded_file = await loop.run_in_executor(None, download_file)
        return downloaded_file, True