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
            InlineKeyboardButton(text="- 𝐃 𝐄 𝐕 ↺", url=f"https://t.me/Q6_6C"),
            InlineKeyboardButton(text="- 𝐆 𝐑 𝐎 𝐔 𝐏 ↺", url=f"https://t.me/Q_CR_3"), 
        ],
        [
            
            InlineKeyboardButton(text="- 𝐒 𝐎 𝐔 𝐑 𝐂 𝐄 ↺", url=f"https://t.me/l2_2Y") , 
        ],
    ]
    return buttons
