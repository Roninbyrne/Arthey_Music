from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic import app
from config import OWNER_ID



@app.on_message(filters.video_chat_started)
async def brah(_, msg):
       await msg.reply("❖ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ sᴛᴀʀᴛᴇᴅ ᴏɴ ᴛʜɪs ɢʀᴏᴜᴘ.")


@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
       await msg.reply("**❖ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴇɴᴅᴇᴅ ᴏɴ ᴛʜɪs ɢʀᴏᴜᴘ.**")



@app.on_message(filters.video_chat_members_invited)
async def brah3(app :app, message:Message):
           text = f"❖ {message.from_user.mention} ɪɴᴠɪᴛᴇᴅ "
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f" [{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ᴛᴏ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ♥︎")
           except:
             pass


####

@app.on_message(filters.command("math", prefixes="/"))
def calculate_math(client, message):   
    expression = message.text.split("/math ", 1)[1]
    try:        
        result = eval(expression)
        response = f"❖ ᴛʜᴇ ʀᴇsᴜʟᴛ ɪs ➥ {result}"
    except:
        response = "❖ ɪɴᴠᴀʟɪᴅ ᴇxᴘʀᴇssɪᴏɴ"
    message.reply(response)

###
@app.on_message(filters.command("leavegroup")& filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = f"❖ ʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴛʜᴇ ɢʀᴏᴜᴘ."
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)

