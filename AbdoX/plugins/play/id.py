import asyncio
from pyrogram import Client, filters
from AbdoX import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    command(["ايدي","id","ا"])
    & filters.group
    
)
async def iddd(client, message):
    if message.chat.id in iddof:
      return
 caption=f""" - ꪀᥲ️︎ꪔᥱ︎ :{message.from_user.mention}\n- u᥉ᥱ︎ɾ :@{message.from_user.username}\n- Ꭵძ . :`{message.from_user.id}`\nႦᎥ᥆ :{usr.bio}\nᥴ𝗁ᥲ️ƚ: {message.chat.title}\n𝚒𝚍 𝚐𝚛𝚘𝚞𝚋 :`{message.chat.id}`""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )




