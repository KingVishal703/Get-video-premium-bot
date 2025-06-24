from pymongo import MongoClient
from config import MONGO_URL
from datetime import datetime, timedelta

client = MongoClient(MONGO_URL)
db = client["GetVideoBot"]
users = db["users"]

async def add_user(user_id):
    if not users.find_one({"_id": user_id}):
        users.insert_one({
            "_id": user_id,
            "used_today": 0,
            "premium_until": None,
            "last_used": None
        })

async def is_premium(user_id):
    user = users.find_one({"_id": user_id})
    if user and user.get("premium_until"):
        return datetime.utcnow() < user["premium_until"]
    return False

async def increase_usage(user_id):
    users.update_one({"_id": user_id}, {"$inc": {"used_today": 1}})

async def reset_daily_usage():
    users.update_many({}, {"$set": {"used_today": 0}})

async def get_usage(user_id):
    user = users.find_one({"_id": user_id})
    return user.get("used_today", 0) if user else 0

async def give_premium(user_id, days=1):
    expiry = datetime.utcnow() + timedelta(days=days)
    users.update_one({"_id": user_id}, {"$set": {"premium_until": expiry}})
