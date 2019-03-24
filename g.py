import redis
from core.pallium import Pallium
from core.brain import Brain
from core.feedback import Feedback
import tools.client
from retina import Retina

# 全局数据库
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)  # 解决获取的值类型是bytes字节问题
r = redis.Redis(connection_pool=pool)

# 全局帧
frame =0
temp = r.get("frame")
if temp == None:
    frame = 0
else:
    frame = int(r.get("frame"))
print("初始化redis...历史帧：", frame)


def updateFrame():
    global frame
    r.set("frame",frame+1)
    frame  = frame+1

#全局brain
brain = Brain()

#全局皮层
pallium = Pallium()

# 初始化反馈区
feedback = Feedback()

#初始化套接字
client = tools.client.Client()

#初始化视网膜
retina = Retina()


#当前问题 ：
#1、bad反馈需要在下一帧中才能体现
#2、管道用时太长
#3、反馈的效果不好，依旧会走错的路。