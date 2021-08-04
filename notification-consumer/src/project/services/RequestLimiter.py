import redis
import time
import logging
import os

class RequestLimiter:
    def __init__(self):
        self.r = r = redis.from_url(os.getenv('REDIS_URL'))

    def limit(self, key, limit):
        self.r.incr(key)
        logging.info(self.r.get(key))
        if int(self.r.get(key)) >= int(limit):
            logging.info("I am waiting for a minute")
            time.sleep(60)
