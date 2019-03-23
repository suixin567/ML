# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import os
import guandao

train_path='training_data'
imgWidth=1000
imgHeight=600


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

        # 送入管道
        guandao.begin(activateimg)

if __name__=="__main__":
    #解析数据文件
    parseFile();