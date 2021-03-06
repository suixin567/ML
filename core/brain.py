from core.neure import Neure
import g
import random

from configobj import ConfigObj

# 读取配置文件
config = ConfigObj("conf.ini", encoding='UTF8')
neureRows = int(config['ml']['neureRows'])
neureColumns = int(config['ml']['neureColumns'])


class Brain:
    def __init__(self):
        print("脑初始化...")
        index =-1
        self.neures = [[0 for i in range(neureRows)] for j in range(neureColumns)]
        for i in range(neureRows):
            for j in range(neureColumns):
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
        for i in range(0,neureRows-1):
            # print("让第",i,"排的元向前传递")
            for j in range(neureColumns):
                neure=self.neures[i][j]
                #获取这个元的特征列表（只获取当前帧的最新特征！！！）
                allFeatureList = neure.frameFeatures
                if len(allFeatureList)==0:#如果这个元此次没有接收到特征则跳过。
                    continue
                self.transmitMethod(allFeatureList,i+1)
        #通知皮层当前帧的特征全部传完了
        g.pallium.receive_ok(neureRows,neureColumns)


    #单个元的传递规则 根据特征List向下传递一层
    def  transmitMethod(self,featureList,stepIndex):
        for f in featureList:
            #向下传递（对每一个特征都要找到最应该传递的目标元）
            #遍历下一排元
            isAccept = False#此特征是否被接收
            for j in range(neureColumns):
                # print(self.neures[i][j].id)
                isAccept = self.neures[stepIndex][j].familiar(f)#判断这个元是否接收此特征
                if isAccept == True:
                    # print("找到了最熟悉的元")
                    self.neures[stepIndex][j].receive(f)
                    break
            if isAccept == False:
                # print("没有熟悉的元")
                self.neures[stepIndex][random.randint(0, 9)].receive(f)



    def update(self,isok):
        # print("脑进行反馈...")
        for i in range(neureRows):
            for j in range(neureColumns):
                neure = self.neures[i][j]
                #让每个元进行反馈更新
                neure.update(isok)