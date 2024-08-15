from pyrogram import Client, filters
from pyrogram.types import Message
import qrcode
from AnonXMusic import app
from PIL import Image
import io
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/@Arthey_bot?startgroup=true"),
    ],
]


# Function to create a QR code
def generate_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="white", back_color="green")

    # Save the QR code to a bytes object to send with Pyrogram
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)  # Go to the start of the bytes object

    return img_bytes


@app.on_message(filters.command("qr"))
def qr_handler(client, message: Message):
    # Extracting the text passed after the command
    command_text = message.command
    if len(command_text) > 1:
        input_text = " ".join(command_text[1:])
        qr_image = generate_qr_code(input_text)
        message.reply_photo(qr_image, caption="✦ ǫʀ ᴄᴏᴅᴇ sᴜᴄᴄᴇssғᴜʟʟʏ ɢᴇɴʀsᴛᴇᴅ ✦\n\n๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠ 𝐀𝐫𝐭𝐡𝐞𝐲 ", reply_markup=InlineKeyboardMarkup(EVAA),)

    else:
        message.reply_text("✦ Please provide the text for the QR code after the command. Example usage ➠ /qr text")
      
