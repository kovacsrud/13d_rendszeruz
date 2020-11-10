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
# példák a lehetséges átalakításra
print(npszamok.reshape(2,6))
print(npszamok.reshape(6,2))
print(npszamok.reshape(3,4))
print(npszamok.reshape(4,3))

# egy 3 sorból, 4 oszlopból álló
# tömbbé alakítjuk az eredetit
npszamok2=npszamok.reshape(3,4)

#a dimenziók kiíratása
print(npszamok2.shape)

print(npszamok2)
print(npszamok2[0,0])
print(npszamok2[0,1])
print(npszamok2[1,1])

# Gyakorló feladat: For ciklusok segítségével
# írassa ki az npszamok2 tömb elemeit

for i in range(0,npszamok2.shape[0]):
    for j in range(0,npszamok2.shape[1]):
        print(npszamok2[i,j],end=" ")
    print(" ")    

        
