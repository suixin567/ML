# import g


class Neure:

    def __init__(self,id):
        self.id = id
        self.activate = False

    def receive(self,_from):
        print("接收")
        self.activate =True
        #记录是谁发给自己的
        # g.r.set("neure"+self.id,id)

    def send(self):
        print("发送")
        #记录自己发给谁
        # g.r.set("neure"+self.id,id)
        self.activate = False
