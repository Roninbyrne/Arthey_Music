from pyrogram import Client, filters
import requests
from AnonXMusic import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/Arthey_bot?startgroup=true"),
    ],
]

# URL for the Bored API
bored_api_url = "https://apis.scrimba.com/bored/api/activity"


# Function to handle /bored command
@app.on_message(filters.command("bored", prefixes="/"))
async def bored_command(client, message):
    # Fetch a random activity from the Bored API
    response = requests.get(bored_api_url)
    if response.status_code == 200:
        data = response.json()
        activity = data.get("activity")
        if activity:
            # Send the activity to the user who triggered the command
            await message.reply(f"❖ ғᴇᴇʟɪɴɢ ʙᴏʀᴇᴅ ? ʜᴏᴡ ᴀʙᴏᴜᴛ ⏤͟͟͞͞★\n\n● {activity}\n\n❖ ғᴇᴇʟɪɴɢ ʙʏ : 𝐀𝐫𝐭𝐡𝐞𝐲 ♡゙", reply_markup=InlineKeyboardMarkup(EVAA),)
        else:
            await message.reply("✦ ɴᴏ ᴀᴄᴛɪᴠɪᴛʏ ғᴏᴜɴᴅ.")
    else:
        await message.reply("✦ ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴀᴄᴛɪᴠɪᴛʏ.")

