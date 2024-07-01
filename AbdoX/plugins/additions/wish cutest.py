from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
import requests
from AbdoX import app

SUPPORT_CHAT = "Mr_Eirux"

@app.on_message(filters.regex(r"\bامنيه\b"))
async def wish(_, m):
    if len(m.text.split()) < 2:
        await m.reply("قول امنيتك 🥀!")
        return

    api = requests.get("https://nekos.best/api/v2/happy").json()
    url = api["results"][0]['url']
    text = m.text.split(None, 1)[1]
    wish_count = random.randint(1, 100)
    wish = f"◍ مرحبًا {m.from_user.first_name}! \n"
    wish += f"◍ امنيتك: {text} \n"
    wish += f"◍ نسبة حدوثها: {wish_count}%"
    
    await app.send_animation(
        chat_id=m.chat.id,
        animation=url,
        caption=wish,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("‹ 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 ›", url=f"https://t.me/{SUPPORT_CHAT}")]])
    )
            
BUTTON = [[InlineKeyboardButton("‹ 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 ›", url=f"https://t.me/{SUPPORT_CHAT}")]]
CUTIE = "https://64.media.tumblr.com/d701f53eb5681e87a957a547980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif"

@app.on_message(filters.regex(r"\bكيوت\b"))
async def cute(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTE = f"⌯ نسبة الكياته {mention} {mm}% 😂♥"

    await app.send_document(
        chat_id=message.chat.id,
        document=CUTIE,
        caption=CUTE,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )
    
help_text = """
» ما هي (امنيه):>>
تقوم بكتابة أمنيه خاصه بك وسيقوم البوت بتخمين نسبة حدوثها لك!
مثال: » امنيه نجاحي في العمل 
» امنيه اريد الحصول على ايفون
» كيوت ما هي نسبة الكياته 😂♥ 
"""
