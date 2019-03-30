

#反馈区域
class Feedback:
    def __init__(self):
        print("反馈区初始化...")
        #当前环境的状态
        #这个状态默认是 default unity返回图像之后变成cameraok 然后视网膜开始加载图像，
        # 状态变为default。 得到不好的预测之后变为no，反向更新后 变为default，等待下一帧图像。
        self.state="default"


    def update(self,newState):
        self.state = newState;