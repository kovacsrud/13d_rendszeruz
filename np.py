# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 11:25:21 2020

@author: SysAdmin
"""

import numpy as np
import random as rnd

szamok=[11,22,36,69,112,336,788,211,678,223,626,6969]

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

#kiválogatások, egy feltétel
print(npszamok>40)
print(npszamok[npszamok>40])
print(npszamok[npszamok>40].sum())


#kiválogatások, több feltétel
print((npszamok>40) & (npszamok<200))
print(npszamok[(npszamok>40) & (npszamok<200)])

# elemek kiválogatása index szerint
print(npszamok)
print(npszamok[3:6])
print(npszamok[3:])
print(npszamok[:3])

print(npszamok.shape)
print(npszamok.reshape(2,6))
print(npszamok.reshape(6,2))
print(npszamok.reshape(3,4))
print(npszamok.reshape(4,3))


