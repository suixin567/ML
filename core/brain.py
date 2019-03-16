from core.neure import Neure


class Brain:
    def __init__(self):
        index =-1
        self.neures=[]


        for i in range(10):
            for j in range(10):
                index= index+1
                neu = Neure(index,i)
                # print(index)
                self.neures.append(neu)
        # for j in neures:
            # print(j.id)


    def receive(self,pointer):
        print("脑开始运行...")
        self.neures[11].receive(pointer)


