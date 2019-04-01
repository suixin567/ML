import redis
import random

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)  # 解决获取的值类型是bytes字节问题
r = redis.Redis(connection_pool=pool)
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

#倒序循环
# for m in range(3 , -1, -1):
#     print(m)

# list=['a','b','c','d']
# for i, val in enumerate(list):
#     print("序号：%s   值：%s" % (i, val))


# r.hset('neure12', 'name', 'Jack')
# r.hset('neure12', 'age', 20)
# r.hset('neure12', 'phone', '18712909999')
# r.hset('neure12', 'email', '123@gmail.com')
# rst = r.hgetall('neure12')
# print(rst)
# print(type(rst))
# print(r.hget('neure12','phone'))
#
# print(r.hkeys("neure12"))#获取所有keys的列表

# chance = 0.25
# temp = random.random()
# print("临时",temp)
# if temp<=0.25:
#     print("运行")

# for i in range (10):
#     # 向下传递（对每一个特征都要找到最应该传递的目标元）
#     # 遍历下一排元
#     for j in range(10):
#         print(i,j)
#         if j>3:
#             break;
#             print("ff")
#     print("运行",i)

# arr = ['a','b','c','d','e','f']
# print(arr[len(arr)-2:len(arr)])
# from threading import Thread
# import time
#
# def talk(value):
#     print("说话" ,value)
#     while 1:
#         time.sleep(3)
#         print("说话2", value)
#
#
#
# p = Thread(target=talk, args=(1,))
# p.start()
# print("主线程")

features = ['a','b','c','d','e']
for i in range(len(features) - 1, len(features) - 2 - 1, -1):  # 倒序遍历
    print(features[i])
# index=0
# for i in range(10):
#     for j in range(10):
#         index = index + 1
#         print(index)