# utils/memory.py
import redis
import pickle
from iioksana.config import REDIS_URL

class Memory:
    def __init__(self):
        self.redis_client = redis.Redis.from_url(REDIS_URL)

    def save_user_profile(self, user_id, profile_data):
        key = f"user_profile:{user_id}"
        self.redis_client.set(key, pickle.dumps(profile_data))

    def get_user_profile(self, user_id):
        key = f"user_profile:{user_id}"
        data = self.redis_client.get(key)
        if data:
            return pickle.loads(data)
        else:
            return None

    def save_chat_history(self, user_id, chat_history):
        key = f"chat_history:{user_id}"
        self.redis_client.set(key, pickle.dumps(chat_history))

    def get_chat_history(self, user_id):
        key = f"chat_history:{user_id}"
        data = self.redis_client.get(key)
        if data:
            return pickle.loads(data)
        else:
            return []

    def clear_chat_history(self, user_id):
        key = f"chat_history:{user_id}"
        self.redis_client.delete(key)
