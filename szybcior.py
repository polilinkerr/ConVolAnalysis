import os

import stak
#import TO
import TO2 as TO
from K_ArrayToImage import K_ArrayToImage
import AnalysisIntensity


def max_positions(xls_file):
    xls = open(xls_file)
    dane = xls.readlines()
    xls.close()
    edge = []
    for i in dane[1:]:
        i = i.replace(",", ".")
        a = i.split()
        edge.append((int(round(float(a[11]))), int(round(float(a[12]))), int(round(float(a[13])))))
    return edge


def pisorz(gotowe, wymiary, out_put, output_type):  # ,t0):
    # fw=open(out_put+"_"+output_type, "w")
    print out_put, "   ", output_type, "    ", r"%s_%s" % (out_put, output_type)
    fw = open(r"%s_%s" % (out_put, output_type), "w")
    fw.write('x  y  z  v\n')
    for l in gotowe:
        linia = str(l[0][0]) + " " + str(l[0][1]) + " " + str(l[0][2]) + " " + str(l[1]) + "\n"
        fw.write(linia)

    # T=time.time()-t0
    # print "czas pracy: ", T
    # czas="czas paracy: "+str(T)+"\n"
    if output_type == "l":
        sajz = str(wymiary[1]) + " " + str(wymiary[0]) + " " + str(len(obraz))
        fw.write("______________\n")
        fw.write(sajz)

    fw.close()


######################################################################################


output_type_l = 'l'
output_type_s = 's'
# image = sys.argv[1]
# xls=sys.argv[2]
# out_put=sys.argv[3]


# image = r"C:\Python27\OBJETOSCI\test_macro_C1.tif"
# xls= r"C:\Python27\OBJETOSCI\Statistics for test_macro_C1.xls"
# out_put= r"C:\Python27\OBJETOSCI\test_macro_C1_vol"
path = os.getcwd()
#image = os.path.join(path, "test_macro_wycinek_C1_800.tif")
#xls = os.path.join(path, "Statistics for test_macro_wycinek_C1_800.xls")
#out_put = os.path.join(path, "test_macro_wycinek_C1_vol_800")
#image = os.path.join(path, "test_800.tif")
#xls = os.path.join(path, "Statistics for test_800.xls")
#out_put = os.path.join(path, "test_vol_800")
#image = os.path.join(path, "Series063_chan00_800.tif")
#xls = os.path.join(path, "Statistics for Series063_chan00_800.xls")
#out_put = os.path.join(path, "Series063_chan00_vol_800")
path = os.path.join(os.getcwd(), "Sources")
image = os.path.join(path,"3_065_C2_800.tif" )
xls = os.path.join(path,"Statistics for 3_065_C2_800.xls" )
out_put = os.path.join(path, "3_065_C2_800_vol")

noise_lev = 50

# t0=time.time()

maksima = max_positions(xls)
print "Maksima", maksima
imf = stak.Stack(image)
obraz = imf.obraz_listy()  # zwraca liste przekrojow
wymiary = imf.im_sz

wymiary_full = wymiary + [len(obraz)]

# print " "
print "analizuje obraz: \n" + image
# print " "
print "\t prosze czekac..."
# print " "

poczatek = TO.inicjator(maksima, obraz, wymiary_full)
# def inicjator(maksima,obraz,wymiary_full):
#   return return (obraz,edge,edge_info)



dobre = TO.rdzen(poczatek[0], poczatek[1], poczatek[2], noise_lev, wymiary_full)
# def rdzen(obraz, edge,edge_info, noise_lev,wymiary_full):
#     return obraz

def zapiszmy_dobre(dobre):
    plik = open(os.path.join(path,"zapisaneDobre"),'w')
    for item in dobre:
        plik.write("%s\n" %item)
    plik.close()
    pass

zapiszmy_dobre(dobre)#
zapis = K_ArrayToImage(dobre)  #ekspoeruje macierz dobre do obrazu RGB
zapis.createRGBimageFromDobreMatrix()  #metoda tej klasy ,ktora to robi

listOfFoci = AnalysisIntensity.MainCalculation(image,dobre) # Generuje plik txt z danymi


# tak ZLY STYL PROGRAMOWANIA jest wynikiem ewolucji wstecznej programu
# (ograniczenie stopni swobody uzyszkodnika dla jego dobra)
if output_type_l == "l":
    gotowe = TO.tlumacz(dobre)
    pisorz(gotowe, wymiary, out_put, output_type_l)
if output_type_s == "s":
    gotowe = TO.tlumacz2(dobre, maksima)
    pisorz(gotowe, wymiary, out_put, output_type_s)

print "zakonczono analize pliku: \n" + image
#
print "wynik zapisano w: \n" + out_put + "_l oraz \n" + out_put + "_s"
print " "
exit()
