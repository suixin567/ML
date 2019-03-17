from core.pallium import Pallium
import g
import random

class Neure:
    # 初始化皮层
    pallium = Pallium()

    def __init__(self,id,row):
        self.id = id
        self.activate = False
        # print("元",id,row)

    def receive(self,feature,intensity):
        print("元",self.id," 接收：",feature,"强度",intensity)
        self.activate =True
        #记录一个特征
        #先获取这个特征的intensity
        intensity = 0
        temp = g.r.get("neure" + str(self.id) + "_" + feature)
        if temp == None:
            intensity = 0
        else:
            intensity = int(temp)  # 获取唯一索引号 int类型
            intensity = intensity + 1
        g.r.set("neure" + str(self.id) + "_" + feature,intensity)

        #传递到皮层
        # self.pallium.receive(_from)

    #判断对某个特征的熟悉程度
    def familiar(self,feature): #feature的样子： 13_vertical_
        # print("特征的样子",feature)
        #元查看自己的记忆。具体格式为： neure78_13_vertical
        result = g.r.get("neure"+str(self.id)+"_"+feature)
        if result == None:
            return -1
        else:
            return int(result)






