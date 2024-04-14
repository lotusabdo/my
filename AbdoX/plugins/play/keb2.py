import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, Telegram, YouTube, app)
from AarohiX import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(filters.command(["اصدار"], ""))
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/73299cc44862f1ec277dd.jpg",
        caption=f"""«~~~~•𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀•~~~~»\nمرحبا بك عزيزي {message.from_user.mention}\n
♡♕᚜ اسم سورس:-بودا
♡♕᚜ نوعه:-ميوزك
♡♕᚜ للغه برمجه:- بايثون
♡♕᚜ اللغه:-اللغه العربيه ويدعم الانجليزيه 
♡♕᚜ مجال تشغيل :- تشغيل بوتات الميوزك
♡♕᚜ نظام تشغيل:-بودا بوت ميوزك
♡♕᚜ الاصدار 4.0.1 pyrogram 
♡♕᚜ تاريخ تاسيس:-10-4-2022
«~~~~•𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀•~~~~»""",) 
        
        
        
    


