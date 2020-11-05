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

def atlag(lista):
    osszeg=0
    for i in range(0,len(lista)):
        osszeg=osszeg+lista[i]
    return osszeg/len(lista)   

def min(lista):
    min=lista[0]
    for i in range(0,len(lista)):
        if(lista[i]<min):
            min=lista[i]
    return min        

def max(lista):
    max=lista[0]
    for i in range(0,len(lista)):
        if(lista[i]>max):
            max=lista[i]
    return max  

## pozitívak darabszáma

##a veletlenlista függvény meghívása

szamok=veletlenlista(10,0,100) 
szamok2=veletlenlista(30,-100,100)   
print(szamok)
print(min(szamok))
print(max(szamok))
print(osszeg(szamok))
print(atlag(szamok))

print(osszeg(szamok2))
print(atlag(szamok2))





    

