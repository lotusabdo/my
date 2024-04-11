import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from MatrixMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_video(
        video=f"https://telegra.ph/file/e6f815307a347ec6e17d5.mp4",
        caption=f"""<b>↯︙مرحباً بك عزيزي</b>\n<b>↯︙استخدم الازرار بالاسفل\n» ل تصفح اوامر الميوزك</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ اوامر التشغيل ›", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "‹ اوامر القناة ›", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "‹ اوامر الادمن ›", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "‹ اوامر المطور ›", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(name, url=f"https://t.me/{usrnam}"),
                ],[
                    InlineKeyboardButton(
                        "‹ ᥉᥆ᥙᖇᥴᥱ ᥉᥆ꪔ3ᥲ ›", url="https://t.me/SOURCE_SOM3A"),
                ],
            ]
        ),
    )


