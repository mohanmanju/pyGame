from dna import Dna

class rocket:


    def __init__(self):
        self.dna = Dna()
        self.acc = [0,0]
        self.pos = [0,0]
        self.vel = [0,0]

        self.timer = 20
        pass

    def applyforce(self,acc):
        self.acc = [x+y for x,y in zip(self.acc,acc)]

    def update(self,i):
        self.applyforce(self.dna[i])

        self.vel = [x+y for x,y in zip(self.vel,self.acc)]
        self.pos = [x+y for x,y in zip(self.pos,self.vel)]

    pass
