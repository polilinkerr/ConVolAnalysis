import math
from numpy import roots


class Model:

    def __init__(self, gain, a, b, c, d):
        self.gain = gain
        self.A = a
        self.B = b
        self.C = c
        self.D = d

    def calIntFromCon(self, x):
        # Liczy Intensywnosc Fluorescencji ze stezenia
         y = float((self.A - self.D)/(1+math.pow((x/self.C), self.B))+self.D)
         return y

    def calConFromInt(self,y):
        concentration = y
        # liczy stezenie ze sredniej intensywnosci
        c = ((self.A-y)/(y-self.D))
        d = 1/self.B
        z = self.B
        tabela = [self.A,self.B,self.C,self.D]
        b= math.pow(c,d)
        x = float(self.C*math.pow(((self.A-y)/(y-self.D)),1/self.B))
        return x



if __name__ == '__main__':
  Model1 = Model(500, 2.0, 13.0, 14.0, 150.0)
  print Model1.D
  con1 = 9
  int = Model1.calIntFromCon(con1)
  con2 = Model1.calConFromInt(int)
  print "Con1 ", con1,"/n","Int1 ", int,"/n","con2 ",con2


