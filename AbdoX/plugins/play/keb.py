import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from AbdoX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest


@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = "🧑🏻‍✈️︙اهلا بك بك عزيزي العضو ♥️**\n\n**⤵️︙ اليـكـ كيب الاعضاء الخاص بسورس بودا"
        kep = ReplyKeyboardMarkup([
[" المطور", "مطور السورس"],
["السورس","يـوتيوب "],
["اقتباس","استوري"],
["انمي","متحركه"],
["تويت", "صراحه"],
["نكته","احكام"],
[" لو خيروك","انصحني"],
["قران","نقشبندي"],
["اذكار","كتابات"],
["حروف","بوت"],
["غنيلي","سوال"],
["تلاوات","عبدالباسط"],
["افاتار بنات","افاتار شباب"],
["❎ ¦ حذف الكيبورد"]], resize_keyboard=True)
        await message.reply(
              text=text,
               reply_markup=kep,quote=True)

@app.on_message(filters.command(["❎ ¦ حذف الكيبورد"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )

@app.on_message(filters.command(["❎ ¦ حذف الكيبورد"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )
@app.on_message(filters.regex("يـوتيوب"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://graph.org/file/e8b472bcfa6680f6c6a5d.jpg",
        caption=f"""يتم استخدام هذا الامر لعرض تحميل من اليوتيوب\nاستخدم الامر بهذا الشكل `تنزيل`  او  `يوتيوب`  كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدا """,
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ՏΌႮᎡᏟᎬ ᏞΌͲႮՏ", url=f"https://t.me/l2_2Y"),
            ]
         ]
     )
        )