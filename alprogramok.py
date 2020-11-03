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


##a veletlenlista függvény meghívása

szamok=veletlenlista(10,0,100) 
szamok2=veletlenlista(30,-100,100)   

print(szamok)
print(szamok2)





    

