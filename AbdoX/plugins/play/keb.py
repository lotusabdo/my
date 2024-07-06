import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from AbdoX import (Apple, Resso, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest


@app.on_message(filters.regex("^/SaVlO"), group=39)
async def cpanel(_, message: Message):             
        text = "اهلا بك بك عزيزي العضو اليك كيب الاعضاء⚡"
        kep = ReplyKeyboardMarkup([
[" مبرمج السورس", "مطور السورس"],
["السورس","المطور"],
["الالعاب"],
["انميي","متحركة"],
["تويت", "صراحه"],
["لو خيروك"],
["اقتباس","نقشبندي"],
["سوال","اقتباس"],
["استوريهات"],
["تلاوات","عبدالباسط"],
["صور بنات","صور ولاد"],
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
        photo=f"https://telegra.ph/file/73299cc44862f1ec277dd.jpg",
        caption=f"""يتم استخدام هذا الامر لعرض تحميل من اليوتيوب\nاستخدم الامر بهذا الشكل `تنزيل`  او  `يوتيوب`  كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدا """,
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("SoUrCe SaVlO", url=f"https://t.me/l2_2Y"),
            ]
         ]
     )
        )
