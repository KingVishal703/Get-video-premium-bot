from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import FORCE_SUB_CHANNEL
from database import add_user, is_premium

@Client.on_message(filters.command("start"))
async def start(client, message: Message):
    user_id = message.from_user.id
    await add_user(user_id)

    # Force Subscribe
    try:
        member = await client.get_chat_member(FORCE_SUB_CHANNEL, user_id)
        if member.status == "kicked":
            return await message.reply("You are banned.")
    except:
        return await message.reply(
            f"Join @{FORCE_SUB_CHANNEL} first!",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Join Channel", url=f"https://t.me/{FORCE_SUB_CHANNEL}")]]
            )
        )

    # Premium check
    if await is_premium(user_id):
        await message.reply("Welcome back Premium user! Use /getvideo")
    else:
        await message.reply(
            "You're on free plan (2 video/day). Want Premium?",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Get Premium (Verify)", url="https://short.domain/abc123")]]
            )
        )
