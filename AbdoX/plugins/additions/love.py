from pyrogram import Client, filters
import random
from AbdoX import app

def get_random_message(love_percentage):
    if love_percentage <= 30:
        return random.choice([
            "الحب بينكم موجود ولكنه يحتاج إلى القليل من الشغف.",
            "بداية جيدة لكن يحتاج حبكم الى النمو.",
        ])
    elif love_percentage <= 70:
        return random.choice([
            "هناك اتصال قوي بينكم. كونوا بجانب بعضكم البعض.",
            "لديك فرصة جيدة. قم بالعمل عليها.",
            "الحب يزدهر!, استمر."
        ])
    else:
        return random.choice([
            "رائع! إنها علاقة صنعت في الجنة!!",
            "علاقة رائعة! اعتز بهذا السند.",
            "مُقدر أن تكونوا معًا. تهانينا!"
        ])

@app.on_message(filters.regex(r"\bنسبة الحب\b"))
def love_command(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        name1 = args[0].strip()
        name2 = args[1].strip()
        
        love_percentage = random.randint(10, 100)
        love_message = get_random_message(love_percentage)

        response = f"{name1} ♥ + {name2} ♥ = {love_percentage}%\n\n{love_message}"
    else:
        response = "قم بكتابة اسمين بعد أمر نسبة الحب."
    app.send_message(message.chat.id, response)
