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


# 能量分档
def getLadderScore(value):
    print("aaa", value);
    total = 500 * 300 * 255;
    oneStep = total / 100;
    print("bbb", oneStep);
    score = value // oneStep;
    print("ccc", score);


getLadderScore(2000000);