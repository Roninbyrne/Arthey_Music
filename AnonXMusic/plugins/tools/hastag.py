import requests
from bs4 import BeautifulSoup as  BSP
from AnonXMusic import app as roy
from pyrogram import filters

url = "https://all-hashtag.com/library/contents/ajax_generator.php"

@roy.on_message(filters.command("hastag"))
async def hastag(bot, message):
    global content
    try:
        text = message.text.split(' ',1)[1]
        data = dict(keyword=text, filter="top")

        res = requests.post(url, data).text

        content = BSP(res, 'html.parser').find("div", {"class":"copy-hashtags"}).string
    except IndexError:
        return await message.reply_text("✦ Example ➠ /hastag python")
        
    
    await message.reply_text(f"✦ ʜᴇʀᴇ ɪs ʏᴏᴜʀ  ʜᴀsᴛᴀɢ ➠\n\n<pre>{content}</pre>", quote=True)
    
