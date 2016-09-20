import os
import numpy as np
import stak
from K_Model import Model
from Ognisko import Ognisko


def MainCalculation(image, dobre):
    gainValue = int(os.path.basename(image)[-7:-4])

    listoOfFoci = CreateListOfFociObject(image, dobre, gainValue)
    model600 = Model(600, 5.46878, 1.08103, 2.78959, 260.87547)
    model650 = Model(650, 8.51758, 0.92748, 439027.6656, 1.82221E7)
    model700 = Model(700, 13.5435, 1.05686, 1.69071, 463.39034)
    model750 = Model(750, 13.28677, 0.67095, 882633.34392, 2.27924E6)
    model800 = Model(800, 2.72751, 0.52045, 2.10328, 645.46015)
    model850 = Model(850, 0.08335, 0.52578, 0.35122, 465.45001)
    model900 = Model(900, -0.21661, 0.90764, 0.02681, 275.15365)
    model950 = Model(950, 0.52044, 1.04333, 0.0132, 266.9045)
    ListaModeli = [model600, model650, model700, model750, model800, model850, model900, model950]

    for i in listoOfFoci: #wyliczamy stezenie na podstawie sredniej intensywnosci
        for j in ListaModeli:
            if i.gainValue == j.gain:
                try:
                    i.concentration = j.calConFromInt(i.averagedIntensity)
                except ValueError:
                    i.concentration = 1
    for i in listoOfFoci:
        try:
            i.calculateVolume()
            i.calculateNumberOfMolecule()
        except ValueError:
            i.volume = 0.0
            i.moleculeNumber = 0

    OutputFile = open(os.path.join(os.getcwd(), "Results.txt"), 'w')
    OutputFile.write("Gain  Name    index   PixelsNumber    AverageIntensity    SumIntensity    Concentration[mg/ml]    volume[um^3] NumberOfMolecule  \n")
    for i in listoOfFoci:
        OutputFile.write("{}    {}    {}       {}            {:.2f}            {}              {:.4f}        {:.4f}     {:.4f} \n".format(i.gainValue, i.name, i.index, len(i.pixelsList),i.averagedIntensity, i.sumIntensity, i.concentration, i.volume, i.moleculeNumber))

    OutputFile.close()
    return None


def CreateListOfFociObject(image, dobre, gainValue):
    imf = stak.Stack(image)
    obraz = imf.obraz_listy()  # zwraca liste przekrojow
    wymiary = np.asarray(dobre).shape
    dict_Foci = dict()
    n = 0
    for z in range(wymiary[0]):
        for y in range(wymiary[1]):
            for x in range(wymiary[2]):
                if dobre[z][y][x] < 0:
                    cell = dobre[z][y][x]
                    if cell in dict_Foci:
                        dict_Foci.get(cell).addPixel(obraz[z][y][x])

                        # dodaj do listy pikseli danego obiektu
                    else:
                        OgniskoAktualne = Ognisko(cell, n, gainValue)
                        OgniskoAktualne.addPixel(obraz[z][y][x])
                        dict_Foci[cell] = OgniskoAktualne
                        n = n + 1
                        del OgniskoAktualne

    for i in dict_Foci.values():
        i.mainCalculation()

    ListOfFoci = dict_Foci.values()
    return ListOfFoci


if __name__ == '__main__':
    # test1.py executed as script
    # do something
    MainCalculation()
