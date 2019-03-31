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
        self.transmitMethod(featureList,0)#0代表传给第0排

        #让这一排的元向前传递(从第0到第9排)
        for i in range(0,9):
            # print("让第",i,"排的元向前传递")
            for j in range(10):
                neure=self.neures[i][j]
                #获取这个元的特征列表（只获取当前帧的最新特征！！！）
                allFeatureList = g.r.hkeys("neure"+str(neure.id))
                neureFeatureList = allFeatureList[len(allFeatureList)-neure.newFeatureAmount:len(allFeatureList)]
                #获取一个元的最新特征后，重置最新特征数！
                #neure.newFeatureAmount = 0

                if len(neureFeatureList)==0:#如果这个元此次没有接收到特征则跳过。
                    continue
                self.transmitMethod(neureFeatureList,i+1)
        #通知皮层当前帧的特征全部传完了
        g.pallium.receive_ok()


    #单个元的传递规则 根据特征List向下传递一层
    def  transmitMethod(self,featureList,stepIndex):
        for f in featureList:
            #向下传递（对每一个特征都要找到最应该传递的目标元）
            #遍历下一排元
            isAccept = False#此特征是否被接收
            for j in range(10):
                # print(self.neures[i][j].id)
                isAccept = self.neures[stepIndex][j].familiar(f)#判断这个元是否接收此特征
                if isAccept == True:
                    # print("找到了最熟悉的元")
                    self.neures[stepIndex][j].receive(f)
                    break
            if isAccept == False:
                # print("没有熟悉的元")
                self.neures[stepIndex][random.randint(0, 9)].receive(f)



    def update(self):
        # print("脑进行反馈...")
        for i in range(10):
            for j in range(10):
                neure = self.neures[i][j]
                #让每个元进行反馈更新
                neure.update()

    def reset(self):

        for i in range(10):
            for j in range(10):
                neure = self.neures[i][j]
                neure.newFeatureAmount = 0