from pyrogram.types import InlineKeyboardButton

import config
from AbdoX import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="- 𝐆 𝐑 𝐎 𝐔 𝐏 ↺", url= "https://t.me/Q_CR_3"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        
        [
            InlineKeyboardButton(text="مطور البوت", url=f"https://t.me/YeYvYe"),
            InlineKeyboardButton(text="𝗚𝗥𝗼𝘂𝗽", url=f"https://t.me/Tm_JACK"), 
        ],
        [
            
            InlineKeyboardButton(text="𝗧𝗲𝗠 𝗝𝗮𝗖𝗞", url=f"https://t.me/SORCE_JACK") , 
        ],
    ]
    return buttons
