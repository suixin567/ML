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

        featureList = g.r.lrange(pointer, 0,g.r.llen(pointer))  # 获取记忆的具体内容 ['15_corner_', '13_vertical_']
        #传给第一排元
        self.transmitMethod(featureList,0)

        #传递接下来每一排的元
        for i in range(1,10):
            print("准备传递至第", i, "层")
            for j in range(10):
                neure=self.neures[i][j]
                #获取这个元的特征列表
                nuure_features = g.r.keys(pattern='neure' + str(neure.id) + '*')
                self.transmitMethod(nuure_features,i)

    #单个元的传递规则 根据特征List向下传递一层
    def  transmitMethod(self,featureList,stepIndex):

        for f in featureList:
            #向下传递（对每一个特征都要找到最应该传递的目标元）
            familiar_neure =None#最想传给的元
            familiar_max = -1#记录哪个元最熟悉这个特征
            #遍历下一排元
            for j in range(10):
                # print(self.neures[i][j].id)
                familiar_intensity = self.neures[stepIndex][j].familiar(f)#获得熟悉程度
                if familiar_intensity > familiar_max:
                    familiar_max = familiar_intensity
                    familiar_neure = self.neures[stepIndex][j]
            if familiar_max ==-1:
                #print("没有熟悉的元")
                self.neures[stepIndex][random.randint(0, 9)].receive(f,intensity=10)
            else:
                #print("找到了最熟悉的元")
                familiar_neure.receive(f,intensity=10)

