from pyrogram import Client, filters
from AnonXMusic import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/?startgroup=true"),
    ],
]

@app.on_message(filters.command("weather"))
def weather(client, message):
    try:
        # Get the location from user message
        user_input = message.command[1]
        location = user_input.strip()
        weather_url = f"https://wttr.in/{location}.png"
        
        # Reply with the weather information as a photo
        message.reply_photo(photo=weather_url, caption="✦ ʜᴇʀᴇ's ᴛʜᴇ ᴡᴇᴀᴛʜᴇʀ ғᴏʀ ʏᴏᴜʀ ʟᴏᴄᴀᴛɪᴏɴ.\n\n๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠ 𝐀𝐫𝐭𝐡𝐞𝐲", reply_markup=InlineKeyboardMarkup(EVAA),)
    except IndexError:
        # User didn't provide a location
        message.reply_text("✦ Please provide a location. ♥︎ Use /weather NEW YORK")
      
