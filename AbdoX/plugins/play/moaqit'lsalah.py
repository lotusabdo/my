from requests import Session
from requests import Response
from typing import Union
from pyrogram import Client, filters
from pyrogram.types import Message
from config import *
from AbdoX  import app 

s = Session()
@app.on_message(filters.regex(r"^(مواقيت صلاة|مواقيت صلاه|صلوات)"))
async def sendAdhan(_: Client, message: Message) -> None:
    address: str = message.text.rsplit(maxsplit=1)[-1]
    if address in ["مواقيت صلاة", "مواقيت صلاه", "صلوات"]: return await message.reply("- اكتب اسم المنطقه بجانب الأمر،")
    adhan: Union[str, bool] = getAdhan(address)
    if not adhan: return await message.reply("- حدث خطأ أثناء جلب مواقيت الصلاة.", reply_to_message_id=message.id)
    await message.reply(adhan, reply_to_message_id=message.id)    


pnames: dict = {
    'Fajr': "الفجر", 
    'Sunrise': "الشروق", 
    'Dhuhr': "الظهر", 
    'Asr': "العصر",
    'Maghrib': "المغرب", 
    'Isha': "العشاء", 
    'Imsak': "الامساك",
    'Midnight': "منتصف الليل", 
    'Firstthird': "الثلث الأول من الليل", 
    'Lastthird': "الثلث الأخير من الليل"
}


def getAdhan(address: str) -> Union[str, bool]:
    method: int = 1
    params = {
        "address" : address,
        "method" : method, 
        "school" : 0
    }
    res: Response = s.get("http://api.aladhan.com/timingsByAddress", params=params)
    data: dict = res.json()
    if data["code"] != 200: return False
    data: dict = data["data"]
    timings: dict = data["timings"]
    date: dict = data["date"]["hijri"]
    date2: dict = data["date"]["gregorian"]
    month2: str = date2["month"]["en"]
    weekday: str = date["weekday"]["ar"] + " - " + date["weekday"]["en"]
    month: str = date["month"]["ar"] + " - " + date["month"]["en"]
    date: str = date["date"]
    date2: str = date2["date"]
    del timings['Sunset']
    next: str = getNext(timings)
    caption = f"- {next}\n"
    caption += f"- مواقيت الصلاة:"
    for prayer, time in timings.items():
        caption += f"\n    - {pnames[prayer]}: {time}"
    caption += f"\n\n- بـتـاريـخ: {date} (هـ) | {date2} (م)\n- يـوم: {weekday}\n- بـشـهـر: {month} (هـ) | {month2} (م)"
    return caption
    
    
def getNext(timings: dict) -> str:
    current_time = datetime.now(zone).strftime("%H:%M")
    next_prayer = None
    for prayer, time in timings.items():
        if current_time < time:
            next_prayer = prayer
            break
    if next_prayer is None: return "انتهت صلوات اليوم."
    next_prayer_time = datetime.strptime(timings[next_prayer], "%H:%M")
    current_time = datetime.strptime(current_time, "%H:%M")
    time_difference = next_prayer_time - current_time
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"متبقى على صلاة {pnames[next_prayer]} {hours} ساعه و {minutes} دقيقه."



