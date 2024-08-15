import random, os
from pyrogram import Client, filters, enums 
from AnonXMusic import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(filters.command(["genpassword", 'genpw']))
async def password(bot, update):
    message = await update.reply_text(text="✦ ᴘʀᴏᴄᴇꜱꜱɪɴɢ...")
    password = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+".lower()
    if len(update.command) > 1:
        qw = update.text.split(" ", 1)[1]
    else:
        ST = ["5", "7", "6", "9", "10", "12", "14", "8", "13"] 
        qw = random.choice(ST)
    limit = int(qw)
    random_value = "".join(random.sample(password, limit))
    txt = f"❖ <b>ʟɪᴍɪᴛ ➥</b> {str(limit)} \n\n● <b>ᴘᴀꜱꜱᴡᴏʀᴅ ➥ `<code>{random_value}</code>`\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ~ 𝐀𝐫𝐭𝐡𝐞𝐲"
    btn = InlineKeyboardMarkup([[InlineKeyboardButton(' ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ', url='https://t.me/Arthey_bot?startgroup=true')]])
    await message.edit_text(text=txt, reply_markup=btn, parse_mode=enums.ParseMode.HTML)

