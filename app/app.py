import time
import redis
from flask import Flask
import os

app = Flask(__name__)

if os.environ.get("TESTING") == "True":
    class FakeRedis:
        def incr(self, key): return 1
    cache = FakeRedis()
else:
    cache = redis.Redis(host='redis', port=6379)


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
