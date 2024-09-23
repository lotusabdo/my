import asyncio
from asyncio import gather
from pyrogram import Client, filters
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
import time
import aiohttp
from pyrogram.types import CallbackQuery
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AbdoX import (Apple, Resso, Spotify, Telegram, YouTube, app)
from AbdoX import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait


iddof = []
id = {}

@app.on_message(filters.command(["تعطيل الايدي", "قفل الايدي"], "") & filters.group)
async def iddlock(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in iddof:
            return await message.reply_text("◍الامر معطل من قبل")
        iddof.append(message.chat.id)
        return await message.reply_text("◍تم تعطيل الايدي بنجاح")
    else:
        return await message.reply_text("◍عذرا عزيزي هذا الامر للادمن الجروب فقط")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], "") & filters.group)
async def iddopen(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in iddof:
            return await message.reply_text("◍الايدي مفعل من قبل")
        iddof.remove(message.chat.id)
        return await message.reply_text("◍تم تفعيل الايدي بنجاح")
    else:
        return await message.reply_text("◍عذرا عزيزي هذا الامر للادمن الجروب فقط")

@app.on_message(filters.command(["ايدي","ا"], ""))
async def muid(client: Client, message):
    if message.chat.id in iddof:
        return await message.reply_text("◍تم تعطيل امر الايدي من قبل المشرفين")
    
    user = await client.get_chat(message.from_user.id)
    user_id = user.id
    username = user.username
    first_name = user.first_name
    bio = user.bio
    chat = message.chat.title
    chat_id = message.chat.id
   
    photo = user.photo.big_file_id
    if photo:
        photo = await client.download_media(photo)
    else:
        photo = None
    
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""𝅄 𓏺 𝐍𝐚𝐦𝐞 :{message.from_user.mention}\n𝅄 𓏺 𝐔𝐬𝐞𝐫 :@{message.from_user.username}\n𝅄 𓏺 𝐈𝐝 :`{message.from_user.id}`\n𝅄 𓏺 𝐁𝐢𝐨 :{usr.bio}\n𝅄 𓏺 𝐂𝐡𝐚𝐭 : {message.chat.title}\n𝅄 𓏺 𝐈𝐝 𝐜𝐡𝐚𝐭:`{message.chat.id}`""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
