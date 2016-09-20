#!/usr/bin/env python
import os
import sys
system=sys.platform[0]
path=os.getcwd()
var = raw_input("jesli chcesz wykonac program dla jednego pliku podaj jego nazwe\n")

if system == "w" or system == "W":
   os.chdir("C:\\Python27\\OBJETOSCI")
   com = "..\\python .\\frendli.py "+path+" "+var
   print com
else:

   dom=os.path.expanduser("~")
   os.chdir(dom+os.sep+'OBJETOSCI')
   com = "python frendli.py "+path+" "+var
   print path

os.system(com)
print ""
raw_input("zakonczono wszystkie obliczenia")

