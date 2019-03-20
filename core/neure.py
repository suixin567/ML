from core.pallium import Pallium
import g
import random

class Neure:

    def __init__(self,id,row):
        self.id = id
        self.activate = False
        self.isEnd =False
        if row == 9:
            self.isEnd =True
        # print("元",id,row)

    def receive(self,feature):
        self.activate =True


        #先获取自己已经有的特征，有的话就别重复的添加了
        #myFeatureList = g.r.lrange('neure'+str(self.id), 0, g.r.llen('neure'+str(self.id)))
        # for f in myFeatureList:
        #     if f == feature:#此特征已经存在
        #         #先获取这个特征的intensity
        #         intensity = g.r.get("neure" + str(self.id) + "_" + feature)
        #         newIntensity = int(intensity)+1  # 获取唯一索引号 int类型
        #         g.r.set("neure" + str(self.id) + "_" + feature,newIntensity)
        #         print("我是元",self.id,"收到熟悉的特征：",feature,"最新强度值",newIntensity)
        #         # 传递到皮层
        #         if self.isEnd:
        #             g.pallium.receive(feature)
        #         return
        # 最新收集到的特征强度为1
        print("我是元",self.id,"收到最新的特征：",feature)
        g.r.rpush('neure'+str(self.id), feature)

        # 先获取这个特征的intensity
        newIntensity =0
        intensity = g.r.get("neure" + str(self.id) + "_" + feature)
        if intensity == None:
            newIntensity = 1
        else:
            newIntensity = int(intensity)+1  # 获取唯一索引号 int类型
        g.r.set("neure" + str(self.id) + "_" + feature,newIntensity)


        #传递到皮层
        if self.isEnd:
            g.pallium.receive(feature)

    #判断对某个特征的熟悉程度
    def familiar(self,feature): #feature的样子： 13_vertical_
        # print("特征的样子",feature)
        #元查看自己的记忆。具体格式为： neure78_13_vertical
        result = g.r.get("neure"+str(self.id)+"_"+feature)
        if result == None:
            return -1
        else:
            return int(result)






