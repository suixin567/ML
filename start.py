# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import os
import guandao

train_path='training_data'
imgWidth=1000
imgHeight=600
# kernelV = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
# kernelH = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
# kernela = np.array([[1, 1, 1], [1, 0, 0], [1, 0, 0]])#左上角的直角检测器。
# kernela = np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]])  # 右上角的直角检测器。

def parseFile():
    for _, dirs, _ in os.walk(train_path):
        if (len(dirs)>0):
            print('总物体列表', dirs)  #子目录
            for dir in dirs:
                files = os.listdir(os.path.join(train_path, dir))
                files.sort(key=lambda x: int(x[:-4]))
                start(dir, files)

#得到光线
def start(objName,files):
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
        # activateimg = activateimg.astype(np.uint8)#此句不可以省略。
        # cv2.imshow('activate', activateimg)
        # cv2.moveWindow("activate", 0, 0)
        # cv2.waitKey(1)

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

        # 送入管道
        guandao.begin(activateimg)

if __name__=="__main__":
    #解析数据文件
    parseFile();