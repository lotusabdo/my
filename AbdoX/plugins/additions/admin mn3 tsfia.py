from AbdoX import app
from AbdoX.misc import SUDOERS
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client, filters
from pyrogram import enums
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus , ChatType
from pyrogram.types import ChatPermissions, ChatPrivileges
import asyncio

welcome_enabled = True

strict_txt = [
    "لا تصل إلى الكبرى.",
    "حقًا؟ انه لشئ مضحك.",
    "لا يمكنني تقييد أعز أصدقائي.",
    "أعرفه. حاول أن تفهم، إذا قمت بتقييده، سيكون الأمر سيئًا."
]

# أوامر الترقيات والتخفيضات باللغة العربية
promote = ["ترقيه", "ترقية"]
fullpromote = ["ترقيه كامله", "ترقية كاملة" ,"رول"]
demote = ["تخفيض", "تخفيض الرتبه", "نزع"]

# ----------------------------AbdoX------------------------------- #

@app.on_message(filters.command(["ترقيه", "ترقية", "ترقيه كامله", "ترقية كاملة", "تخفيض", "تخفيض الرتبه"]) & admin_filter)
async def handle_admin_commands(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    
    if not reply:
        return await message.reply(random.choice(strict_txt))

    user_id = reply.from_user.id
    command = message.command[0].lower()

    if command in promote:
        await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
            can_change_info=False,
            can_invite_users=True,
            can_delete_messages=True,
            can_restrict_members=False,
            can_pin_messages=True,
            can_promote_members=False,
            can_manage_chat=True,
            can_manage_video_chats=True,
        ))
        await message.reply("تمت ترقية العضو ببعض الصلاحيات بنجاح!")

    elif command in demote:
        await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
            can_change_info=False,
            can_invite_users=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_chat=False,
            can_manage_video_chats=False,
        ))
        await message.reply("تم تخفيض رتبة العضو بنجاح!")

    elif command in fullpromote:
        await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
            can_change_info=True,
            can_invite_users=True,
            can_delete_messages=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=True,
            can_manage_chat=True,
            can_manage_video_chats=True,
        ))
        await message.reply("تمت ترقية العضو بكامل الصلاحيات بنجاح!")

@app.on_chat_member_updated()
async def welcome(client, chat_member_updated):
    if not welcome_enabled:
        return
    
    if chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED:
        kicked_by = chat_member_updated.new_chat_member.restricted_by
        user = chat_member_updated.new_chat_member.user
        
        if kicked_by is not None and kicked_by.is_self:
            messagee = f"⌯ المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة بواسطة البوت"
        else:
            if kicked_by is not None:
                message = f"منع التصفيه التـلقائي 🫧\n\n⌯ المستخدم : [{kicked_by.first_name}](tg://user?id={kicked_by.id}) تـم تنزيله من قائمه الادمنيه\n⌯ السبب : حاول تصفيه مجموعتك وطرد العضو : [{user.first_name}](tg://user?id={user.id})"
                try:
                    await client.ban_chat_member(chat_member_updated.chat.id, kicked_by.id)
                except Exception as e:
                    message += f"\n\nيجب ان يكون المشرف مرفوع من البوت حتي استطيع تنزيله من الاشراف \nلـ معرفه كيفيه رفع مشرف : قم بعمل ريبلي علي الشخص المحدد واكتب رفع مشرف"
            else:
                message = f"⌯ المستخدم {user.username} ({user.first_name}) ⌯ تم طرده من الدردشة"
            
            
        
        await client.send_message(chat_member_updated.chat.id, message)



@app.on_message(filters.command(["رفع مشرف"], "") & filters.group)
def promote_g_admin(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[1]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    tom_id = message.from_user.id
    chat_id = message.chat.id
    ToM= ChatPrivileges(
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_promote_members=False,
                    can_change_info=False,
                    can_post_messages=False,
                    can_edit_messages=False,
                    can_invite_users=True,
                    can_pin_messages=True,
                    is_anonymous=False
                )
    tooom = client.get_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS)
    for tom in tooom:
    	if tom.user.id == tom_id and (tom.status == enums.ChatMemberStatus.OWNER or tom.status == enums.ChatMemberStatus.ADMINISTRATOR):
    		client.promote_chat_member(chat_id, user_id, ToM)
    		message.reply(f"⌯ تم رفع {user_id} ادمن بنجاح \n\n √")
