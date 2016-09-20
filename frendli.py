import os
import sys

class Objetosci:

    def __init__(self, path, plik=''):#(self,output_type, path, plik=''):
        self.path=path
        #self.output_type=output_type
        self.plik=plik
        self.system=sys.platform[0]


    def list_creator(self):
        if self.plik != '':
            self.obrazy=[self.plik]
            if self.system=="w" or self.system=="W":
                 self.xlsy=["Statistics for "+plik.split('.tif')[0]+".xls\"" for plik in self.obrazy]
                 print "Aa",self.xlsy
            else:
                 self.xlsy=["Statistics for "+plik.split('.tif')[0]+".xls\"" for plik in self.obrazy]
            print "A"
        else:
            pliki=os.listdir(self.path)
            self.obrazy=[plik for plik in pliki if plik[-4:]==".tif"]

            if self.system=="w" or self.system=="W":
                 self.xlsy=["Statistics for "+plik.split('.tif')[0]+".xls\"" for plik in self.obrazy]
            else:
                 self.xlsy=["Statistics for "+plik.split('.tif')[0]+".xls\"" for plik in self.obrazy]
            print "B"


    def main_loop(self):
        for i in range(len(self.obrazy)):
            #print " "
            print "[", i+1, "plik na ", len(self.obrazy), "]"
            dopisek=os.path.join(self.path,self.obrazy[i])+' \"'+os.path.join(self.path,self.xlsy[i])+' '+os.path.join(self.path,self.obrazy[i].split('.tif')[0]+"_vol")
            print "Dopisek",dopisek
            comand ="python ./szybcior.py "+dopisek
            if self.system=="w" or self.system=="W":
                os.chdir('C:\\Python27')
                comand ="python .\\OBJETOSCI\\szybcior.py "+dopisek
            os.system(comand)
	print "zakonczono wszystkie obliczenia"


def Krzysiek(name):
        print "jestem w funkcji Krzysiek"
        path="C:\Python27\OBJETOSCI"
        try:
            plik="test_macro_C1.tif"

        except IndexError:
            plik=''

        c=Objetosci(path,plik)
        c.list_creator()
        c.main_loop()
        print ""






if __name__ == '__main__':
    Krzysiek("C:\Python27\OBJETOSCI macro_test.tif")


