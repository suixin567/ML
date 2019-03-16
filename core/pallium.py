#皮层元
class PalliumNeure:
    def __init__(self,id):
        self.id = id
        self.activate = False
        print("皮层元",id)

    def receive(self,_from):
        print("皮层元 接收",_from)
        self.activate =True
        #记录是谁发给自己的
        # g.r.set("neure"+self.id,id)



class Pallium:
    def __init__(self):
        print("皮层初始化...")

        self.palliumNeures=[]

        for i in range(10):
                palliumNeure = PalliumNeure(i)
                self.palliumNeures.append(palliumNeure)

    def receive(self,pointer):
        print("皮层开始运行...")
        self.palliumNeures[2].receive(pointer)



