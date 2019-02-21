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




import os
import glob

def parseFile(path):
    for _, dirs, _ in os.walk(path):
        if (len(dirs)>0):
            print('物体列表', dirs)  #子目录
            for dir in dirs:
                files = os.listdir(os.path.join(path, dir))
                files.sort(key=lambda x: int(x[:-4]))
                print(files);




train_path='training_data'
parseFile(train_path);
