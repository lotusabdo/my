from pyrogram import filters, Client
from AbdoX import app
import asyncio
from pyrogram.types import VideoChatEnded, Message
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AbdoX.core.call import Alina
from AbdoX.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)
@app.on_message(filters.regex("^مين في الكول$"))
async def strcall(client, message):
    assistant = await group_assistant(Alina,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./AbdoX/assets/call.mp3"), stream_type=StreamType().pulse_stream)
        text="الناس القاعده في المكالمه تكذب:\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يرغوي "
            else:
                mut="ساكت "
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}➤{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"    
        await message.reply(f"{text}")
        await asyncio.sleep(7)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"المكالمه مش مفتوحه اصلا")
    except TelegramServerError:
        await message.reply(f"ارسل الامر تاني في مشكله في سيرفر التلجرام")
    except AlreadyJoinedError:
        text="االناس القاعده في المكالمه تكذب:\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يرغوي"
            else:
                mut="ساكت "
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}➤{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"    
        await message.reply(f"{text}")
@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
    da = message.video_chat_ended.duration
    ma = divmod(da, 60)
    ho = divmod(ma[0], 60)
    day = divmod(ho[0], 24)
    if da < 60:
       await message.reply(f"** - تم انهاء مكالمة الفيديو مدتها {da} ثواني وصكرها **")        
    elif 60 < da < 3600:
        if 1 <= ma[0] < 2:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها دقيقه**")
        elif 2 <= ma[0] < 3:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها دقيقتين **")
        elif 3 <= ma[0] < 11:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها {ma[0]} دقايق **")  
        else:
            await message.reply(f"**- تم إنهاء مكالمة الفيديو مدتها {ma[0]} دقيقه**")
    elif 3600 < da < 86400:
        if 1 <= ho[0] < 2:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها ساعه **")
        elif 2 <= ho[0] < 3:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها ساعتين **")
        elif 3 <= ho[0] < 11:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها {ho[0]} ساعات **")  
        else:
            await message.reply(f"**- تم إنهاء مكالمة الفيديو مدتها {ho[0]} ساعة **")
    else:
        if 1 <= day[0] < 2:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها يوم **")
        elif 2 <= day[0] < 3:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها يومين **")
        elif 3 <= day[0] < 11:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها {day[0]} ايام **")  
        else:
            await message.reply(f"**- تم إنهاء مكالمة الفيديو مدتها {day[0]} يوم**")
@Client.on_message(filters.command("رتبتي", ""))
async def bt(client: Client, message: Message):
  try:
     if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
     userr = message.from_user
     bot_username = client.me.username
     dev = await get_dev(bot_username)
     if userr.username in OWNER :
         await message.reply_text("**♪ رتبتك هي : مطور السورس  💎 .**")
         return
     if userr.username in ["EU_TM"]:
         await message.reply_text("**♪ رتبتك هي : المطور كابوس  💎 .**")
         return
     if userr.username in ["EU_TM"]:
         await message.reply_text("**♪ رتبتك هي : المطور كابوس 💎 .**")
         return
     if userr.id == dev:
        return await message.reply_text("**♪ رتبتك هي : المطور الاساسي  💎 .**")
     user = await message._client.get_chat_member(message.chat.id, message.from_user.id)
     if user.status == enums.ChatMemberStatus.OWNER:
         await message.reply_text("**♪ رتبتك هي : المالك  💎 .**")
         return
     if user.status == enums.ChatMemberStatus.ADMINISTRATOR:
         await message.reply_text("**♪ رتبتك هي : الادمن  💎 .**")
         return 
     else:
         await message.reply_text("**♪ رتبتك هي : العضو  💎 .**")
  except:
    pass
