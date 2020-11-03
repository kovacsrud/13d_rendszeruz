# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:58:57 2020

@author: SysAdmin
"""
## Programozási tételek függvényekkel

import random as rnd

def veletlenlista(db,also,felso):
    lista=[]
    for i in range(0,db):
        lista.append(rnd.randint(also,felso))
    return lista

def osszeg(lista):
    osszeg=0
    for i in range(0,len(lista)):
        osszeg=osszeg+lista[i]
    return osszeg    

## pozitívak darabszáma

##a veletlenlista függvény meghívása

szamok=veletlenlista(10,0,100) 
szamok2=veletlenlista(30,-100,100)   

print(osszeg(szamok))
print(osszeg(szamok2))





    

