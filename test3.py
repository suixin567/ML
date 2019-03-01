# -*- coding: UTF-8 -*-
import numpy as np
# import tool
#
#
# a = np.zeros((4,5))
# b = np.zeros((4,5))
# c = np.array([[10,10,10,10,0,0,0,0],[10,10,10,10,0,0,0,0],[10,10,10,10,0,0,0,0],[10,10,10,10,0,0,0,0],[10,10,10,10,0,0,0,0],[10,10,10,10,0,0,0,0]])
# #c = np.array([[3,0,1,2,7,4],[1,5,8,9,3,1],[2,7,2,5,1,3],[0,1,3,1,7,8],[4,2,1,6,2,8],[2,4,5,2,3,9]])
# d = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
# print(c.shape);
# print(d.shape);
#
# end_2=tool.conv_same(c,d)
# print(end_2)

# import os
# import glob
#
# def parseFile(path):
#     for _, dirs, _ in os.walk(path):
#         if (len(dirs)>0):
#             print('物体列表', dirs)  #子目录
#             for dir in dirs:
#                 files = os.listdir(os.path.join(path, dir))
#                 files.sort(key=lambda x: int(x[:-4]))
#                 print(files);
#
#
#
#
# train_path='training_data'
# parseFile(train_path);


# input2 = tf.constant([[
#     [
#         [1],[2],[ 3]
#     ],
#   [[4],
#    [5],
#    [6 ]],
#   [[ 7],
#    [8],
#    [9]]]],dtype=tf.float32)
# filter2 = tf.constant([[[[1]],
#   [[2]]],
#  [[[ 3]],
#   [[4]]]],dtype=tf.float32)

# - * - coding: utf - 8 -*-
# import tensorflow as tf
# import os
# import numpy as np
# import cv2
#
# images = []  # 图像集合
# image = cv2.imread(os.path.join('10.jpg'))
# image = cv2.resize(image, (500,300 ), 0, 0, cv2.INTER_LINEAR)
# image = image.astype(np.float32)
# images.append(image)
# images = np.array(images)

# shape=[1,600,1000,3]#filter尺寸 、通道数
# batch = np.zeros(shape,dtype=np.float32)
# batch[0]=image
# print(batch)
#input=tf.Variable(images);





# shape=[3, 3,3 ,1]#filter尺寸 、通道数、过滤器个数
# filter =tf.Variable(tf.truncated_normal(shape, stddev=0.05))#截断式分布

# filter = tf.constant(
# [[[[1,0,-1],
# [1,0,-1],
# [1,0,-1]],
# [[1,0,-1],
# [1,0,-1],
# [1,0,-1]],
# [[1,0,-1],
# [1,0,-1],
# [1,0,-1]]]]
# ,dtype=tf.float32)
#
# filter1 = tf.constant(
# [
#         [
#                 [
#                         [-1],
#                         [-1],
#                         [-1]
#                 ],
#                 [
#                         [0],
#                         [0],
#                         [0]
#                 ],
#             [
#                 [1],
#                 [1],
#                 [1]
#             ]
#         ],
#         [
#                 [
#                         [-1],
#                         [-1],
#                         [-1]
#                 ],
#                 [
#                         [0],
#                         [0],
#                         [0]
#                 ],
#             [
#                 [1],
#                 [1],
#                 [1]
#             ]
#         ],
#         [
#                 [
#                         [-1],
#                         [-1],
#                         [-1]
#                 ],
#                 [
#                         [0],
#                         [0],
#                         [0]
#                 ],
#             [
#                 [1],
#                 [1],
#                 [1]
#             ]
#         ]
# ]

# ,dtype=tf.float32)
# print("你好呢",filter1.shape);
# test =np.array( [[[[1],[1],[1]],
#   [[0],[0],[0]],
#   [[-1],[-1],[-1]]],
# [[[1],[1],[1]],
#  [[0],[0],[0]],
#   [[-1],[-1],[-1]]],
# [[[1],[1],[1]],
#   [[0],[0],[0]],
#   [[-1],[-1],[-1]]]])
#
# cv2.imshow('22', test)
# cv2.moveWindow("22", 0, 0)
# cv2.waitKey(0)

#竖向检测器
# filter2 = tf.constant(
# [
#         [
#                 [
#                         [1],
#                         [0],
#                         [-1]
#                 ],
#                 [
#                         [1],
#                         [0],
#                         [-1]
#                 ],
#             [
#                 [1],
#                 [0],
#                 [-1]
#             ]
#         ],
#         [
#                 [
#                         [1],
#                         [0],
#                         [-1]
#                 ],
#                 [
#                         [1],
#                         [0],
#                         [-1]
#                 ],
#             [
#                 [1],
#                 [0],
#                 [-1]
#             ]
#         ],
#         [
#                 [
#                         [1],
#                         [0],
#                         [-1]
#                 ],
#                 [
#                         [1],
#                         [0],
#                         [-1]
#                 ],
#             [
#                 [1],
#                 [0],
#                 [-1]
#             ]
#         ]
# ]
# ,dtype=tf.float32)




# shap=(3,3,3,1)
# gg = np.zeros(shap,dtype=np.float32)
# print("应该有的样子",gg);
#
# op = tf.nn.conv2d(input, filter2, strides=[1, 1, 1, 1], padding='SAME')
# init = tf.global_variables_initializer()
# with tf.Session() as sess:
#     sess.run(init)
#
#
#
#     result = sess.run(op)
#     print("结果的形状",result.shape)# 1,600,1000,3
#     res2 = result[0].astype(np.uint8)
#     res2 = np.clip(res2, 0, 255)
#     print("第一张图的形状", res2.shape)
#     print("第一张图的形状", res2)
#
#     cv2.imshow('activate', res2)
#     cv2.moveWindow("activate", 0, 0)
#     cv2.waitKey(0)
#

import numpy as np
# import cv2
# from matplotlib import pyplot as plt
#
# img = cv2.imread('11.jpg',0)
#
# # Initiate FAST object with default values
# fast = cv2.FastFeatureDetector()
#
# # find and draw the keypoints
# kp = fast.detect(img,None)
# img2 = cv2.drawKeypoints(img, kp, color=(255,0,0))
#
# # Print all default params
# # print "Threshold: ", fast.getInt('threshold')
# # print "nonmaxSuppression: ", fast.getBool('nonmaxSuppression')
# # print "neighborhood: ", fast.getInt('type')
# # print "Total Keypoints with nonmaxSuppression: ", len(kp)
#
# cv2.imwrite('fast_true.png',img2)
#
# # Disable nonmaxSuppression
# fast.setBool('nonmaxSuppression',0)
# kp = fast.detect(img,None)
#
# # print "Total Keypoints without nonmaxSuppression: ", len(kp)
#
# img3 = cv2.drawKeypoints(img, kp, color=(255,0,0))
#
# cv2.imwrite('fast_false.png',img3)
kernelH = np.array([[1,2,3],[0,0,0],[-1,-1,-1]])

kernelH = np.where(kernelH > 2, kernelH, 0)
print(kernelH)