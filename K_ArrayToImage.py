import os
from random import randint
import PIL.Image
import numpy as np


class K_ArrayToImage:
    def __init__(self, dobre):
        # plik = open(dobre,'r')
        # arrayy = plik.readlines()
        self.matrix = dobre

    def export(self, matrix):
        # espoeryje surowa macierz z dobre
        n = 0

        for i in matrix:
            nazwa = "%.2f_MyNewImage.tif" % n
            i = np.array(i)
            image = PIL.Image.fromarray(i, mode="RGB")
            image.save(os.path.join(os.path.join(os.getcwd(), "Images"), nazwa))
            n = n + 1

    def saveArrayAsImage(self, array):
        n = 0
        for i in array:
            y_width = len(i)
            x_width = len(i[0])
            flatten_i = [item for sublist in i for item in sublist]
            nazwa = "%.2f_MyNewImage.tif" % n
            image = PIL.Image.new("RGB", (x_width, y_width))
            image.putdata(flatten_i)
            image.save(os.path.join(os.path.join(os.getcwd(), "Images"), nazwa))
            n = n + 1

    def makeFantom(self):

        myNEWarray = np.asarray(self.matrix)
        print "CCCC", myNEWarray.shape
        self.fantom = np.zeros(myNEWarray.shape).tolist()

    def createRGBimageFromDobreMatrix(self):
        self.makeFantom()
        dobre = self.matrix
        fantom = self.fantom
        dict_Foci = dict()
        wymiary = np.asarray(self.matrix).shape
        for z in range(wymiary[0]):
            for y in range(wymiary[1]):
                for x in range(wymiary[2]):
                    if dobre[z][y][x] < 0:
                        cell = dobre[z][y][x]
                        if cell in dict_Foci:
                            color = dict_Foci.get(cell, (0, 0, 0))
                            fantom[z][y][x] = color
                        else:
                            dict_Foci[cell] = self.randomColor()  # dopisuje element do slownika jako klucz, a wartosc to randomy kolor
                            fantom[z][y][x] = dict_Foci.get(cell, (255, 255, 255))

                    elif dobre[z][y][x] == 0:
                        fantom[z][y][x] = (0, 0, 0)
                    else:
                        fantom[z][y][x] = (0, 0, 0)

        self.saveArrayAsImage(fantom)

    def randomColor(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

    def export2(self):
        print self.matrix[1]
        pass


if __name__ == '__main__':
    zapis = K_ArrayToImage(os.path.join(os.getcwd(), "zapisaneDobre"))
    zapis.export()
