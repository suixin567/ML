# -*- coding: UTF-8 -*-
import sqlite3

class ShallowMemory:
    f1 = 0;
    intensity = 0;

    # 创建一条新的浅记忆
    def __init__(self, f1):
        self.f1 = f1;


    def __init__(self, value):
        self.f1 = value;


class Hippocampus:

    toDeep = 5#转为深记忆阈值
    shallowMemorys = []

    def __init__(self):
        self.conn = sqlite3.connect("memory.db")
        self.cursor = self.conn.cursor()
        sql = "select * from shallow"

        # shallows = self.cursor.fetchall()
        for row in self.cursor.execute(sql):
            print(row)
            shallow = ShallowMemory(row[0]);
            shallow.intensity = row[2]
            self.shallowMemorys.append(shallow);
        print("读取浅记忆完成...", len(self.shallowMemorys))

    def collect(self,feature):
        Hf, Wf = feature.shape
        count=0;
        for i in range(Hf):
            for j in range(Wf):
                count += feature[i][j];
        #分档
        if(count<50):
            self.check(0);
            return;
        if ( 50<=count and count <100):
            self.check(50);
            return;
        if (100 <= count and count < 150):
            self.check(100);
            return;
        if (150 <= count and count < 200):
            self.check(150);
            return;
        if (200 <= count and count < 250):
            self.check(200);
            return;
        if (250 <= count and count < 300):
            self.check(250);
            return;
        if (300 <= count):
            self.check(300);
            return;

    def check(self,newValue):
        # 判断是否已经存在此记忆
        isExist = False;
        for i in range(len(self.shallowMemorys)):
            if newValue == self.shallowMemorys[i].f1:
                self.shallowMemorys[i].intensity+=1;
                print("+++++++++++++++++++++++++++++++>>>", newValue);
                if(self.shallowMemorys[i].intensity>=self.toDeep):
                    print("这个记忆转为深记忆",self.shallowMemorys[i].f1)
                isExist = True;
        if(isExist == False):
            print("----------------------------->>>", newValue);
            newMemery = ShallowMemory(newValue);
            self.shallowMemorys.append(newMemery);


    def save(self):
        print("保存海马体...");
        self.cursor.execute('delete from shallow')#清空
        for i in range(len(self.shallowMemorys)):
            vertical = self.shallowMemorys[i].f1
            intensity = self.shallowMemorys[i].intensity
            self.cursor.execute("insert into shallow values(?,?,?)", (vertical, 'suixin', intensity))
            self.conn.commit()
            self.conn.close()