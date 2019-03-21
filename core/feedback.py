import g
import time


#反馈区域
class Feedback:
    def __init__(self):
        print("反馈区初始化...")


    def send(self,action):
        print("发送了一个命令",action)
        #发送后等待环境反馈
        time.sleep(1)
        self.receive()

    def receive(self):
        print("模拟一个不好的反馈")
        g.pallium.env_feedback(False)
