import g
import cv2
import os
import guandao
import tools.tool2

train_path='ML_unity/training_data'
imgWidth=1000
imgHeight=600


class Retina:
    def __init__(self):
        print("视网膜初始化...")

    def loadImg(self):
        image = cv2.imread(os.path.join(train_path, "0.jpg"))
        # print("原图尺寸", image.shape);
        rimg = cv2.split(image)[0]
        rimg = cv2.resize(rimg, (imgWidth, imgHeight), 0, 0, cv2.INTER_LINEAR)
        # 送入管道
        guandao.begin(rimg)

if __name__=="__main__":
    #通知unity截图
    g.client.send("camera")
