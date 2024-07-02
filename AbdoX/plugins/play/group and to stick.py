
import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from MazenMusic import (Apple, Resso, Spotify, Telegram, YouTube, app)
from MazenMusic import app
from asyncio import gather

@app.on_message(
    filters.command(["بايو","البايو"], "")
    & filters.group
    & filters.group
)
async def biio(client, message):
  nq = await client.get_chat(message.from_user.id)
  bio = nq.bio
  await message.reply_text(bio
  )
 
 
 

@app.on_message(filters.command(["الجروب", "جروب"], "") & filters.group)
async def ginnj(client: Client, message: Message):
    chat_idd = message.chat.id
    chat_name = message.chat.title
    chat_username = f"@{message.chat.username}"
    photo = await client.download_media(message.chat.photo.big_file_id)
    await message.reply_photo(photo=photo, caption=f"""⌯ اسم الجروب : {chat_name} 🍀 ⋅\n⌯ ايدي الجروب : {chat_idd} 🍀 ⋅\n⌯ رابط الجروب : {chat_username} 🍀 ⋅""",     
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        chat_name, url=f"https://t.me/{message.chat.username}")
                ],
            ]
        ),
    )
    
