import sys
import asyncio
import requests
import re
import string
from pyrogram.types import Message
from aiohttp import ClientSession
from pyrogram import filters, Client
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from AbdoX import (Apple, Resso , Spotify, Telegram, YouTube, app)

#########
#الاوامر
@app.on_message(
    filters.command(["الاوامر"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/73299cc44862f1ec277dd.jpg",
        caption=f"""✅ مرحبا بك عزيزي {message.from_user.mention}
     
✅ اليك قائمة اوامر سورس بودا
      

✅ قائمه الاوامر تحتوي علي ٢ اوامر .
      
1 ← اوامـر الـحـمـايـه .
2 ← اوامـر الـمـوزك .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "اوامـر الحـمايـه", callback_data=f"hmaya"),
                    InlineKeyboardButton(
                        "اوامـر الـمـوزك", callback_data=f"musichelal"),
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀", callback_data=f"devhelp"),
                ],[
                    InlineKeyboardButton(
                        "إغـلاق", callback_data=f"close"),
               ],
            ]
        ),
    )
#الاوامر كول باك
@app.on_callback_query(filters.regex("ayamr"))
async def ayamr(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ اليك قائمة اوامر سورس بودا
          
✅ قائمه الاوامر تحتوي علي ٢ اوامر .
           
1 ← اوامـر الـحـمـايـه .
2 ← اوامـر الـمـوزك .""",reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "اوامـر الحـمايـه", callback_data=f"hmaya"),
                    InlineKeyboardButton(
                        "اوامـر الـمـوزك", callback_data=f"musichelal"),
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀", callback_data=f"devhelp"),
                ],[
                    InlineKeyboardButton(
                        "إغـلاق", callback_data=f"close"),
               ],
            ]
        ),
    )
########
#اوامر الحمايه
@app.on_callback_query(filters.regex("hmaya"))
async def bhr(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f""" ✅ اليك قائمة اوامر سورس بودا
         

✅ قائمه الاوامر الحمايه تحتوي علي  اوامر .
         𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀 """,reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "اوامـر التسليه", callback_data=f"maya"),
                    InlineKeyboardButton(
                        "اوامـر الادمن", callback_data=f"aya"),
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀", callback_data=f"devv"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع ♬", callback_data=f"ayamr"), 
               ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("maya"))
async def bhhr(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ اليك قائمة اوامر سورس بودا
          
✅ قائمه الاوامر الحمايه تحتوي علي  اوامر .
           
1 ← اوامر الحمايه  .
2 ← اوامر الحمايه  .""",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامـر الادمن", callback_data=f"aya"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع ♬", callback_data=f"hmaya"), 
               ],
            ]
        ),
    )
    
@app.on_callback_query(filters.regex("aya"))
async def br(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ اليك قائمة اوامر سورس بودا
         

✅ قائمه الاوامر الحمايه تحتوي علي  اوامر .
         
1 ← اوامر الحمايه  .
2 ← اوامر الحمايه  .""",reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "اوامـر التسليه", callback_data=f"maya"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع ♬", callback_data=f"hmaya"), 
               ],
            ]
        ),
    )
    


