import asyncio, os, time, aiohttp
import aiohttp
from pyrogram import filters
from blackpink import blackpink as bp
from AnonXMusic import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/Arthey_bot?startgroup=true"),
    ],
]

###
@app.on_message(filters.command("blackpink"))
async def blackpink(_, message):
    text = message.text[len("/blackpink") :]
    bp(f"{text}").save(f"blackpink_{message.from_user.id}.png", caption=f"❖ ʙʟᴀᴄᴋᴘɪɴɢ ʙʏ ~ 𝐀𝐫𝐭𝐡𝐞𝐲", reply_markup=InlineKeyboardMarkup(EVAA),)
    await message.reply_photo(f"blackpink_{message.from_user.id}.png", caption=f"❖ ʙʟᴀᴄᴋᴘɪɴɢ ʙʏ ~ 𝐀𝐫𝐭𝐡𝐞𝐲", reply_markup=InlineKeyboardMarkup(EVAA),)
    os.remove(f"blackpink_{message.from_user.id}.png")


####

@app.on_message(filters.command(["github", "git"]))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("❖ ➥ `/git tinaarobot`")
        return

    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'

    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("✦ ᴘʟᴇᴀsᴇ ᴘᴜᴛ ᴠᴀʟɪᴅ ɢɪᴛʜᴜʙ ᴜsᴇʀɴᴀᴍᴇ.")

            result = await request.json()

            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']

                caption = f"""ㅤㅤ❖ ɢɪᴛʜᴜʙ ɪɴғᴏ ᴏғ {name} ❖
                 
● ᴜsᴇʀɴᴀᴍᴇ ➥ {username}
● ʙɪᴏ ➥ {bio}
● ʟɪɴᴋ ➥ [Here]({url})
● ᴄᴏᴍᴩᴀɴʏ ➥ {company}
● ᴄʀᴇᴀᴛᴇᴅ ᴏɴ ➥ {created_at}
● ʀᴇᴩᴏsɪᴛᴏʀɪᴇs ➥ {repositories}
● ʙʟᴏɢ ➥ {blog}
● ʟᴏᴄᴀᴛɪᴏɴ ➥ {location}
● ғᴏʟʟᴏᴡᴇʀs ➥ {followers}
● ғᴏʟʟᴏᴡɪɴɢ ➥ {following}

❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ~ 𝐀𝐫𝐭𝐡𝐞𝐲"""

            except Exception as e:
                print(str(e))
                pass

    # Create an inline keyboard with a close button
    close_button = InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")
    inline_keyboard = InlineKeyboardMarkup([[close_button]])

    # Send the message with the inline keyboard
    await message.reply_photo(photo=avatar_url, caption=caption, reply_markup=inline_keyboard)

  
