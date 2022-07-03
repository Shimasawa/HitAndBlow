from random import randrange

class HitAndBlow:
    def __init__(self):
        self.NUM = str(randrange(999))
        self.turn = 1 
        self.hit = self.blow = 0

    def check(self,num :str):
        self.hit = self.blow = 0

        for i,n in zip(list(self.NUM),list(num)):
            if i == n:
                self.hit += 1
            elif n in self.NUM:
                self.blow += 1

        self.turn += 1
