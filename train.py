# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import os
import tools.tool
import hippocampus

train_path='training_data'
imgWidth=1000
imgHeight=600
kernelV = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
kernelH = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

def parseFile():
    for _, dirs, _ in os.walk(train_path):
        if (len(dirs)>0):
            print('总物体列表', dirs)  #子目录
            for dir in dirs:
                files = os.listdir(os.path.join(train_path, dir))
                files.sort(key=lambda x: int(x[:-4]))
                train(dir, files)



#一个物体一个物体的训练
def train(objName,files):
    print(objName, files)
    lastimg = np.zeros((imgHeight,imgWidth))
    activateimg = np.zeros((imgHeight,imgWidth))
    for fl in files:
        image = cv2.imread(os.path.join(train_path, objName, fl))
        print("原图尺寸",image.shape);
        rimg = cv2.split(image)[0]
        rimg = cv2.resize(rimg, (imgWidth,imgHeight ), 0, 0, cv2.INTER_LINEAR)
        print("resize尺寸", rimg.shape);
        activateimg = rimg - lastimg
        lastimg = rimg
        activateimg = activateimg.astype(np.uint8)#此句不可以省略。

        cv2.imshow('activate', activateimg)
        cv2.moveWindow("activate", 0, 0)
        cv2.waitKey(1)

        # #获取v特征
        # featureV = tools.tool.conv_same(activateimg,kernelV)
        # featureV = np.clip(featureV,0,255)
        # cv2.imshow('featureV', featureV)
        # cv2.moveWindow("featureV", 0, 350)
        # cv2.waitKey(1)
        #
        # #获取h特征
        # featureH = tools.tool.conv_same(activateimg, kernelH)
        # featureH = np.clip(featureH, 0, 255)
        # cv2.imshow('featureH', featureH)
        # cv2.moveWindow("featureH", 0, 750)
        # cv2.waitKey(1)

        #进行第一次卷积
        kernela = np.array([[1, 1, 1], [1, 0, 0], [1, 0, 0]])#右上角的直角检测器。
        con_1 = tools.tool.conv_same(activateimg,kernela);
        print(con_1.max())
        #con_1= con_1/2;
        con_1 = np.where(con_1 > 20, con_1, 0)#大于20的才可以保留，否则变成0.todo这里有也有问题，会弱化浅的关键点，误伤。
        print("第一次卷积去弱后", con_1.max());
        con_1 = con_1.astype(np.uint8)  # 此句不可以省略。
        cv2.imshow('con_1', con_1)
        cv2.moveWindow("con_1", 0, 300)
        cv2.waitKey(1000)
        #第一次池化
        pool_1 =  tools.tool.pool(con_1);
       # pool_1 = pool_1/2;
        print("第一次池化后", pool_1.max());
        #第二次卷积
        con_2 = tools.tool.conv_same(pool_1, kernela);
     #   con_2 = con_2 / 2;
        con_2 = np.where(con_2 > 20, con_2, 0)  # 大于20的才可以保留，否则变成0.todo这里有也有问题，会弱化浅的关键点，误伤。
        print("第二次卷积", con_2.max());
        con_2 = con_2.astype(np.uint8)  # 此句不可以省略。
        cv2.imshow('con_2', con_2)
        cv2.moveWindow("con_2", 0, 600)
        cv2.waitKey(1000)
        #第二次池化
        pool_2 = tools.tool.pool(con_2);
       # pool_2 = pool_2 / 2;
        print("第二次池化", pool_2.max())
        # #第三次卷积
        con_3 = tools.tool.conv_same(pool_2, kernela);
     #   con_3 = con_3 / 2;
        con_3 = np.where(con_3 > 20, con_3, 0)  # 大于20的才可以保留，否则变成0.todo这里有也有问题，会弱化浅的关键点，误伤。
        print("第三次卷积", con_3.max())
        con_3 = con_3.astype(np.uint8)  # 此句不可以省略。
        cv2.imshow('con_3', con_3)
        cv2.moveWindow("con_3", 0, 900)
        cv2.waitKey(1000)
        #第三次池化
        pool_3 = tools.tool.pool(con_3);
      #  pool_3 = pool_3 / 2;
        print("第三次池化", pool_3.max())
        # #第四次卷积
        con_4 = tools.tool.conv_same(pool_3, kernela);
       # con_4 = con_4 / 2;
        con_4 = con_4/3
        con_4 = np.where(con_4 > 20, con_4, 0)  # 大于20的才可以保留，否则变成0.todo这里有也有问题，会弱化浅的关键点，误伤。
        print("第四次卷积", con_4.max())
        con_4 = con_4.astype(np.uint8)  # 此句不可以省略。
        cv2.imshow('con_4', con_4)
        cv2.moveWindow("con_4", 0, 1200)
        cv2.waitKey(2000)



        print(con_4)
        cv2.imwrite("./a.jpg", con_4)
        #进入海马体
        #hipp.collect(objName,featureV,featureH);


if __name__=="__main__":
    #创建海马体
    hipp = hippocampus.Hippocampus();
    #解析数据文件
    parseFile();
    #持久化海马体
    hipp.save();