#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
from z3 import *

# path = input()
# with open(path, 'r') as f:
#     automaton = json.load(f)

with open("/home/adis/Programming/PIZZO/Zad3/test2.json", 'r') as f:
    dieta = json.load(f)

s = Solver()

zmienne = []
for skladnik in dieta[u"składniki"]:
    zmienne.append([Int(skladnik["nazwa"]+str(i)) for i in range(5)])

zmienne = []
for parametr in dieta["parametry"]:
    zmienne[:] = []
    for skladnik in dieta[u"składniki"]:
        ZS = [Int(skladnik["nazwa"]+str(i)) for i in range(5)]
        for z in ZS:
            s.add(z>=0)
        zmienne.append(skladnik[parametr] * ToReal(Sum(ZS)))
    s.add(Sum(zmienne)>dieta["cel"][parametr]["min"])
    s.add(Sum(zmienne)<dieta["cel"][parametr]["max"])

#        zmienne.append(Sum([skladnik["nazwa"]+str(i) for i in range(5)]))
#        print [skladnik["nazwa"]+str(i) for i in range(5)]
#        print(parametr + " " + str(skladnik[parametr]) + " " + str(dieta["cel"][parametr]["min"]))

print s.check()
print s.model()
