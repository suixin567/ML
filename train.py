import cv2
import numpy as np
import glob
import os
import time
train_path='training_data'
imgWidth=1000
imgHeight=600

def foo():
    path = os.path.join(train_path, '*g')  # 找到图片路径
    print("路径",path)
    files = glob.glob(path)  # 得到文件
    print("文件", files)
    lastimg = np.zeros((imgHeight,imgWidth ,3))
    activateimg = np.zeros((imgHeight, imgWidth,3))
    for fl in files:
        image = cv2.imread(fl)
        print(image.shape);
        image = cv2.resize(image, (imgWidth, imgHeight), 0, 0, cv2.INTER_LINEAR)
        image = image.astype(np.float32)
        activateimg = image - lastimg
        lastimg = image
        activateimg = activateimg.astype(np.uint8)
        cv2.imshow('int', activateimg)
        cv2.waitKey(100)




if __name__=="__main__":
    foo();

# cv2.imwrite("./" +train_path+"/a.jpg",image)