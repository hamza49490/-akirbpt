from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram
from Config import Config
from datetime import datetime


app = Client(
    "MentionAll",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root='pyrogram_plugins')
)


    
app.start()
print(f"Botun pyrogram modülleri ( {pyrogram.__version__} sürümü ile başlatıldı. ")
idle()
