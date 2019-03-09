import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)  # 解决获取的值类型是bytes字节问题
r = redis.Redis(connection_pool=pool)

frame =0

temp = r.get("frame")
if temp == None:
    frame = 0
else:
    frame = int(r.get("frame"))  # 获取唯一索引号 int类型
print("初始化redis...历史帧：", frame)


def updateFrame():
    r.set("frame",frame+1)