from pyrogram.types import InlineKeyboardButton

import config
from AbdoX import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𝐆𝐑𝐎𝐔𝐏", url= "https://t.me/jx_xll"),
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
            InlineKeyboardButton(text="مطور السورس ", url=f"https://t.me/EU_TM"),
            InlineKeyboardButton(text="𝐆𝐑𝐎𝐔𝐏", url=f"https://t.me/jx_xll"), 
        ],
        [
            
            InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=f"https://t.me/l2_2Y") , 
        ],
    ]
    return buttons
