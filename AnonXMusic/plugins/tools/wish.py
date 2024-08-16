from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
import requests
from AnonXMusic import app 

SUPPORT_CHAT = "The_friendz"

@app.on_message(filters.command("wish"))
async def wish(_, m):
    if len(m.command) < 2:
        await m.reply("๏ ᴀᴅᴅ ᴡɪꜱʜ ʙᴀʙʏ!")
        return 

    api = requests.get("https://nekos.best/api/v2/happy").json()
    url = api["results"][0]['url']
    text = m.text.split(None, 1)[1]
    wish_count = random.randint(1, 100)
    wish = f"❖ ʜᴇʏ {m.from_user.first_name}"
    wish += f"\n\n● ʏᴏᴜʀ ᴡɪꜱʜ ➥ {text} "
    wish += f"\n● ᴘᴏꜱꜱɪʙʟᴇ ᴛᴏ ➥ {wish_count}%"
    wish += f"\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ 𝐀 𝐫 𝐭 𝐡 𝐞 𝐲"
    
    await app.send_animation(
        chat_id=m.chat.id,
        animation=url,
        caption=wish,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}")]])
    )
            
    
BUTTON = [[InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}")]]
CUTIE = "https://64.media.tumblr.com/d701f53eb5681e87a957a547980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif"

@app.on_message(filters.command("cute"))
async def cute(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTE = f"❖ {mention} {mm}% ᴄᴜᴛᴇ ʙᴀʙʏ."

    await app.send_document(
        chat_id=message.chat.id,
        document=CUTIE,
        caption=CUTE,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )
    
