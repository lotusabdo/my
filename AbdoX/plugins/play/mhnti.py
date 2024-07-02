import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AbdoX import app
from config import OWNER_ID

@app.on_message(filters.command(['مهنتي'], prefixes=""))
def get_user_info(_, message):
    url = f"https://t.me/{message.from_user.username}"
    age = random.randint(20, 30)
    jobs = ["مدرس 👨‍🏫", "طبيب 👨‍⚕", "مهندس 👷‍♂", "خيال 🏇", "سباح 🏊", "مطور 👨‍💻"]
    job = random.choice(jobs)
    statuses = ["متزوج 👨‍👩‍👧‍👦", "اعزب 🧍‍♂", "مرتبط 👩‍❤️‍💋‍👨", "نرجسي 💆‍♂", "ملهم 🧝‍♂"]
    status = random.choice(statuses)
    inline_keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(f"↢ اسمك :  {message.from_user.first_name}", url=url)],
            [InlineKeyboardButton(f"↢ عمرك :  {age}", callback_data=f"age_{age}")],
            [InlineKeyboardButton(f"↢ مهنتك :  {job}", callback_data=f"job_{job}")],
            [InlineKeyboardButton(f"↢ حالتي :  {status}", callback_data=f"status_{status}")], 
            [InlineKeyboardButton("𝖲𝗈𝖴𝗋𝖼𝖾 𝖤𝗂𝗋𝖳𝗁𝗈𝗇", url=f"https://t.me/eirthon")]
        ]
    )
    app.send_photo(
        chat_id=message.chat.id,
        photo=url,
        reply_markup=inline_keyboard
    )

