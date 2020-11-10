# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 11:25:21 2020

@author: SysAdmin
"""

import numpy as np

szamok=[11,22,36,69,112,336,788,211,678,223]

npszamok=np.array(szamok)

print(npszamok)

# információk

#elemszám
print(npszamok.size)
#dimenziók száma
print(npszamok.shape)

#elemek indexelése
print(npszamok[5])

#elemi algoritmusok egyszerűen
print(npszamok.sum())
print(npszamok.mean())
print(npszamok.min())
print(npszamok.max())

#kiválogatások
print(npszamok>40)
print(npszamok[npszamok>40])
print(npszamok[npszamok>40].sum())

