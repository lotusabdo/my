from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_ID
from AbdoX import app

async def is_admin_or_owner(client, chat_id, user_id):
    member = await client.get_chat_member(chat_id, user_id)
    return member.status in ["administrator", "creator"] or user_id == OWNER_ID

@app.on_message(filters.regex(r"^(طرد|حظر)( .+)?$"))
async def kick_or_ban_member(client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if not await is_admin_or_owner(client, chat_id, user_id):
        await message.reply_text("هذا الأمر مخصص للمشرفين فقط.")
        return

    command = message.text.split()[0]
    if message.reply_to_message:
        target_user_id = message.reply_to_message.from_user.id
    elif len(message.text.split()) > 1:
        target_user_id = message.text.split()[1]
        if target_user_id.isdigit():
            target_user_id = int(target_user_id)
    else:
        await message.reply_text("الاستخدام: طرد [اسم المستخدم أو المعرف] أو الرد على رسالة العضو بكلمة طرد")
        return

    try:
        if command == "طرد":
            await client.kick_chat_member(chat_id, target_user_id)
            await message.reply_text("تم طرد المستخدم بنجاح.")
        elif command == "حظر":
            await client.ban_chat_member(chat_id, target_user_id)
            await message.reply_text("تم حظر المستخدم بنجاح.")
    except Exception as e:
        await message.reply_text(f"حدث خطأ أثناء تنفيذ الأمر: {e}")

if __name__ == "__main__":
    app.run()
