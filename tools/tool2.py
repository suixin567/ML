import cv2
import numpy as np
import matplotlib.pyplot as plt

posy =0

#显示一张二维矩阵
def show(image,time,name):
    tempImage = image.copy()
    temp = tempImage.max() / 255
    tempImage = tempImage / temp

    global posy
    Hi, Wi = tempImage.shape
    tempImage = tempImage.astype(np.uint8)  # 此句不可以省略。但会导致最大255的截取。
    cv2.imshow(name, tempImage)
    cv2.moveWindow(name, 0, posy)
    cv2.waitKey(time)
    posy += Hi+50
    if name!="":
        cv2.imwrite("./logs/"+name+".jpg", tempImage)

#显示折线图
def show2(arr):
    x1 = range(0, len(arr))
    plt.plot(x1, arr, label='Frist line', linewidth=1, color='r', marker='o', markerfacecolor='blue', markersize=2)
    # plt.plot(x2,y2,label='second line')
    plt.xlabel('角度')
    plt.ylabel('角度数量')
    plt.title('角度分布')
    plt.legend()
    plt.show()



#######方法储备######

#con_3 = np.where(con_3 > 20, con_3, 0)  # 大于20的才可以保留，否则变成0.todo这里有也有问题，会弱化浅的关键点，误伤。

#反向循环列表
# a=[1,2,3,4,5]
# for i in a[::-1]:
#   print(i)