# -*- coding: UTF-8 -*-
import g

from core.brain import *

class Hippocampus:

    def __init__(self):
        print("海马初始化...")
        self.features = []  # 当前帧激活的过滤器
        self.brain = Brain()

    #收集激活的过滤器
    def collect_features(self,featureName):
        self.features.append(featureName)
        print("收到一个激活过滤器", self.features)

    # 收集激活的过滤器完成，统一处理
    def collect_features_ok(self):
        print("海马开始进行判断...")
        # 判断为旧记忆还是新记忆
        #遍历所有之前的记忆
        for m in range(int(g.frame) - 1, -1, -1):  # 遍历历史记忆(不包含此次记忆，所以-1)
            # print("之前的记忆", str(m) + '_shallow')  #之前的记忆  33_shallow  32_shallow  31_shallow
            featureList = g.r.lrange(str(m) + '_shallow', 0, g.r.llen(str(m) + '_shallow'))#获取记忆的具体内容 ['15_corner_', '13_vertical_']
            #print("记忆具体内容",featureList,"本次海马得到的内容",self.features)
            if featureList == self.features:
                # print(len(self.features),featureList)
                print("发现此历史记忆匹配",str(m) + '_shallow')

                self.brain.receive(str(m) + '_shallow')
                # 对比具体挡位是否一致
                # score = 0
                # for n in range(len(featureList)):#n代表激活器的序号
                #     print("正在对比这个过滤器",featureList[n])
                #     for i in range(10):
                #         print("对比的是",featureList[n]+str(i),"  ",self.features[n]+str(i) )
                #         if g.r.get(featureList[n]+str(i)) == g.r.get(self.features[n]+str(i)):
                #             score = score+10
                # if score ==len(featureList)*100:#达到满分
                #     print("发现一个熟悉的东西！")
                return
        #没有发现熟悉的记忆，存储这些激活的过滤器（示例23_shallow : ['15_corner_','13_vertical_']） 也就是说'15_corner_'与'13_vertical_'可能是一个物体。
        for f in self.features:
            g.r.rpush(str(g.frame)+'_shallow', f)
        #打印这些过滤器的组合
        print("发现一个新东西：", g.r.lrange(str(g.frame)+'_shallow', 0, g.r.llen(str(g.frame)+'_shallow')));

        #重置
        self.features = []
