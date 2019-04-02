import g
import cv2
import os
import guandao
from configobj import ConfigObj

# 读取配置文件
config = ConfigObj("conf.ini", encoding='UTF8')
imgWidth = int(config['ml']['imgWidth'])
imgHeight = int(config['ml']['imgHeight'])
train_path = config['ml']['train_path']


class Retina:
    def __init__(self):
        print("视网膜初始化...")
        # 通知unity截图
        g.client.send("camera")

        while g.run:
            if g.feedback.state == "cameraok":
                g.feedback.update("default")
                self.loadImg()



    def loadImg(self):
        image = cv2.imread(os.path.join(train_path, "0.jpg"))
        # print("原图尺寸", image.shape);
        rimg = cv2.split(image)[0]
        rimg = cv2.resize(rimg, (imgWidth, imgHeight), 0, 0, cv2.INTER_LINEAR)
        # 送入管道
        guandao.begin(rimg)

if __name__=="__main__":
    ret = Retina()

