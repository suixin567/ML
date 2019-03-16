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

    def receive(self,_from):
        print("元",self.id," 接收：",_from)
        # self.activate =True
        #记录是谁发给自己的
        # g.r.set("neure"+self.id,id)
        #传递到皮层
        # self.pallium.receive(_from)

    # def send(self):
    #     print("发送")
    #     #记录自己发给谁
    #     # g.r.set("neure"+self.id,id)
    #     self.activate = False

    #判断对某个特征的熟悉程度
    def familiar(self,fature): #feature的样子： 13_vertical_
        # print("特征的样子",fature)
        #元查看自己的记忆。具体格式为： neure78_13_vertical
        result = g.r.get("neure"+str(self.id)+"_"+fature)
        if result == None:
            return -1
        else:
            return int(result)



