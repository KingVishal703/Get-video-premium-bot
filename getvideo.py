from pyrogram import Client, filters
from pyrogram.types import Message
from database import is_premium, get_usage, increase_usage
from config import CHANNEL_ID
import random

@Client.on_message(filters.command("getvideo"))
async def getvideo(client, message: Message):
    user_id = message.from_user.id

    if await is_premium(user_id):
        pass  # Unlimited
    else:
        usage = await get_usage(user_id)
        if usage >= 2:
            return await message.reply("You've used your 2 free videos today.")
        await increase_usage(user_id)

    msgs = [msg async for msg in client.get_chat_history(CHANNEL_ID, limit=100)]
    videos = [m for m in msgs if m.video or m.document or m.animation]
    if not videos:
        return await message.reply("No videos found.")
    video = random.choice(videos)
    await video.copy(message.chat.id)
