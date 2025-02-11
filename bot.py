from pyrogram import Client, filters

# إعداد بيانات البوت
api_id = 123456  # استبدله بـ API ID الخاص بك
api_hash = "your_api_hash"  # استبدله بـ API Hash الخاص بك
bot_token = "7671239821:AAH_uCEakDeMwzOpyIcb9bioDnZxjDE_pG8"  # تم استبدال التوكن هنا

app = Client("music_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("مرحبا! أنا بوت الموسيقى 🎵")

app.run()
