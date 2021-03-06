from core.pallium import Pallium
import g
import random


class Neure:
    def __init__(self,id,row):
        self.id = id
        # print("元",id,row)
        self.frameFeatures=[]#当前帧收到的特征。

    def receive(self,feature):
        self.frameFeatures.append(feature)
        # 最新收集到的特征强度为1
        print("我是元",self.id,"收到特征：",feature,"第",len(self.frameFeatures),"个特征")

    #判断对某个特征的熟悉程度
    def familiar(self,feature): #feature的样子： 13_vertical_
        #判断一下自己是否接收这个特征首先便利自己的特征列表
        features = g.r.hkeys("neure"+str(self.id))  # 获取所有keys的列表
        # print("我是元",self.id,"特征列表是",features)
        for i in range(len(features)-1, -1, -1):#倒序遍历
            if feature == features[i]:#如果存在这个特征
                value = g.r.hget("neure" + str(self.id), features[i])
                # print(value)
                rand = random.random()
                # print("临时", rand)
                if rand <= float(value):#落在了机会范围内则被选中
                    # print("我是元",self.id,"对特征",features[i],"的几率是",value,"随机值是",rand,"交给我吧！")
                    return True
        return False


    #元的反馈更新todo: 这里存在问题：同一个元在同一帧内接受了多个特征的话，对每个特征的惩罚是递减的，但同一帧下应统一削弱。
    def update(self,isok):
        if len(self.frameFeatures)>0:
            if isok == True:#好的反馈
                for f in self.frameFeatures:
                    g.r.hset('neure' + str(self.id), f, 1)
                self.frameFeatures = []
            else:#不好的反馈
                self.frameFeatures = []



        # features = g.r.hkeys("neure" + str(self.id))  # 获取所有keys的列表
        # if len(features) == 0:
        #     return
        # print("元进行反馈更新：我是元", self.id, "特征列表是", features)
        # count = 0
        # for i in range(len(features) - 1, -1, -1):  # 倒序遍历
        #     value = g.r.hget("neure" + str(self.id), features[i])
        #     newValue = float(value)-float(value)*(rate**count)
        #     print("更新后,元",self.id,"的特征",features[i],"的最新值是",newValue)
        #     g.r.hset("neure" + str(self.id), features[i], newValue)
        #     if newValue<=0:#移出这个特征
        #         g.r.hdel("neure" + str(self.id),features[i])
        #         ttvalue = g.r.hget("neure" + str(self.id), features[i])
        #         # print("已经删除了应该是None",ttvalue)
        #     count = count + 1

        #只更新上次收到的特征
        # for i in range(len(features) - 1, len(features)-self.newFeatureAmount-1, -1):  # 倒序遍历
        #     print("元",self.id,"正在更新特征。",i,features[i]);
        #     g.r.hdel("neure" + str(self.id), features[i])
            #ttvalue = g.r.hget("neure" + str(self.id), features[i])
            #print("已经删除了应该是None",ttvalue)


