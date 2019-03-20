from core.neure import Neure
import g
import random

class Brain:
    def __init__(self):
        print("脑初始化...")
        index =-1
        self.neures = [[0 for i in range(10)] for j in range(10)]
        for i in range(10):
            for j in range(10):
                index= index+1
                neu = Neure(index,i)
                # print(index)
                self.neures[i][j]=neu
        # print(self.neures)

    def receive(self,features):
        print("脑开始运行...")#此list的具体内容： ['15_corner_', '13_vertical_']

        featureList = g.r.lrange(features, 0,g.r.llen(features))  # 获取记忆的具体内容 ['15_corner_', '13_vertical_']
        #传给第一排元
        self.transmitMethod(featureList,0)

        #让这一排的元向前传递(从第0到第9排)
        for i in range(0,9):
            print("让第",i,"排的元向前传递")
            for j in range(10):
                neure=self.neures[i][j]
                #获取这个元的特征列表（只获取当前帧的最新特征！！！）
                neureFeatureList = g.r.lrange('neure' + str(neure.id), g.r.llen('neure' + str(neure.id)) - neure.newFeatureAmount , g.r.llen('neure' + str(neure.id)))
                #获取一个元的最新特征后，重置最新特征数！
                neure.newFeatureAmount = 0

                if len(neureFeatureList)==0 or neure.activate==False:
                    continue
                self.transmitMethod(neureFeatureList,i+1)
        #通知皮层当前帧的特征全部传完了
        g.pallium.receive_ok()


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
                self.neures[stepIndex][random.randint(0, 9)].receive(f)
            else:
                #print("找到了最熟悉的元")
                familiar_neure.receive(f)
