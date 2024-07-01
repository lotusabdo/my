from pyrogram import filters
import asyncio
import pyfiglet 
from random import choice
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram.handlers import MessageHandler
from AbdoX import app


def figle(text):
    x = pyfiglet.FigletFont.getFonts()
    font = choice(x)
    figled = str(pyfiglet.figlet_format(text,font=font))
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="‹ 𝖢𝗁𝖺𝗇𝗀𝖾 ›", callback_data="figlet"),InlineKeyboardButton(text="‹ 𝖢𝗅𝗈𝗌𝖾 ›", callback_data="close_reply")]])
    return figled, keyboard

@app.on_message(filters.command(["نمط"], ""))
async def ahmedteto(bot, message):
    global text
    try:
        text = message.text.split(' ',1)[1]
    except IndexError:
        return await message.reply_text("↢ مثال:\n نمط Abdo")
    kul_text, keyboard = figle(text)
    await message.reply_text(f"↢ هذا هو النمط الخاص بك :\n<pre>{kul_text}</pre>", quote=True, reply_markup=keyboard)

@app.on_callback_query(filters.regex("figlet"))
async def figlet_handler(Client, query: CallbackQuery):
  try:
      kul_text, keyboard = figle(text)
      await query.message.edit_text(f"↢ هذا هو النمط الخاص بك :\n<pre>{kul_text}</pre>", reply_markup=keyboard)
  except Exception as e : 
      await message.reply(e)
__mod_name__ = "نمط" 
__help__="""
❍ /نمط : انشاء نمط خاص بك بدون عناء
مثال :\n\n/نمط Abdo"""
