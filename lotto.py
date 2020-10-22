# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 09:39:01 2020

@author: SysAdmin
"""

from colorama import Fore,Back,Style
import random as rnd

tippek=[]
nyeroszamok=[]

print("Hány számmal játszunk?:",end="")
hanySzam=int(input())

print("Mennyiből sorsolunk?:",end="")
osszSzam=int(input())

for i in range(0,hanySzam):
    print(str(i+1)+" tipp:")
    atmeneti=int(input())
    while(atmeneti<1 or atmeneti>osszSzam or atmeneti in tippek):
        print("Rossz tipp,újra! "+str(i+1)+" tipp:")
        atmeneti=int(input())
    tippek.append(atmeneti)    

for i in range(0,hanySzam):
    atmeneti=rnd.randint(1,osszSzam)
    while(atmeneti in nyeroszamok):
        atmeneti=rnd.randint(1,osszSzam)
    nyeroszamok.append(atmeneti)    
    

print(tippek)    
print(nyeroszamok)


