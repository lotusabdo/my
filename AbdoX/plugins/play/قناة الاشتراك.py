from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AbdoX import app

@app.on_message(filters.private & filters.user(OWNER_ID))
async def must_join_channel(_, message):
    if "‹ قناة الاشتراك ›" in message.text:
        link = f"https://t.me/{l2_2Y}"
        await message.reply(
            text=f"~ عزيزي المطور \n~ هذا هي قناة الاشتراك الاجباري @{l2_2Y} .",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("قناة البوت", url=link)]
            ])
        )
