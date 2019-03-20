# import redis
#
# pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)  # 解决获取的值类型是bytes字节问题
# r = redis.Redis(connection_pool=pool)
#
# valueList = ['a','b','c','d']
# # for val in valueList:
# #     r.rpush('tt', val)
# print(r.llen('tt'))
# print(r.lrange('tt',r.llen('tt')-3,r.llen('tt')));

# import random
#
# print(random.randint(0, 9))

# print(max(1,2,2))

for m in range(3 - 1, 0, -1):
    print(m)