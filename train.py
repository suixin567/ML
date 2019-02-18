# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import glob
import os
import tool


train_path='training_data'
imgWidth=500
imgHeight=300
kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])

def foo():
    path = os.path.join(train_path, '*g')  # 找到图片路径
    files = glob.glob(path)  # 得到文件
    print("文件", files)
    lastimg = np.zeros((imgHeight,imgWidth))
    activateimg = np.zeros((imgHeight,imgWidth))

    for fl in files:
        image = cv2.imread(fl)
        print("原图尺寸",image.shape);
        rimg = cv2.split(image)[0]
        rimg = cv2.resize(rimg, (imgWidth,imgHeight ), 0, 0, cv2.INTER_LINEAR)
        print("resize尺寸", rimg.shape);
        # image = image.astype(np.float32)
        activateimg = rimg - lastimg
        lastimg = rimg
        activateimg = activateimg.astype(np.uint8)#此句不可以省略。
        #print(activateimg);
        cv2.imshow('activate', activateimg)
        cv2.waitKey(1000)
        #print(activateimg);

        # cv2.imshow('单通道图像', b)
        # cv2.waitKey(1000)
        res = tool.conv_same(activateimg,kernel)
        #print("竖向检测完成后",res);

        res = np.clip(res,0,255)
        #res2 = res2.astype(np.uint8)
        #print("截取后", res2)
        cv2.imshow('v-result', res)
        cv2.waitKey(1000)

if __name__=="__main__":
    foo();

# cv2.imwrite("./" +train_path+"/a.jpg",image)