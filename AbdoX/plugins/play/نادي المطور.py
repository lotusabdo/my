
import asyncio
from strings.filters import command
from AbdoX.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from AbdoX import (Apple, Resso, Telegram, YouTube, app)
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import OWNER_ID

@app.on_message(filters.command(["المطور","اا "], ""))
async def khfzss(client: Client, message: Message):
    usrr = await client.get_chat(OWNER_ID)
    name = usrr.first_name
    bio = usrr.bio
    id = usrr.id
    username = usrr.username
    async for photo in client.get_chat_photos(OWNER_ID, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""مــعلومــات مــطور الــبـوت : \n\n name: {name} \n\n usre: @{username} \n\n id: {id} \n\n bio: {bio} \n\n 𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{username}")
                ],
            ]
        ),
    )                    
    chatusername = f"@{message.chat.username}"
    user_id = message.from_user.id
    user_ab = message.from_user.username
    user_name = message.from_user.first_name
    buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await app.send_message(OWNER_ID, f"- قام {message.from_user.mention}\n"
                                     f"- بمناداتك عزيزي المطور\n"
                                     f"- الأيدي {user_id}\n"
                                     f"- اليوزر @{user_ab}\n"
                                     f"- ايدي المجموعة {message.chat.id}\n"
                                     f"- الرابط {chatusername}",
                                     reply_markup=reply_markup)

    # إنشاء زر "اونلاين"
    online_button = InlineKeyboardButton("<قناة البوت>", url=f"https://t.me/{l2_2Y}")
    
    await message.reply_text(f"~ تم إرسال النداء إلى مطور البوت\n\n-› Master -› @{l2_2Y} .",
                             disable_web_page_preview=True,
                             reply_markup=InlineKeyboardMarkup([[online_button]]))
