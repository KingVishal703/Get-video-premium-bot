from pyrogram import Client, filters
from pyrogram.types import Message
from config import ADMINS
from database import client as mongo_client

users_col = mongo_client["GetVideoBot"]["users"]

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def broadcast_handler(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a message you want to broadcast.")

    sent = 0
    failed = 0

    async for user in users_col.find({}, {"_id": 1}):
        try:
            await message.reply_to_message.copy(user["_id"])
            sent += 1
        except:
            failed += 1

    await message.reply(f"✅ Broadcast complete.\n\n✔️ Sent: {sent}\n❌ Failed: {failed}")
