from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import getvideo
import start
import verify
import broadcast

app = Client("getvideobot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

app.run()