@app.on_callback_query(filters.regex("musichelal"))
async def back(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ اليك قائمة اوامر سورس بودا
         

✅ قائمه الاوامر الميوزك تحتوي علي 6 اوامر .
          
1 ← اوامر التشغيل .
2 ← اوامر القنوات .
3 ← اوامر مطور البوت .
4 ← مميزات السورس .
5 ← اوامر البوت .
6 ← اوامر الادمن .""",
       reply_markup=InlineKeyboardMarkup(
                [
                      [
                      InlineKeyboardButton(
                        "اوامـر الـتـشـغـيل", callback_data=f"g1"),
                    InlineKeyboardButton(
                        "اوامـر الـقـنـوات", callback_data=f"g2"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـمـطـور", callback_data=f"g3"),
                    InlineKeyboardButton(
                        "مـمـيـزات الـسـورس", callback_data=f"g4"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـبـوت", callback_data=f"g5"),
                    InlineKeyboardButton(
                        "اوامـر الادمـن", callback_data=f"g6"),
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
               "رجـوع ♬", callback_data=f"ayamr"),
               ],
            ]
        ),
    )
       
#قائمه الاوامر الاولي
@app.on_callback_query(filters.regex("g1"))
async def tt(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""

         
✅ اليك قائمة اوامر التشغيل ,

- اولا اليك اوامر التشغيل ف الجروب .
          
- لتشغيل اغنيه اكتب : تشغيل او شغل او /play
- لتشغيل فيديو اكتب : فيديو او /video
- لأنهاء الاغنيه اكتب : ايقاف او انهاء او /stop
- لايقاف الاغنيه مؤقت اكتب : وقف او /pause
- لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او /resume
- لتخطي الاغنيه اكتب : تخطي او /skip
- لكتم البوت في الكول اكتب : اسكت او /mute
- لألغاء كتم البوت في الكول اكتب : اتكلم او /unmute
- لاعادة تشغيل البوت اكتب : /restart""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "اوامـر الـقـنـوات", callback_data=f"g2"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـمـطـور", callback_data=f"g3"),
                    InlineKeyboardButton(
                        "مـمـيـزات الـسـورس", callback_data=f"g4"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـبـوت", callback_data=f"g5"),
                    InlineKeyboardButton(
                        "اوامـر الادمـن", callback_data=f"g6"),
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع ♬", callback_data=f"musichelal"),
               ],
          ]
        ),
    )
    
#قائمه الاوامى الثانيه
@app.on_callback_query(filters.regex("g2"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""

       
✅ اليك قائمة اوامر القنوات ,

- اولا اليك اوامر ربط البوت ب القناة .
      
 لربط البوت ب القناة مالك القناة فقط يستطيع ربطه .
لربط القناة اكتب : ربط + معرف القناة

- ثانيا اليك اوامر تشغيل البوت في القناة .

- لتشغيل اغنيه اكتب : ق تشغيل او ق شغل او cplay
- لتشغيل فيديو اكتب : ق فيديو او cvideo
- لأنهاء الاغنيه اكتب : ق ايقاف او ق انهاء او cstop
- لايقاف الاغنيه مؤقت اكتب : ق وقف او cpause
- لتكملة الاغنيه من الايقاف المؤقت اكتب : ق كمل او cresume
- لتخطي الاغنيه اكتب : تخطي او cskip
- لكتم البوت في الكول اكتب : ق اسكت او cmute
- لألغاء كتم البوت في الكول اكتب : ق اتكلم او cunmute
- لاعادة تشغيل البوت اكتب : /restart""",
       reply_markup=InlineKeyboardMarkup(
               [
                    [
                      InlineKeyboardButton(
                        "اوامـر الـتـشـغـيل", callback_data=f"g1"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـمـطـور", callback_data=f"g3"),
                    InlineKeyboardButton(
                        "مـمـيـزات الـسـورس", callback_data=f"g4"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـبـوت", callback_data=f"g5"),
                    InlineKeyboardButton(
                        "اوامـر الادمـن", callback_data=f"g6"),
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع ♬", callback_data=f"musichelal"),
               ],
          ]
        ),
    )

#قائمه الاوامى الثالثه
@app.on_callback_query(filters.regex("g3"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""

      
✅ اليك قائمة اوامر مطور البوت ,

- جميع الاوامر خاصه بمطور البوت فقط .
      
- لعمل اذاعه في البوت اعمل ريبلاي علي الاذاعه واكتب : اذاعه .
 - لعرض احصائيات البوت اكتب : الاحصائيات .
- لعرض سرعه البوت اكتب : بينج .
- للتحكم في لغه البوت اكتب : اللغه .
- للتحكم في ازار التشغيل اكتب : وضع شغل .
- لعرض اعدادات البوت اكتب : الاعدادات .

- ثانيا اليك اوامر الرتب .
      
- لرفع ادمن في الجروب اكتب : ر ا د .
- لرفع ادمن في الجروب اكتب : ت ا د .
- لعرض قائمه الادمنيه اكتب : ق ا د .
- لرفع مطور ثانوي اكتب : ر م ث .
- لتنزيل مطور ثانوي اكتب : ت م ث .
- لعرض قائمه الثانوين اكتب : ق م ث .

- ثالثا اليك اوامر الحظر .
      
- لحظر عضو من الجروب اكتب : ح ر .
- لالغاء حظر عضو من الجروب اكتب : ا ر .
- لعرض قائمه المحظورين اكتب : ق ح ر .
- لحظر عضو عام من الجروب اكتب : ح ع .
- لالغاء حظر عضو عام من الجروب اكتب : ا ر .
- لعرض قائمه المحظورين عام اكتب : ق ح ع .""",
       reply_markup=InlineKeyboardMarkup(
                    [
                      [
                      InlineKeyboardButton(
                        "اوامـر الـتـشـغـيل", callback_data=f"g1"),
                    InlineKeyboardButton(
                        "اوامـر الـقـنـوات", callback_data=f"g2"),
                ],[
                    InlineKeyboardButton(
                        "مـمـيـزات الـسـورس", callback_data=f"g4"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـبـوت", callback_data=f"g5"),
                    InlineKeyboardButton(
                        "اوامـر الادمـن", callback_data=f"g6"),
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع ♬", callback_data=f"musichelal"),
               ],
          ]
        ),
    )
    
#قائمه الاوامى الثالثه
@app.on_callback_query(filters.regex("g4"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""


      
✅ اليك قائمة مميزات السورس ,
      
✅ هذه قائمه مميزات سورس بودا الميوزك .
      
- لعرض اوامر البوت اكتب : الاوامر .
- لعرض كليشه السورس اكتب : سورس بودا .
- لعرض مطور البوت اكتب : المطور .
- لعرض اسم البوت اكتب : البوت .
- لعرض الايدي الخاص بك وصورتك اكتب : ا .

✅ اولا قائمة اوامر البوت ,
      
- لعمل اذاعه في البوت اعمل ريبلاي علي الاذاعه واكتب : اذاعه .
- لعرض سرعه البوت اكتب : بينج .
- للتحكم في لغه البوت اكتب : اللغه .
- للتحكم في ازار التشغيل اكتب : وضع شغل .
- لعرض اعدادات البوت اكتب : الاعدادات .

✅ ثانيا اليك اوامر الرتب .
      
- لرفع ادمن في الجروب اكتب : ر ا د .
- لرفع ادمن في الجروب اكتب : ت ا د .
- لعرض قائمه الادمنيه اكتب : ق ا د .

✅ ثالثا اليك اوامر الحظر .
      
- لحظر عضو من الجروب اكتب : ح ر .
- لالغاء حظر عضو من الجروب اكتب : ا ر .
- لعرض قائمه المحظورين اكتب : ق ح ر .""",
       reply_markup=InlineKeyboardMarkup(
                    [
                      [
                      InlineKeyboardButton(
                        "اوامـر الـتـشـغـيل", callback_data=f"g1"),
                    InlineKeyboardButton(
                        "اوامـر الـقـنـوات", callback_data=f"g2"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـمـطـور", callback_data=f"g3"),          
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـبـوت", callback_data=f"g5"),
                    InlineKeyboardButton(
                        "اوامـر الادمـن", callback_data=f"g6"),
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع ♬", callback_data=f"musichelal"),
               ],
          ]
        ),
    )
    
#قائمه الاوامى الثالثه
@app.on_callback_query(filters.regex("g5"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""


      
✅ اليك قائمة اوامر البوت ,
      
- لعرض سرعه البوت اكتب : بينج .
- للتحكم في لغه البوت اكتب : اللغه .
- للتحكم في ازار التشغيل اكتب : وضع شغل .
- لعرض اعدادات البوت اكتب : الاعدادات .

- ثانيا اليك اوامر الرتب .

- لرفع ادمن في الجروب اكتب : ر ا د .
- لرفع ادمن في الجروب اكتب : ت ا د .
- لعرض قائمه الادمنيه اكتب : ق ا د .
- لتنزيل مطور ثانوي اكتب : ت م ث .


- ثالثا اليك اوامر الحظر .

- لحظر عضو من الجروب اكتب : ح ر .
- لالغاء حظر عضو من الجروب اكتب : ا ر .
- لعرض قائمه المحظورين اكتب : ق ح ر .
- لحظر عضو عام من الجروب اكتب : ح ع .
- لالغاء حظر عضو عام من الجروب اكتب : ا ر .
- لعرض قائمه المحظورين عام اكتب : ق ح ع .""",
       reply_markup=InlineKeyboardMarkup(
                    [
                      [
                      InlineKeyboardButton(
                        "اوامـر الـتـشـغـيل", callback_data=f"g1"),
                    InlineKeyboardButton(
                        "اوامـر الـقـنـوات", callback_data=f"g2"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـمـطـور", callback_data=f"g3"),
                    InlineKeyboardButton(
                        "مـمـيـزات الـسـورس", callback_data=f"g4"),
                ],[
                    InlineKeyboardButton(
                        "اوامـر الادمـن", callback_data=f"g6"),
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع ♬", callback_data=f"musichelal"),
               ],
          ]
        ),
    )
    
#قائمه الاوامى الثالثه
@app.on_callback_query(filters.regex("g6"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""


      
✅ اليك قائمة اوامر الادمن ,

- جميع الاوامر خاصه ب الادمن فقط .
      
- لعرض سرعه البوت اكتب : بينج .
- للتحكم في لغه البوت اكتب : اللغه .
- للتحكم في ازار التشغيل اكتب : وضع شغل .
- لعرض اعدادات البوت اكتب : الاعدادات .

- ثانيا اليك اوامر الرتب .
       
- لرفع ادمن في الجروب اكتب : ر ا د .
- لرفع ادمن في الجروب اكتب : ت ا د .
- لعرض قائمه الادمنيه اكتب : ق ا د .

- ثالثا اليك اوامر الحظر .
       
- لحظر عضو من الجروب اكتب : ح ر .
- لالغاء حظر عضو من الجروب اكتب : ا ر .
- لعرض قائمه المحظورين اكتب : ق ح ر .""",
       reply_markup=InlineKeyboardMarkup(
                    [
                      [
                      InlineKeyboardButton(
                        "اوامـر الـتـشـغـيل", callback_data=f"g1"),
                    InlineKeyboardButton(
                        "اوامـر الـقـنـوات", callback_data=f"g2"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـمـطـور", callback_data=f"g3"),
                    InlineKeyboardButton(
                        "مـمـيـزات الـسـورس", callback_data=f"g4"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـبـوت", callback_data=f"g5"),
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع ♬", callback_data=f"musichelal"),
               ],
          ]
        ),
    )
##########  
#المطورين
#الاوامر
@app.on_callback_query(filters.regex("devhelp"))
async def devhelp(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"𝐖𝐞𝐥𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐁𝐨𝐝𝐚 𝐌𝐮𝐬𝐢𝐜",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "𖥻 𝐔𝐑 , 𝐅𝐚𝐕 𝐀𝐛𝐃𝐎𝐨 -", url=f"https://t.me/EU_TM"),
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀•", url=f"https://t.me/l2_2Y")
                ],[
                    InlineKeyboardButton(
                        "رجـوع ♬", callback_data=f"ayamr"),
               ], 
          ]
        ),
    )
#الحمايه   
@app.on_callback_query(filters.regex("devv"))
async def devh(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"𝐖𝐞𝐥𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐁𝐨𝐝𝐚 𝐌𝐮𝐬𝐢𝐜",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "𖥻 𝐔𝐑 , 𝐅𝐚𝐕 𝐀𝐛𝐃𝐎𝐨 -", url=f"https://t.me/EU_TM"),
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀", url=f"https://t.me/l2_2Y")
                ],[
                    InlineKeyboardButton(
                        "رجـوع ♬", callback_data=f"hmaya"),
               ],
          ]
        ),
    )
#الميوزك
@app.on_callback_query(filters.regex("devmusic"))
async def devmusic(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"𝐖𝐞𝐥𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐁𝐨𝐝𝐚 𝐌𝐮𝐬𝐢𝐜",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "𖥻 𝐔𝐑 , 𝐅𝐚𝐕 𝐀𝐛𝐃𝐎𝐨 -", url=f"https://t.me/EU_TM"),
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀•", url=f"https://t.me/l2_2Y")
                ],[
                    InlineKeyboardButton(
                        "رجـوع ♬", callback_data=f"musichelal"),
               ],
          ]
        ),
    )  
#الستار
@app.on_callback_query(filters.regex("devstart"))
async def devmusic(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"𝐖𝐞𝐥𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐁𝐨𝐝𝐚 𝐌𝐮𝐬𝐢𝐜",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "𖥻 𝐔𝐑 , 𝐅𝐚𝐕 𝐀𝐛𝐃𝐎𝐨 -", url=f"https://t.me/EU_TM"),
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀•", url=f"https://t.me/l2_2Y")
                ],[
                    InlineKeyboardButton(
                        "رجـوع ♬", callback_data=f"settingsback_helper"),
               ],
          ]
        ),
    )  
