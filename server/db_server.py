import redis
# create a connection to the localhost Redis server instance, by
# default it runs on port 6379
r = redis.StrictRedis(host="localhost", port=6379, db=0)
while True:
    pass