from random import randint
from  scipy.constants import *

import math


class Ognisko:

    def __init__(self,name, index,gainValue):
        self.name = "Ognisko%i"%name
        self.index = index     # numer porzadkowy
        self.pixelsList = []
        self.averagedIntensity = 0.0       # srednia intensywnosc
        self.sumIntensity = 0            # calka po intensywnosci
        self.volume = 0                  # objetosc um^3
        self.numberOfPixels = 0
        self.gainValue = gainValue
        self.concentration = 0.0
        self.moleculeNumber = 0.0

    def addPixel(self,pixel):
        self.pixelsList.append(pixel)

    def mainCalculation(self):
        list = self.pixelsList
        sumIntensity2 = reduce(lambda x,y:x+y,list)
        self.sumIntensity = sumIntensity2
        self.numberOfPixels = len(list)
        self.averagedIntensity = float(self.sumIntensity)/float(self.numberOfPixels)

    def calculateVolume(self):
        xPixelSize = 0.06 #um
        zPixelSize = 0.13 # um
        voxelVolume = math.pow(xPixelSize,2)*zPixelSize
        self.volume = voxelVolume*self.numberOfPixels #um^3

    def calculateNumberOfMolecule(self):
        masa1MolaeGFP = 32700 #[g] # masaeGFP = 32,7kDA
        a = self.concentration*self.volume*math.pow(10,-15) #liczba gramow w objetosci focus
        liczbaMoliwOgnisku = a/masa1MolaeGFP
        liczbaMolekul = N_A*liczbaMoliwOgnisku
        self.moleculeNumber = liczbaMolekul
if __name__ == '__main__':
    ognisko1 = Ognisko(1)
    i = 0
    while i<30:
        ognisko1.addPixel(randint(0,255))
        i=i+1
    ognisko1.mainCalculation()
    print ognisko1.averagedIntensity,ognisko1.sumIntensity,ognisko1.volume,ognisko1.numberOfPixels
