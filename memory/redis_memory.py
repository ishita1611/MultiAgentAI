import redis
import json

class SharedMemory:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def log(self, key, data):
        self.redis.set(key, json.dumps(data))

    def get(self, key):
        val = self.redis.get(key)
        return json.loads(val) if val else None

    def exists(self, key):
        return self.redis.exists(key)

    def clear_all(self):  # optional: use to reset
        self.redis.flushdb()

