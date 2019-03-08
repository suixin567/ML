# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import os
import tools.tool
import tools.tool2
# import hippocampus
import hippocampus2

train_path='training_data'
imgWidth=1000
imgHeight=600
kernelV = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
kernelH = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
# kernela = np.array([[1, 1, 1], [1, 0, 0], [1, 0, 0]])#左上角的直角检测器。
kernela = np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]])  # 右上角的直角检测器。
kernelV2 = np.array([[0,1,0],[0,1,0],[0,1,0]])
kernelcorner = np.array([[1,1,1],[1,1,1],[1,1,1]])

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

        # 检测垂直
        verticalResult = conv(activateimg,kernelV2);
        # 检测角点
        cornerResult = conv_corner(activateimg);


        #进入海马体
        #hipp.collect(objName,featureV,featureH);

        hipp2.collect_corner(cornerResult)
        hipp2.collect_vertical(verticalResult)

        #收集完成
        hipp2.collect_ok(objName)


def conv(imgae ,kernel):
    # 第一次卷积
    con_1 = tools.tool.conv_same(imgae, kernel);
    print("第一次卷积后的最大值", con_1.max())
    # 第一次池化
    pool_1 = tools.tool.pool(con_1);
    print("第一次池化后的最大值", pool_1.max());
    # 第二次卷积
    con_2 = tools.tool.conv_same(pool_1, kernel);
    print("第二次卷积后的最大值", con_2.max());
    # 第二次池化
    pool_2 = tools.tool.pool(con_2);
    print("第二次池化后的最大值", pool_2.max())
    # #第三次卷积
    con_3 = tools.tool.conv_same(pool_2, kernel);
    print("第三次卷积后的最大值", con_3.max())
    tools.tool2.show(con_3, 100, "con_3")
    # 第三次池化
    pool_3 = tools.tool.pool(con_3);
    print("第三次池化后的最大值", pool_3.max())
    # #第四次卷积
    con_4 = tools.tool.conv_same(pool_3, kernel);
    print("第四次卷积后的最大值", con_4.max())
    tools.tool2.show(con_4, 100, "con_4")
    # 第四次池化
    pool_4 = tools.tool.pool(con_4);
    print("第四次池化后的最大值", pool_4.max())
    # 第五次卷积
    con_5 = tools.tool.conv_same(pool_4, kernel);
    print("第五次卷积后的最大值", con_5.max())
    tools.tool2.show(con_5, 100, "conv_5")
    return con_5



def conv_corner(imgae):
    # 第一次卷积
    con_1 = tools.tool.conv_corner(imgae);
    print("第一次卷积后的最大值", con_1.max())
    # 第一次池化
    pool_1 = tools.tool.pool(con_1);
    print("第一次池化后的最大值", pool_1.max());
    # 第二次卷积
    con_2 = tools.tool.conv_corner(pool_1);
    print("第二次卷积后的最大值", con_2.max());
    # 第二次池化
    pool_2 = tools.tool.pool(con_2);
    print("第二次池化后的最大值", pool_2.max())
    # #第三次卷积
    con_3 = tools.tool.conv_corner(pool_2);
    print("第三次卷积后的最大值", con_3.max())
    tools.tool2.show(con_3, 100, "con_3")
    # 第三次池化
    pool_3 = tools.tool.pool(con_3);
    print("第三次池化后的最大值", pool_3.max())
    # #第四次卷积
    con_4 = tools.tool.conv_corner(pool_3);
    print("第四次卷积后的最大值", con_4.max())
    tools.tool2.show(con_4, 100, "con_4")
    # 第四次池化
    pool_4 = tools.tool.pool(con_4);
    print("第四次池化后的最大值", pool_4.max())
    # 第五次卷积
    con_5 = tools.tool.conv_corner(pool_4);
    print("第五次卷积后的最大值", con_5.max())
    tools.tool2.show(con_5, 200, "conv_5")
    return con_5


if __name__=="__main__":
    #创建海马体
   # hipp = hippocampus.Hippocampus();
    hipp2 = hippocampus2.Hippocampus();
    #解析数据文件
    parseFile();
    #持久化海马体
   # hipp.save();
    hipp2.save();