import cv2
import numpy as np
posy =0


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





#######方法储备######

#con_3 = np.where(con_3 > 20, con_3, 0)  # 大于20的才可以保留，否则变成0.todo这里有也有问题，会弱化浅的关键点，误伤。