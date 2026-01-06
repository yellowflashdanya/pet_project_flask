import time
import redis
from flask import Flask
import os

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "redis")
cache = redis.Redis(host=redis_host, port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello! I see you {count} times.\n'
