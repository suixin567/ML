import random
import g
import time
import numpy as np

#皮层元
class PalliumNeure:
    def __init__(self,id):
        self.id = id
        self.activate = False
        #print("皮层元",id)


    def receive(self,feature):
        # self.activate =True
        # print("我是皮层元", self.id, "收到最新的特征：", feature)
        # g.r.rpush('palliumneure' + str(self.id), feature)
        # # 先获取这个特征的intensity
        # newIntensity = 0
        # intensity = g.r.get("palliumneure" + str(self.id) + "_" + feature)
        # if intensity == None:
        #     newIntensity = 1
        # else:
        #     newIntensity = int(intensity) + 1  # 获取唯一索引号 int类型
        # g.r.set("palliumneure" + str(self.id) + "_" + feature, newIntensity)
        self.activate = True

        # 最新收集到的特征强度为1
        # print("我是皮层元", self.id, "收到最新的特征：", feature)
        g.r.hset('palliumneure' + str(self.id), feature, 1)


    #判断对某个特征的熟悉程度
    def familiar(self,feature): #feature的样子： 13_vertical_
        # # print("特征的样子",feature)
        # #元查看自己的记忆。具体格式为： neure78_13_vertical
        # result = g.r.get("palliumneure"+str(self.id)+"_"+feature)
        # if result == None:
        #     return -1
        # else:
        #     return int(result)

        # 判断一下自己是否接收这个特征首先便利自己的特征列表
        features = g.r.hkeys("palliumneure" + str(self.id))  # 获取所有keys的列表
        # print("我是皮层元", self.id, "特征列表是", features)
        for i in range(len(features) - 1, -1, -1):  # 倒序遍历
            if feature == features[i]:  # 如果存在这个特征
                value = g.r.hget("palliumneure" + str(self.id), features[i])
                # print(value)
                rand = random.random()
                # print("临时", rand)
                if rand <= float(value):  # 落在了机会范围内则被选中
                    # print("我是皮层元", self.id, "对特征", features[i], "的几率是", value, "随机值是", rand, "交给我吧！")
                    return True
        return False



    #元的反馈更新todo: 这里存在问题：同一个元在同一帧内接受了多个特征的话，对每个特征的惩罚是递减的，但同一帧下应统一削弱。
    def update(self):
        rate =0.5#衰减率
        features = g.r.hkeys("palliumneure" + str(self.id))  # 获取所有keys的列表
        if len(features) == 0:
            return
        # print("皮层元进行反馈更新：我是皮层元", self.id, "特征列表是", features)
        count = 0
        for i in range(len(features) - 1, -1, -1):  # 倒序遍历
            value = g.r.hget("palliumneure" + str(self.id), features[i])
            newValue = float(value)-float(value)*(rate**count)
            # print("更新后,皮层元",self.id,"的特征",features[i],"的最新值是",newValue)
            g.r.hset("palliumneure" + str(self.id), features[i], newValue)
            if newValue<=0:#移出这个特征
                g.r.hdel("palliumneure" + str(self.id),features[i])
                ttvalue = g.r.hget("palliumneure" + str(self.id), features[i])
                # print("已经删除了应该是None",ttvalue)

            count = count + 1



class Pallium:
    def __init__(self):
        print("皮层初始化...")

        self.palliumNeures=[]
        self.features = []  # 当前帧皮层收到的特征列表

        self.actions=['0','1','2']

        for i in range(10):
                palliumNeure = PalliumNeure(i)
                self.palliumNeures.append(palliumNeure)



    def receive(self,feature):
        # print("皮层收到一个特征...",feature)
        self.features.append(feature)


    def receive_ok(self):
        print("皮层接收ok")
        #把特征分配给每个皮层元
        self.transmitMethod(self.features)
        #特征都分配给皮层元之后现在该做出判断了
        print("现在该做出判断了",self.features);
        leftScore = 0
        rightScore = 0
        forwardScore = 0
        for i in self.palliumNeures:
            if i.activate:
                # print("我是激活的",i.id)
                if i.id<3:
                    leftScore = leftScore+1
                elif i.id>6:
                    rightScore =rightScore+1
                else:
                    forwardScore = forwardScore+1
        #得出结论
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
            g.client.send(np.random.choice(self.actions))

        #做出动作后等一下反馈
        print("等待反馈中...")
        time.sleep(2)
        #查看当前的反馈情况
        if g.feedback.state == "no":
            g.feedback.state = "default"#改变状态
            print("收到一个不好的反馈，接下来对自身做出调整！")
            # 进行一步反馈更新
            g.brain.update()
            g.pallium.update()
        else:
            print("刚才做出了正确的选择！")
        time.sleep(3)

        #重置特征列表
        self.features = []
        print("重置皮层",self.features)
        # 增加帧数
        print("增加帧数...")
        g.updateFrame()



   #单个元的传递规则 根据特征List向下传递一层
    def  transmitMethod(self,featureList):
        print("准备分配给皮层元")
        for f in featureList:
            #向下传递（对每一个特征都要找到最应该传递的目标元）
            #遍历下一排元
            isAccept = False  # 此特征是否被接收
            for j in range(10):
                # print(self.neures[i][j].id)
                isAccept = self.palliumNeures[j].familiar(f)#获得熟悉程度
                if isAccept == True:
                    # print("找到了最熟悉的元")
                    self.palliumNeures[j].receive(f)
                    break
            if isAccept == False:
                #print("没有熟悉的元")
                self.palliumNeures[random.randint(0, 9)].receive(f)


    #对皮层元的更新
    def update(self):
        # print("皮层进行反馈...")
        for i in range(10):
            neure = self.palliumNeures[i]
            #让每个皮层元进行反馈更新
            neure.update()