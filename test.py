# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import os
import tools.tool

train_path='training_data'
imgWidth=1000
imgHeight=600



#一个物体一个物体的训练
def train():
        image = cv2.imread("123.jpg")
        rimg = cv2.split(image)[0]
        rimg = cv2.resize(rimg, (imgWidth,imgHeight ), 0, 0, cv2.INTER_LINEAR)
        rimg = rimg.astype(np.uint8)#此句不可以省略。

        cv2.imshow('activate', rimg)
        cv2.moveWindow("activate", 0, 0)
        cv2.waitKey(100)
        #对激活区域做去同，留下凹凸轮廓。
        remove_same = tools.tool.remove_same(rimg)
        cv2.imshow('remove_same', remove_same)
        cv2.moveWindow("remove_same", 0, 300)
        cv2.waitKey(100)
        # #角点检测
        # corner_a = tools.tool.conv_corner(remove_same)
        # cv2.imshow('corner_a', corner_a)
        # cv2.moveWindow("corner_a", 0, 650)
        # cv2.waitKey(200)
        #
        # pool_a = tools.tool.pool(corner_a)
        # remove_same_b = tools.tool.remove_same(pool_a)
        # corner_b = tools.tool.conv_corner(remove_same_b)
        #
        # cv2.imshow('corner_b', corner_b)
        # cv2.moveWindow("corner_b", 0, 950)
        # cv2.waitKey(200)
        a=tools.tool.conv_corner(remove_same)
        b= tools.tool.pool(a)
        c = tools.tool.conv_corner(b)
        d = tools.tool.pool(c)
        e = tools.tool.conv_corner(d)
        f = tools.tool.pool(e)
        g = tools.tool.conv_corner(f)
        cv2.imshow('e', g)
        cv2.moveWindow("e", 0, 650)
        cv2.waitKey(0)


if __name__=="__main__":
    #解析数据文件
    train();

#

#

#
#
# pool_a = tools.tool.pool_a(conv_a)
# cv2.imshow('pool_a', pool_a)
# cv2.moveWindow("pool_a", 600, 850)
# cv2.waitKey(10)
#
#
# conv_b =  tools.tool.conv_a(pool_a)
# pool_b= tools.tool.pool_a(conv_b)
#
# conv_c =  tools.tool.conv_a(pool_b)
# pool_c= tools.tool.pool_a(conv_c)
#
# conv_d =  tools.tool.conv_a(pool_c)
# pool_d= tools.tool.pool_a(conv_d)
#
# cv2.imshow('pool_d', pool_d)
# cv2.moveWindow("pool_d", 1500, 850)
# cv2.waitKey(0)