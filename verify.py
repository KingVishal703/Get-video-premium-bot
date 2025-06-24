from pyrogram import Client, filters
from pyrogram.types import Message
from database import is_premium, give_premium

@Client.on_message(filters.command("verify"))
async def verify(client, message: Message):
    user_id = message.from_user.id

    if await is_premium(user_id):
        return await message.reply("You're already a premium user.")

    # You can improve this with actual shortlink open verification later
    await give_premium(user_id, days=1)
    await message.reply("✅ Premium activated for 1 day! Use /getvideo now.")
