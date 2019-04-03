import redis
from core.pallium import Pallium
from core.brain import Brain
from core.feedback import Feedback
import tools.client
from core.feedback import State

# 全局数据库
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)  # 解决获取的值类型是bytes字节问题
r = redis.Redis(connection_pool=pool)

#全局运行状态
run = True

# 全局帧
frame =0
temp = r.get("frame")
if temp == None:
    frame = 0
else:
    frame = int(r.get("frame"))
print("初始化redis...历史帧：", frame)


def updateFrame(isok=False):
    global frame
    r.set("frame",frame+1)
    frame  = frame+1
    # 通知unity截图
    if isok ==True:#只有上次做对了才会切换物体。
        client.send("camera")
    else:
        feedback.update(State.CAMERA_OK)

#全局brain
brain = Brain()

#全局皮层
pallium = Pallium()

# 初始化反馈区
feedback = Feedback()

#初始化套接字
client = tools.client.Client()




#当前问题 ：
#1、bad反馈需要在下一帧中才能体现     ok
#2、管道用时太长
#3、反馈的效果不好，依旧会走错的路。ok