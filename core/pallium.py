import random
import g
import time

class Pallium:
    def __init__(self):
        print("皮层初始化...")

        self.actions=['0','1','2']


    def receive_ok(self):
        print("皮层接收ok")
        leftScore = 0
        rightScore = 0
        forwardScore = 0
        for n in range(10):#遍历最后一排元
            if len(g.brain.neures[9][n].frameFeatures)>0:
                if 90+n<93:
                    leftScore = leftScore+1
                elif 90+n>96:
                    rightScore =rightScore+1
                else:
                    forwardScore = forwardScore+1
        #得出结论
        #print(leftScore,rightScore,forwardScore)
        if leftScore>rightScore and leftScore>forwardScore:
            g.client.send("0")
            print("指令是 0")
        elif rightScore > leftScore and rightScore > forwardScore:
            g.client.send("1")
            print("指令是 1")
        elif forwardScore > leftScore and forwardScore > rightScore:
            g.client.send("2")
            print("指令是 2")
        else:
            print("没有明确动作，做一个随机动作")
            g.feedback.update("no")  # 改变状态

        #做出动作后等一下反馈
        print("等待反馈中...")
        time.sleep(0.5)
        isok = False;
        #查看当前的反馈情况
        if g.feedback.state == "no":
            g.feedback.update("default")#改变状态
            print("收到一个不好的反馈，接下来对自身做出调整！")
            isok=False
            time.sleep(2)
        else:
            print("刚才做出了正确的选择！")
            time.sleep(2)
            isok = True
        # 进行一步反馈更新
        g.brain.update(isok)
        # 增加帧数
        print("增加帧数...")
        g.updateFrame(isok)
        print("======================================================")
        print("======================================================")