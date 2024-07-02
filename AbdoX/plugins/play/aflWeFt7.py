import json
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus, MessageMediaType
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from AbdoX import app

class ChatPermissions:
    def __init__(
        self, all_locked=False, chat_locked=False, photo_locked=False,
        video_locked=False, link_locked=False, sticker_locked=False,
        forward_locked=False, reply_locked=False, voice_locked=False
    ):
        self.all_locked = all_locked
        self.chat_locked = chat_locked
        self.photo_locked = photo_locked
        self.video_locked = video_locked
        self.link_locked = link_locked
        self.sticker_locked = sticker_locked
        self.forward_locked = forward_locked
        self.reply_locked = reply_locked
        self.voice_locked = voice_locked

settings_file = "group_settings.json"

def get_group_permissions(chat_id):
    try:
        with open(settings_file, "r") as file:
            settings = json.load(file)
            group_settings = settings.get(str(chat_id))
            if group_settings:
                expected_keys = {'all_locked', 'chat_locked', 'photo_locked', 'video_locked', 'link_locked', 'sticker_locked', 'forward_locked', 'reply_locked', 'voice_locked'}
                clean_settings = {k: v for k, v in group_settings.items() if k in expected_keys}
                permissions = ChatPermissions(**clean_settings)
                return permissions
    except FileNotFoundError:
        pass
    return ChatPermissions()

def save_group_permissions(chat_id, permissions):
    try:
        with open(settings_file, "r") as file:
            settings = json.load(file)
    except FileNotFoundError:
        settings = {}
    settings[str(chat_id)] = permissions.__dict__
    with open(settings_file, "w") as file:
        json.dump(settings, file, indent=2)

permissions = [
    ("إغلاق الكل", "all_locked"),
    ("قفل الدردشه", "chat_locked"),
    ("قفل الصور", "photo_locked"),
    ("قفل الفيديوز", "video_locked"),
    ("قفل الصوتيات", 'voice_locked'),
    ("قفل اللينكات", "link_locked"),
    ("قفل الإستيكر", "sticker_locked"),
    ("قفل التحويل", "forward_locked"),
    ("قفل الرد", "reply_locked")
]

@app.on_message(filters.command(["ترتيب الاوامر"], ""), group=100)
async def command_buttons(client: Client, message: Message):
    chat_id = message.chat.id
    member_status = await client.get_chat_member(chat_id, message.from_user.id)
    
    if member_status.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        chat_permissions = get_group_permissions(chat_id)
        if chat_permissions is None:
            chat_permissions = ChatPermissions()
        keyboard = []
        for permission_name, permission_key in permissions:
            button_text = permission_name + " ✅" if getattr(chat_permissions, permission_key) else permission_name + " ❌"
            boolean = "-True" if getattr(chat_permissions, permission_key) else "-False"
            keyboard.append([InlineKeyboardButton(button_text, callback_data=f"{permission_key}{boolean}-permissions")])
        keyboard.append([InlineKeyboardButton("اغلاق", callback_data="permission-save")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await message.reply_text("قم بإختيار الصلاحيات المطلوبة :", reply_markup=reply_markup)
    else:
        await message.reply_text("مفكر نفسك ادمن ياروح امك")

@app.on_callback_query(filters.regex("permissions"), group=200)
async def handle_callback_query(client: Client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    member_status = await client.get_chat_member(chat_id, callback_query.from_user.id)
    if member_status.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        data = callback_query.data
        chat_permissions = get_group_permissions(chat_id)
        if data.endswith("-permissions"):
            permission_key, boolean = data.rsplit("-", 2)[:2]
            new_status = not getattr(chat_permissions, permission_key)
            setattr(chat_permissions, permission_key, new_status)
            save_group_permissions(chat_id, chat_permissions)
            keyboard = []
            for perm_name, perm_key in permissions:
                status = getattr(chat_permissions, perm_key)
                button_text = f"{perm_name} {'✅' if status else '❌'}"
                keyboard.append([InlineKeyboardButton(button_text, callback_data=f"{perm_key}-{'True' if status else 'False'}-permissions")])
            keyboard.append([InlineKeyboardButton("إغلاق 🚶", callback_data="permissions-save")])
            reply_markup = InlineKeyboardMarkup(keyboard)
            await callback_query.edit_message_text(
                text="قم بإختيار الصلاحيات المطلوبة:",
                reply_markup=reply_markup
            )
            await callback_query.answer("تم عزيزي الادمن تغير الصلاحية بنجاح ⚡")
        elif data == "permissions-save":
            await callback_query.edit_message_text("**تم حفظ الإعدادات ✅️**")
            await callback_query.message.delete()
    else:
        await callback_query.answer("لما تكبر ياصغنن هنفذلك الامر ده حاضر ", show_alert=True)

@app.on_message(filters.all, group=300)
async def check_permissions(client: Client, message: Message):
    chat_id = message.chat.id
    chat_permissions = get_group_permissions(chat_id)
    if chat_permissions.all_locked:
        await message.delete()
        await client.send_message(chat_id, "تم حذف الرسالة: جميع الرسائل مقفلة هنا.")
    elif chat_permissions.chat_locked and message.text and not message.entities and not message.reply_to_message:
        await message.delete()
        await client.send_message(chat_id, "تم حذف الرسالة: الدردشة مقفلة هنا.")
    elif chat_permissions.photo_locked and message.media == MessageMediaType.PHOTO:
        await message.delete()
        await client.send_message(chat_id, "تم حذف الرسالة: الصور مقفلة هنا.")
    elif chat_permissions.video_locked and (message.media == MessageMediaType.VIDEO or message.media == MessageMediaType.ANIMATION):
        await message.delete()
        await client.send_message(chat_id, "تم حذف الرسالة: الفيديوهات مقفلة هنا.")
    elif chat_permissions.sticker_locked and message.media == MessageMediaType.STICKER:
        await message.delete()
        await client.send_message(chat_id, "تم حذف الرسالة: الملصقات مقفلة هنا.")
    elif chat_permissions.link_locked and message.entities:
        await message.delete()
        await client.send_message(chat_id, "تم حذف الرسالة: الروابط مقفلة هنا.")
    elif chat_permissions.reply_locked and message.reply_to_message:
        await message.delete()
        await client.send_message(chat_id, "تم حذف الرسالة: الردود مقفلة هنا.")
    elif chat_permissions.forward_locked and (message.forward_from or message.forward_from_chat):
        await message.delete()
        await client.send_message(chat_id, "تم حذف الرسالة: التحويلات مقفلة هنا.")
    elif chat_permissions.voice_locked and message.media == MessageMediaType.VOICE:
        await message.delete()
        await client.send_message(chat_id, "تم حذف الرسالة: الرسائل الصوتية مقفلة هنا.")

# تشغيل التطبيق
if __name__ == "__main__":
    app.run()
