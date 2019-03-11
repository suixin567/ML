
from neure import Neure

class Brain:
    def __init__(self):
        index =-1
        neures=[]

        for i in range(10):
            for j in range(10):
                index= index+1
                neu = Neure(index)
                print(index)
                neures.append(neu)
        for j in neures:
            print(j.id)

b = Brain()