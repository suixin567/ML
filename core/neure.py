from core.pallium import Pallium

class Neure:
    # 初始化皮层
    pallium = Pallium()

    def __init__(self,id,row):
        self.id = id
        self.activate = False
        print("元",id,row)

    def receive(self,_from):
        print("元 接收",_from)
        self.activate =True
        #记录是谁发给自己的
        # g.r.set("neure"+self.id,id)
        #传递到皮层
        self.pallium.receive(_from)

    def send(self):
        print("发送")
        #记录自己发给谁
        # g.r.set("neure"+self.id,id)
        self.activate = False
