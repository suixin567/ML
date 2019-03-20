import random
import g
from core.feedback import Feedback


#皮层元
class PalliumNeure:
    def __init__(self,id):
        self.id = id
        self.activate = False
        #print("皮层元",id)


    def receive(self,feature):
        self.activate =True

        #先获取自己已经有的特征，有的话就别重复的添加了
        # myFeatureList = g.r.lrange('palliumneure'+str(self.id), 0, g.r.llen('palliumneure'+str(self.id)))
        # for f in myFeatureList:
        #     if f == feature:#此特征已经存在
        #         #先获取这个特征的intensity
        #         intensity = g.r.get("palliumneure" + str(self.id) + "_" + feature)
        #         newIntensity = int(intensity)+1  # 获取唯一索引号 int类型
        #         g.r.set("palliumneure" + str(self.id) + "_" + feature,newIntensity)
        #         print("我是皮层元",self.id,"收到熟悉的特征：",feature,"最新强度值",newIntensity)
        #         return

        print("我是皮层元", self.id, "收到最新的特征：", feature)
        g.r.rpush('palliumneure' + str(self.id), feature)

        # 先获取这个特征的intensity
        newIntensity = 0
        intensity = g.r.get("palliumneure" + str(self.id) + "_" + feature)
        if intensity == None:
            newIntensity = 1
        else:
            newIntensity = int(intensity) + 1  # 获取唯一索引号 int类型
        g.r.set("palliumneure" + str(self.id) + "_" + feature, newIntensity)


    #判断对某个特征的熟悉程度
    def familiar(self,feature): #feature的样子： 13_vertical_
        # print("特征的样子",feature)
        #元查看自己的记忆。具体格式为： neure78_13_vertical
        result = g.r.get("palliumneure"+str(self.id)+"_"+feature)
        if result == None:
            return -1
        else:
            return int(result)



class Pallium:
    def __init__(self):
        print("皮层初始化...")

        self.palliumNeures=[]
        self.features = []  # 当前帧皮层收到的特征列表

        self.action=['left','right','forward']

        for i in range(10):
                palliumNeure = PalliumNeure(i)
                self.palliumNeures.append(palliumNeure)
        #初始化反馈区
        self.feedback = Feedback()


    def receive(self,feature):
        print("皮层收到一个特征...",feature)
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
                print("我是激活的",i.id)
                if i.id<3:
                    leftScore = leftScore+1
                elif i.id>6:
                    rightScore =rightScore+1
                else:
                    forwardScore = forwardScore+1
        #得出结论
        if leftScore>rightScore and leftScore>forwardScore:
            self.feedback.send("action:left!")
            return
        if rightScore > leftScore and rightScore > forwardScore:
            self.feedback.send("action:right!")
            return
        if forwardScore > leftScore and forwardScore > rightScore:
            self.feedback.send("action:forward!")
            return
        print("没有明确动作，那么就做一个随机动作吧")
        self.feedback.send("action:forward!")


    #收到环境的反馈
    def env_feedback(self,feedback):
        print("收到环境的反馈")
        if feedback==False:
            print("收到一个不好的反馈，接下来对自身做出调整！")



   #单个元的传递规则 根据特征List向下传递一层
    def  transmitMethod(self,featureList):
        print("准备分配给皮层元")
        for f in featureList:
            #向下传递（对每一个特征都要找到最应该传递的目标元）
            familiar_neure =None#最想传给的元
            familiar_max = -1#记录哪个元最熟悉这个特征
            #遍历下一排元
            for j in range(10):
                # print(self.neures[i][j].id)
                familiar_intensity = self.palliumNeures[j].familiar(f)#获得熟悉程度
                if familiar_intensity > familiar_max:
                    familiar_max = familiar_intensity
                    familiar_neure = self.palliumNeures[j]
            if familiar_max ==-1:
                #print("没有熟悉的元")
                self.palliumNeures[random.randint(0, 9)].receive(f)
            else:
                #print("找到了最熟悉的元")
                familiar_neure.receive(f)