import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)  # 解决获取的值类型是bytes字节问题
r = redis.Redis(connection_pool=pool)

valueList = ['a','b']
for val in valueList:
    r.rpush('tt', val)

print(r.lrange('tt',0,r.llen('tt')));