import numpy as np

#same卷积
def conv_same(image, kernel):
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    print("准备卷积",image.shape,kernel.shape);

    temp_paddinged = np.zeros((Hi + 2, Wi +2))  # 所得为 full 矩阵
    Hp, Wp = temp_paddinged.shape
    print("padding尺寸",temp_paddinged.shape);
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
    print("padding完成:\n")
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

                temp_m[k][l] = temp
                #print("得到一个值",temp);
    return temp_m
    # # 截取出 same 矩阵 （输出尺寸同输入）
    # for i in range(Hi):
    #     for j in range(Wi):
    #         out[i][j] = temp_m[int(i+(Hk-1)/2)][int(j+(Wk-1)/2)]
    # return out