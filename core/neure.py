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
        self.newFeatureAmount=0#当前帧收到的最近特征个数，（只会传递相应个数的特征到下一层，太过之前的不会进行传递。）


    def receive(self,feature):
        self.activate =True
        self.newFeatureAmount= self.newFeatureAmount+1
        # 最新收集到的特征强度为1
        print("我是元",self.id,"收到最新的特征：",feature,"当前帧我收到的第",self.newFeatureAmount,"个特征")
        g.r.hset('neure'+str(self.id), feature, 1)
        #传递到皮层
        if self.isEnd:
            g.pallium.receive(feature)

    #判断对某个特征的熟悉程度
    def familiar(self,feature): #feature的样子： 13_vertical_
        #判断一下自己是否接收这个特征首先便利自己的特征列表
        features = g.r.hkeys("neure"+str(self.id))  # 获取所有keys的列表
        print("我是元",self.id,"特征列表是",features)
        for i in range(len(features)-1, -1, -1):#倒序遍历
            if feature == features[i]:#如果存在这个特征
                value = g.r.hget("neure" + str(self.id), features[i])
                print(value)
                rand = random.random()
                print("临时", rand)
                if rand <= float(value):#落在了机会范围内则被选中
                    print("我是元",self.id,"对特征",features[i],"的几率是",value,"随机值是",rand,"交给我吧！")
                    return True
        return False



    def update(self):
        print("元进行反馈更新");
        return
        reduce=1#衰减多少
        rate =0.5#衰减率
        featureAmount = g.r.llen('neure' + str(self.id))
        print("特征个数",featureAmount)
        myFeatureList = g.r.lrange('neure'+str(self.id), 0, featureAmount)
        print("特征列表", myFeatureList)

        # for i, f in enumerate(myFeatureList):
        #     reduce = rate**i
        #     #先获取这个特征的intensity
        #     intensity = g.r.get("neure" + str(self.id) + "_" + f)
        #     print("我是元",self.id,"特征是",f,"强度是",intensity)
        #     newIntensity = int(intensity) - int(intensity)*reduce
        #     print("新强度是",newIntensity)
        #     g.r.set("neure" + str(self.id) + "_" + f,newIntensity)

        count=0
        #倒序循环
        for m in range(featureAmount-1, -1, -1):#m是从大到小的顺序
            count=count+1


            print(m,myFeatureList[m])





