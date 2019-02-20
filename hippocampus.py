# -*- coding: UTF-8 -*-
import sqlite3

class ShallowMemory:
    featureV = 0;
    featureH=0;
    intensity = 0;

    # 创建一条新的浅记忆
    def __init__(self, fv,fh):
        self.featureV = fv;
        self.featureH = fh;



class Hippocampus:
    imgWidth = 500#超参数
    imgHeight = 300#超参数
    toDeep = 5#超参数 转为深记忆阈值
    ladder = 1000;#超参数 能量梯子
    shallowMemorys = []

    def __init__(self):
        self.conn = sqlite3.connect("memory.db")
        self.cursor = self.conn.cursor()
        sql = "select * from shallow"

        # shallows = self.cursor.fetchall()
        for row in self.cursor.execute(sql):
            print(row)
            shallow = ShallowMemory(row[2], row[3])
            shallow.intensity = row[1]
            self.shallowMemorys.append(shallow)
        print("读取浅记忆完成...", len(self.shallowMemorys))

    def collect(self,featureV,featureH):
        Hf, Wf = featureV.shape
        count=0;
        for i in range(Hf):
            for j in range(Wf):
                count += featureV[i][j];
        #分档
        score = self.getLadderScore(count);
        count2 = 0;
        for i in range(Hf):
            for j in range(Wf):
                count2 += featureH[i][j];
        # 分档
        score2 = self.getLadderScore(count2);
        # 判断为旧记忆还是新记忆
        self.check(score,score2);


    # 能量分档
    def getLadderScore(self,value):
        total = self.imgWidth*self.imgHeight*255;
        oneStep = total/self.ladder;
        score = value // oneStep;
        return score;

    #判断为旧记忆还是新记忆
    def check(self,featureV,featureH):
        # 判断是否已经存在此记忆
        isExist = False;
        for i in range(len(self.shallowMemorys)):
            if featureV == self.shallowMemorys[i].featureV and featureH == self.shallowMemorys[i].featureH:
                self.shallowMemorys[i].intensity += 1
                isExist = True;
                print("+++++++++++++++++++++++++++++++>>>", featureV, featureH)
                if(self.shallowMemorys[i].intensity>=self.toDeep):
                    print("这个记忆转为深记忆", self.shallowMemorys[i].featureV, self.shallowMemorys[i].featureH)
        if(isExist == False):
            print("----------------------------->>>", featureV, featureH);
            newMemery = ShallowMemory(featureV,featureH);
            self.shallowMemorys.append(newMemery);


    def save(self):
        print("保存海马体...");
        self.cursor.execute('delete from shallow')#清空
        for i in range(len(self.shallowMemorys)):
            featureV = self.shallowMemorys[i].featureV
            featureH = self.shallowMemorys[i].featureH
            intensity = self.shallowMemorys[i].intensity
            self.cursor.execute("insert into shallow values(?,?,?,?)", ('suixin', intensity, featureV, featureH))
            self.conn.commit()
        self.conn.close()
