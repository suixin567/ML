import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)  # 解决获取的值类型是bytes字节问题
r = redis.Redis(connection_pool=pool)
r.rpush('aa', 1, 2)
print(r.lrange('aa',0,r.llen('aa')));