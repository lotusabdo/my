from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from AbdoX import app
from config import OWNER_ID
from pyrogram.types import Message
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ----------------------------AbdoX------------------------------- #


@app.on_message(filters.create(lambda _, __, m: m.text and "تثبيت" in m.text.lower()) & admin_filter)
async def pin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("هذه الميزه تعمل فقط بالمجموعات √")
    elif not replied:
        await message.reply_text("قم بعمل رد لتثبيت الرساله √")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.pin()
                await message.reply_text(f"تم تثبيت الرساله بنجاح √", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("شاهد الرساله ◍", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))


@app.on_message(filters.create(lambda _, __, m: m.text and "مثبت" in m.text.lower()))
async def pinned(_, message):
    chat = await app.get_chat(message.chat.id)
    if not chat.pinned_message:
        return await message.reply_text("لم يتم العثور على رسالة مثبته")
    try:        
        await message.reply_text("هنا آخر رسالة مثبته",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(text="◍ رؤية الرساله",url=chat.pinned_message.link)]]))  
    except Exception as er:
        await message.reply_text(er)


# ----------------------------AbdoX------------------------------- #

@app.on_message(filters.create(lambda _, __, m: m.text and "الغاء تثبيت" in m.text.lower()) & admin_filter)
async def unpin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("هذه الميزه تعمل فقط بالمجموعات √")
    elif not replied:
        await message.reply_text("قم بعمل رد علي الرساله")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.unpin()
                await message.reply_text(f"تم الغاء تثبيت الرساله بنجاح √", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("شاهد الرساله ◍", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))




# ----------------------------AbdoX------------------------------- #

@app.on_message(filters.create(lambda _, __, m: m.text and "حذف الصورة" in m.text.lower()) & admin_filter)
async def deletechatphoto(_, message):
      
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("يتم المعالجه...")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("هذه الميزه تعمل فقط بالمجموعات √ !") 
      try:
         if admin_check.privileges.can_change_info:
             await app.delete_chat_photo(chat_id)
             await msg.edit("تم بنجاح حذف صورة الجروب !\nبواسطة : {}".format(message.from_user.mention))    
      except:
          await msg.edit("لا يوجد صورة او ليس لدي صلاحيات لحذف صورة الجروب !")


# ----------------------------AbdoX------------------------------- #

@app.on_message(filters.create(lambda _, __, m: m.text and "وضع الصورة" in m.text.lower()) & admin_filter)
async def setchatphoto(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("يتم المعالجه...")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("هذه الميزه تعمل فقط بالمجموعات √ !") 
      elif not reply:
           await msg.edit("قم بالرد على صورة او ملف صورة.")
      elif reply:
          try:
             if admin_check.privileges.can_change_info:
                photo = await reply.download()
                await message.chat.set_photo(photo=photo)
                await msg.edit_text("تم اضافة صورة الجروب بنجاح !\nبواسطة : {}".format(message.from_user.mention))
             else:
                await msg.edit("هناك خطأ يرجى وضع صورة اخرى !")
     
          except:
              await msg.edit("ليس لدي الصلاحيات الكافية لوضع صورة للجروب !")


# ----------------------------AbdoX------------------------------- #
@app.on_message(filters.create(lambda _, __, m: m.text and "وضع الاسم" in m.text.lower()) & admin_filter)
async def setgrouptitle(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("يتم المعالجه...")
    if message.chat.type == enums.ChatType.PRIVATE:
          await msg.edit("هذه الميزه تعمل فقط بالمجموعات √ !")
    elif reply:
          try:
            title = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("تم وضع اسم جديد للجروب بنجاح!\nبواسطة : {}".format(message.from_user.mention))
          except AttributeError:
                await msg.edit("ليس لديك صلاحيات كافية لتغيير اسم الجروب!")   
    elif len(message.command) >1:
        try:
            title = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("تم بنجاح تغيير اسم الجروب !\nبواسطة : {}".format(message.from_user.mention))
        except AttributeError:
               await msg.edit("ليس لديك صلاحيات كافيه لتغيير اسم الجروب!")
          

    else:
       await msg.edit("قم بالرد على اسم الجروب المراد وضعه")


# ----------------------------AbdoX------------------------------- #



@app.on_message(filters.create(lambda _, __, m: m.text and "وضع وصف" in m.text.lower()) & admin_filter)
async def setg_discription(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("يتم المعالجه...")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("هذه الميزه تعمل فقط بالمجموعات √ !")
    elif reply:
        try:
            discription = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("تم وضع وصف جديد للجروب!\nبواسطة : {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("ليس لديك صلاحيات كافية لتغيير وصف الجروب!")   
    elif len(message.command) > 1:
        try:
            discription = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("تم بنجاح تغيير وصف الجروب!\nبواسطة : {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("ليس لديك صلاحيات كافية لتغيير وصف الجروب!")
    else:
        await msg.edit("قم بالرد بالأمر على الكليشة المراد وضعها!")


# ----------------------------AbdoX------------------------------- #

@app.on_message(filters.create(lambda _, __, m: m.text and ("بوتي غادر" in m.text.lower() or "سوفيا اخرجي" in m.text.lower())) & admin_filter)
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = "<b>تم الخروج بنجاح من المجموعة</b> √"
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)
    await delete_served_chat(chat_id)



# ----------------------------AbdoX------------------------------- #
