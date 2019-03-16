from core.neure import Neure
import g
import random

class Brain:
    def __init__(self):
        index =-1

        self.neures = [[0 for i in range(10)] for j in range(10)]

        for i in range(10):
            for j in range(10):
                index= index+1
                neu = Neure(index,i)
                # print(index)
                self.neures[i][j]=neu
        # print(self.neures)

    def receive(self,pointer):
        print("脑开始运行...")#此list的具体内容： ['15_corner_', '13_vertical_']
        stepIndex=0
        featureList = g.r.lrange(pointer, 0,g.r.llen(pointer))  # 获取记忆的具体内容 ['15_corner_', '13_vertical_']
        for f in featureList:
            #向元传递
            familiar_neure =None#最想传给的元
            familiar_max = -1#记录哪个元最熟悉这个特征
            #遍历第一排元
            for j in range(10):
                # print(self.neures[i][j].id)
                familiar_intensity = self.neures[0][j].familiar(f)#获得熟悉程度
                if familiar_intensity > familiar_max:
                    familiar_max = familiar_intensity
                    familiar_neure = self.neures[0][j]
            if familiar_max ==-1:
                print("没有熟悉的元")
                self.neures[0][random.randint(0, 9)].receive(f,intensity=10)
                # self.neures[11].receive(pointer)
            else:
                print("找到了最熟悉的元")
                familiar_neure.receive(f,intensity=10)

        #运行到这里时，对每一个特征都传递给了第一层的元。
        print("已经传给了元，应通知元继续传递一步。")

        for m in range(10):
            for n in range(10):
                self.neures[stepIndex][n].forward()
            #全向前传递一步后，计数加一。
            stepIndex = stepIndex+1
