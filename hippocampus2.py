# -*- coding: UTF-8 -*-
import sqlite3
import redis
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

    def __init__(self):
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0,decode_responses=True)# 解决获取的值类型是bytes字节问题
        self.r = redis.Redis(connection_pool=pool)

        temp = self.r.get("frame")
        if temp == None:
            self.frame =0
        else:
            self.frame = int(self.r.get("frame"))#获取唯一索引号 int类型
        print("海马初始化完成...历史帧：",self.frame)



    def collect_corner(self, image):
        Hi, Wi = image.shape
        interval = image.max() / 10  # 能量分为10个档次
        # print("interval" ,interval)
        engryArr = np.zeros(10)
        for i in range(Hi):
            for j in range(Wi):
                if image[i, j] > 0:  # 只统计有值的地方
                    angleIndex = int(image[i, j] // interval) - 1  # 判断此能量属于哪个档次。
                    if angleIndex < 0:  # 索引不可以为负数
                        angleIndex = 0
                    temp = engryArr[angleIndex]
                    temp = temp + 1
                    engryArr[angleIndex] = temp
        print("角点能量分布", engryArr);
        #存储数据 （示例：88_corner7 = 2）
        for k in  range(len(engryArr)) :
            self.r.set(str(self.frame) +"_corner_" + str(k), engryArr[k])


    def collect_vertical(self, image):
        Hi, Wi = image.shape
        interval = image.max() / 10  # 能量分为10个档次
        # print("interval" ,interval)
        engryArr = np.zeros(10)
        for i in range(Hi):
            for j in range(Wi):
                if image[i, j] > 0:  # 只统计有值的地方
                    angleIndex = int(image[i, j] // interval) - 1  # 判断此能量属于哪个档次。
                    if angleIndex < 0:  # 索引不可以为负数
                        angleIndex = 0
                    temp = engryArr[angleIndex]
                    temp = temp + 1
                    engryArr[angleIndex] = temp
        print("垂直能量分布", engryArr);

        old = int(self.frame) - 10000  # 检索之前的10000条数据
        if old < 0:
            old = 0

        # 进行辨别 (当前帧和之前的所有帧进行对比)
        for m in range(int(self.frame) - 1, old, -1):  # 遍历历史记忆(不包含此次记忆，所以-1)
            score = 0
            for n in range(10):
                print("比较的是：",str(m) + "_vertical_" + str(n))
                print("比较结果是：",self.r.get(str(m) + "_vertical_" + str(n)),"    ",engryArr[n])
                if self.r.get(str(m) + "_vertical_" + str(n)) == str(engryArr[n]):
                    score = score + 10  # 增加10分
            if score==100:
                print("历史激活器被激活，历史序号", m, "vertical", "得分", score);
                #上报此过滤器。
                self.collect_features(engryArr)
                return#如果找到历史中此过滤器的雷同值，则停止继续查找。


        # 存储数据 （示例：88_vertical7 = 2）
        for k in range(len(engryArr)):
            self.r.set(str(self.frame) + "_vertical_" + str(k), engryArr[k])
            print(str(self.frame),"帧时 key是",str(self.frame) + "_vertical_" + str(k),"数据是",engryArr[k],)





    #收集激活的过滤器
    def collect_features(self,feature):
        print("收到一个激活器",feature)
        features = []
        features.append(feature)




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


    def collect_ok(self, objName):
        # 记录当前帧物品
        self.r.set(str(self.frame) + "_obj", objName)
        # 帧数+1
        self.r.set("frame", self.frame + 1)


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
