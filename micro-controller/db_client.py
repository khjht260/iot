import redis

redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)

print(redis_db.get('gender'))