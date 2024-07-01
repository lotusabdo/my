from base64 import b64decode
from inspect import getfullargspec
from io import BytesIO
import requests
from aiohttp import ClientSession
from pyrogram import filters
from pyrogram.types import *
from AbdoX import app

button = InlineKeyboardMarkup([[
            InlineKeyboardButton("‹ 𝖢𝗅𝗈𝗌𝖾 ›", callback_data="close_data")
                              ]])



aiohttpsession = ClientSession()


async def post(url: str, *args, **kwargs):
    async with aiohttpsession.post(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data



async def take_screenshot(url: str, full: bool = False):
    url = "https://" + url if not url.startswith("http") else url
    payload = {
        "url": url,
        "width": 1100,
        "height": 1900,
        "scale": 1,
        "format": "jpeg",
    }
    if full:
        payload["full"] = True
    data = await post(
        "https://webscreenshot.vercel.app/api",
        data=payload,
    )
    if "image" not in data:
        return None
    b = data["image"].replace("data:image/jpeg;base64,", "")
    file = BytesIO(b64decode(b))
    file.name = "webss.jpg"
    return file


async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})


@app.on_message(filters.command("اسكرين",prefixes=""))
async def take_ss(_, message: Message):
    if len(message.command) < 2:
        return await eor(message, text="**• استخدم الامر هكذا : \n\n • اسكرين + اللينك **")

    if len(message.command) == 2:
        url = message.text.split(None, 1)[1]
        full = False
    elif len(message.command) == 3:
        url = message.text.split(None, 2)[1]
        full = message.text.split(None, 2)[2].lower().strip() in [
            "yes",
            "y",
            "1",
            "true",
        ]
    else:
        return await eor(message, text="<\b>خطا حاول مجددا<\b>")

    m = await eor(message, text="**◍ <\b>جاري رفع الاسكرين علي محركات التليجرام<\b>")

    try:
        photo = await take_screenshot(url, full)
        if not photo:
            return await m.edit("◍ <\b>خطا لم يتم اخد اسكربن<\b>*")

        m = await m.edit("◍ <\b>تمم معالجه الصورة<\b>")

        if not full:
            await message.reply_photo(photo, reply_markup=button)
        else:
            await message.reply_photo(photo, reply_markup=button)
        await m.delete()
    except Exception as e:
        await m.edit(str(e))
