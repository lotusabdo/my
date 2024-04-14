import asyncio
from pyrogram import Client, filtersغ
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AbdoX import (Apple, Resso,Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["/help", "الاوامر"])
    
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/73299cc44862f1ec277dd.jpg",
caption=f"""[𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀](https://t.me/l2_2Y)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "عربي 🇪🇬", callback_data="arbic"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "English 🇺🇲", callback_data="english"),
                ],
            ]
        ),
    )


