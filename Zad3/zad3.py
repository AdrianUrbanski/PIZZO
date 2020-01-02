#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import string
from z3 import *

path = input()
with open(path, 'r') as f:
    dieta = json.load(f)

s = Solver()

zmienne = []
for parametr in dieta["parametry"]:
    zmienne.clear()
    for skladnik in dieta[u"składniki"]:
        ZS = [Int(skladnik["nazwa"].encode("utf-8")+str(i).encode("utf-8")) for i in range(5)]
        for z in ZS:
            s.add(z>=0)
        zmienne.append(skladnik[parametr] * ToReal(Sum(ZS)))
    s.add(Sum(zmienne)>=dieta["cel"][parametr]["min"])
    s.add(Sum(zmienne)<=dieta["cel"][parametr]["max"])

for i in range(5):
    s.add(Sum([Int(skladnik["nazwa"].encode("utf-8")+str(i).encode("utf-8")) for skladnik in dieta[u"składniki"]])>0)

for konflikt in dieta["konflikty"]:
    for i in range(5):
        s.add(Or(Int(konflikt["nazwa1"].encode("utf-8")+str(i).encode("utf-8")) == 0, Int(konflikt["nazwa2"].encode("utf-8")+str(i).encode("utf-8")) == 0))

if(s.check() == unsat):
    print(u"Nie można wygenerować diety.")
else:
    jadlospis = [[],[],[],[],[]]
    m = s.model()
    for d in m.decls():
        for i in range(int(str(m[d]))):
            skladnik = d.name()[:-1]
            posilek = d.name()[-1:]
            jadlospis[int(posilek)].append(skladnik)
    print(u"śniadanie:", end=" ")
    print(", ".join(jadlospis[0]))
    print(u"lunch:", end=" ")
    print(", ".join(jadlospis[1]))
    print(u"obiad:", end=" ")
    print(", ".join(jadlospis[2]))
    print(u"podwieczorek:", end=" ")
    print(", ".join(jadlospis[3]))
    print(u"kolacja:", end=" ")
    print(", ".join(jadlospis[4]))
