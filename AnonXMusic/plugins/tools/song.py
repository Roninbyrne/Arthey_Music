import os
import future
import asyncio
import requests
import wget
import time
import yt_dlp
from urllib.parse import urlparse
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from AnonXMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch
from youtubesearchpython import SearchVideos




# ------------------------------------------------------------------------------- #

@app.on_message(filters.command("song"))
def download_song(_, message):
    query = " ".join(message.command[1:])  
    print(query)
    m = message.reply("💌")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

        # Add these lines to define views and channel_name
        views = results[0]["views"]
        channel_name = results[0]["channel"]

    except Exception as e:
        m.edit("⚠️ ɴᴏ ʀᴇsᴜʟᴛs ᴡᴇʀᴇ ғᴏᴜɴᴅ. ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜ ᴛʏᴘᴇᴅ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ sᴏɴɢ ɴᴀᴍᴇ.")
        print(str(e))
        return
    m.edit("📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("📤 ᴜᴘʟᴏᴀᴅɪɴɢ...")

        message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            caption=f"❖ {title}\n\n● ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ ➥ {message.from_user.mention}\n● ᴠɪᴇᴡs ➥ {views}\n● ᴄʜᴀɴɴᴇʟ ➥ {channel_name}\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ 𝐀 𝐫 𝐭 𝐡 𝐞 𝐲",
            duration=dur
        )
        m.delete()
    except Exception as e:
        m.edit(" - An error !!")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
        
        

# ------------------------------------------------------------------------------- #
