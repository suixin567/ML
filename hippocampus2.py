# -*- coding: UTF-8 -*-
import numpy as np

class ShallowMemory:
    objName=""
    featureV = 0;
    featureH=0;
    intensity = 0;

    # 创建一条新的浅记忆
    def __init__(self,objName, fv,fh):
        self.objName = objName;
        self.featureV = fv;
        self.featureH = fh;



class Hippocampus:
    toDeep = 5#超参数 转为深记忆阈值
    ladder = 1000;#超参数 能量梯子
    shallowMemorys = []

    # def __init__(self):

    features = []#当前帧激活的过滤器
    #收集激活的过滤器
    def collect_features(self,featureName):
        print("收到一个激活过滤器", featureName)
        #保存这个激活的过滤器
        # for i in feature:
        #     self.r.rpush("shallow_" + str(self.frame), i)
        # print("打印浅记忆" , r.lrange('aa', 0, r.llen('aa')));
        #
        #
        # features.append(featureName)




    #判断为旧记忆还是新记忆
    def check(self,objName,featureV,featureH):
        # 判断是否已经存在此记忆
        isExist = False;
        for i in range(len(self.shallowMemorys)):
            if featureV == self.shallowMemorys[i].featureV and featureH == self.shallowMemorys[i].featureH:
                self.shallowMemorys[i].intensity += 1
                isExist = True;
                print("+++++++++++++++++++++++++++++++>>>", objName, featureV, featureH)
                if(self.shallowMemorys[i].intensity>=self.toDeep):
                    print("这个记忆转为深记忆", self.shallowMemorys[i].featureV, self.shallowMemorys[i].featureH)
        if(isExist == False):
            print("----------------------------->>>",objName, featureV, featureH);
            newMemery = ShallowMemory(objName,featureV,featureH);
            self.shallowMemorys.append(newMemery);


    # def collect_ok(self, objName):
    #     # 记录当前帧物品
    #     self.r.set(str(self.frame) + "_obj", objName)



    def save(self):
        print("保存海马...");

        # keys = self.r.keys()
        #
        # print(keys)

        # self.cursor.execute('delete from shallow')#清空
        # for i in range(len(self.shallowMemorys)):
        #     objName = self.shallowMemorys[i].objName
        #     intensity = self.shallowMemorys[i].intensity
        #     featureV = self.shallowMemorys[i].featureV
        #     featureH = self.shallowMemorys[i].featureH
        #
        #     self.cursor.execute("insert into shallow values(?,?,?,?)", (objName, intensity, featureV, featureH))
        #     self.conn.commit()
        # self.conn.close()
