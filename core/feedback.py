import g
import time


#反馈区域
class Feedback:
    def __init__(self):
        print("反馈区初始化...")
        #当前环境的状态
        self.state="good"
