from pyrogram import Client, filters
from faker import Faker
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/nykaaxbot?startgroup=true"),
    ],
]

# Create a Faker instance
fake = Faker()


# Generate person info command handler
@app.on_message(filters.command("rand"))
def generate_info(client, message):
    # Generate fake data
    name = fake.name()
    address = fake.address()
    country = fake.country()
    phone_number = fake.phone_number()
    email = fake.email()
    city = fake.city()
    state = fake.state()
    zipcode = fake.zipcode()

    # Create a message with the fake data
    info_message = (
        f"**๏ ғᴜʟʟ ɴᴀᴍᴇ ➠** {name}\n"
        
        f"**๏ ᴀᴅᴅʀᴇss ➠** {address}\n"
        
        f"**๏ ᴄᴏᴜɴᴛʀʏ ➠** {country}\n"
        
        f"**๏ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ➠** {phone_number}\n"
        
        f"**๏ ᴇᴍᴀɪʟ ➠** {email}\n"
        
        f"**๏ ᴄɪᴛʏ ➠** {city}\n"
        
        f"**๏ sᴛᴀᴛᴇ ➠** {state}\n"
        
        f"**๏ ᴢɪᴘᴄᴏᴅᴇ ➠** {zipcode}\n\n"

        f"✦ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠ ๛ɴ ʏ ᴋ ᴀ ᴀ ࿐"
    )
###
    
    message.reply_text(info_message, reply_markup=InlineKeyboardMarkup(EVAA),
    )

