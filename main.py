import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped

# إعدادات البوت
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("QuranStream", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call_py = PyTgCalls(app)

# رابط الإذاعة (قرآن مكة المكرمة 24 ساعة)
STREAM_URL = "https://broadcast.quran.com.sa/radio/8006/radio.mp3"

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text("البوت يعمل! أضفني للقناة وأرسل /play للبدء.")

@app.on_message(filters.command("play"))
async def play(client, message):
    chat_id = message.chat.id
    await call_py.join_group_call(
        chat_id,
        AudioPiped(STREAM_URL),
        stream_type=StreamType().pulse_stream,
    )
    await message.reply_text("بدأ البث المباشر للقرآن الكريم الآن 24/7.")

app.start()
call_py.run()
