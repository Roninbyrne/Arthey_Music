from pyrogram import Client, filters
import requests
from pyrogram.types import Message
from io import BytesIO
from AnonXMusic import app



def get_random_picture():
    response = requests.get('https://source.unsplash.com/random')
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        return None  # If something went wrong



@app.on_message(filters.command("wall"))
def pic(client, message):
    random_pic = get_random_picture()
    if random_pic:
        message.reply_photo(random_pic)
    else:
        message.reply("✦ Sorry, I couldn't get a random picture at the moment. 😔")



#____________________________

@app.on_message(filters.command("pic"))
def pic_command(client, message: Message):
    # Extract the name from the command
    try:
        name = message.command[1]
    except IndexError:
        client.send_message(message.chat.id, "✦ Please provide a name after the /pic command.")
        return

    # Build the Unsplash URL with the provided name
    unsplash_url = f"https://source.unsplash.com/500x500/?{name}"

    # Send the image as a photo
    try:
        response = requests.get(unsplash_url)
        if response.status_code == 200:
            client.send_photo(message.chat.id, photo=unsplash_url, caption=f"✦ ʜᴇʀᴇ's ᴀ ᴘɪᴄᴛᴜʀᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ➠ {name}.\n\n✦ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠ 𝐀 𝐫 𝐭 𝐡 𝐞 𝐲" )
        else:
            client.send_message(message.chat.id, "✦ Failed to fetch image.")
    except requests.RequestException as e:
        client.send_message(message.chat.id, f"✦ An error occurred ➠ {str(e)}")        
