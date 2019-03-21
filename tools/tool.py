# -*- coding: UTF-8 -*-
import numpy as np
from numba import jit


#same卷积
@jit
def conv_same(image, kernel):
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    #print("准备卷积",image.shape,kernel.shape);

    temp_paddinged = np.zeros((Hi + 2, Wi +2))  # 所得为 full 矩阵
    Hp, Wp = temp_paddinged.shape
    #print("padding尺寸",temp_paddinged.shape);
    temp_m = np.zeros((Hi, Wi))
    #进行padding
    for i in range(Hp):
        for j in range(Wp):
            if (i==0 or i==Hp-1 or j==0 or j==Wp-1):
                temp_paddinged[i][j]=0
                #print("为零",i, j);
            else:
                #print("不为零",i,j);
                temp_paddinged[i][j] = image[i-1][j-1]
    #print("padding完成:\n")
    #print( temp_paddinged)


    for k in range(Hp):
        for l in range(Wp):
            if (k <= Hp - Hk and l <= Wp - Wk):
                temp = 0
                # 通常来说，卷积核的尺寸远小于图片尺寸，同时卷积满足交换律，为了加快运算，可用h*f 代替 f*h 进行计算

                for m in range(Hk):
                    for n in range(Wk):
                            temp += temp_paddinged[k+m][l+n] * kernel[m][n]
                            #print("位置",k,l,m,n,"相乘的数是：",temp_paddinged[k+m][l+n] , kernel[m][n],"结果:" ,temp_paddinged[k+m][l+n] * kernel[m][n]);
                if image[k,l] >0:#这里会有问题，让浅的关键点一律消失了。todo
                    temp_m[k][l] = temp
                #print("得到一个值",temp);
    return temp_m
    # # 截取出 same 矩阵 （输出尺寸同输入）
    # for i in range(Hi):
    #     for j in range(Wi):
    #         out[i][j] = temp_m[int(i+(Hk-1)/2)][int(j+(Wk-1)/2)]
    # return out


@jit
def pool(image):
    kernel = np.array([[1, 1], [1, 1]])
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    pooled = np.zeros((int(Hi / 2),int(Wi / 2)))

    Hp,Wp = pooled.shape
    for i in range(Hp):
        for j in range(Wp):
            max = 0
            for m in range(Hk):
                for n in range(Wk):
                    if i*2 + m >= 0 and i*2 + m < Hi and j*2 + n >= 0 and j*2 + n < Wi:
                        if  image[i*2 + m, j*2 + n]>max:
                            max =  image[i*2 + m, j*2 + n]
                        pooled[i,j] = max
    return pooled




#突出反差点，利用3x3矩阵。
@jit
def conv_corner(image):

    Hi, Wi = image.shape
    corner = np.zeros((Hi, Wi))
    for i in range(Hi):
        for j in range(Wi):
            hTuples=(-1,0,1)
            vTuples = (-1, 0, 1)
            self=image[i,j];
            total =0
            for m in hTuples:
                for n in vTuples:
                    if i+m >=0 and i+m<Hi and j+n>=0 and j+n<Wi:
                        offset = abs(self - image[i+m,j+n])
                        total+= offset
            corner[i, j]=total
    return corner




# #去除相同区域，只留下有差异的区域。
# @jit
# def remove_same(image):
#     Hi, Wi = image.shape
#     for i in range(Hi):
#         for j in range(Wi):
#             hTuples=(-1,0,1)
#             vTuples = (-1, 0, 1)
#             isSame=False;
#             self = image[i,j]
#             for m in hTuples:
#                 for n in vTuples:
#                     if i+m >=0 and i+m<Hi and j+n>=0 and j+n<Wi:
#                         if image[i+m, j+n] == self:
#                             isSame =True;
#                         else:
#                             isSame= False
#
#
#             if isSame ==True:
#                 image[i, j] = 0
#     return image

#降低分辨率，池化(平均池化)
# @jit
# def pool_avarge(image):
#     kernel = np.array([[1, 1], [1, 1]])
#     Hi, Wi = image.shape
#     Hk, Wk = kernel.shape
#     pooled = np.zeros((int(Hi / 2),int(Wi / 2)))
#
#     Hp,Wp = pooled.shape
#     for i in range(Hp):
#         for j in range(Wp):
#             count = 0
#             for m in range(Hk):
#                 for n in range(Wk):
#                     if i*2 + m >= 0 and i*2 + m < Hi and j*2 + n >= 0 and j*2 + n < Wi:
#                         count += image[i*2 + m, j*2 + n]
#                         pooled[i,j] = count
#     return pooled


#二值化。
# @jit
# def conv_corner(image, kernel):
#     Hi, Wi = image.shape
#     Hk, Wk = kernel.shape
#     print("准备卷积",image.shape,kernel.shape);
#
#     temp_paddinged = np.zeros((Hi + 2, Wi +2))  # 所得为 full 矩阵
#     Hp, Wp = temp_paddinged.shape
#     print("padding尺寸",temp_paddinged.shape);
#     temp_m = np.zeros((Hi, Wi))
#     #进行padding
#     for i in range(Hp):
#         for j in range(Wp):
#             if (i==0 or i==Hp-1 or j==0 or j==Wp-1):
#                 temp_paddinged[i][j]=0
#                 #print("为零",i, j);
#             else:
#                 #print("不为零",i,j);
#                 temp_paddinged[i][j] = image[i-1][j-1]
#     print("padding完成:\n")
#     #print( temp_paddinged)
#
#
#     for k in range(Hp):
#         for l in range(Wp):
#             if (k <= Hp - Hk and l <= Wp - Wk):
#                 temp = 0
#                 # 通常来说，卷积核的尺寸远小于图片尺寸，同时卷积满足交换律，为了加快运算，可用h*f 代替 f*h 进行计算
#                 for m in range(Hk):
#                     for n in range(Wk):
#                             temp += temp_paddinged[k+m][l+n] * kernel[m][n]
#                             #print("位置",k,l,m,n,"相乘的数是：",temp_paddinged[k+m][l+n] , kernel[m][n],"结果:" ,temp_paddinged[k+m][l+n] * kernel[m][n]);
#                 if temp > 255*4:
#                     temp_m[k][l] = temp
#                     #print("得到一个值",temp);
#     return temp_m
