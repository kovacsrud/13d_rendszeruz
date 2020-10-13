# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:51:55 2020

@author: SysAdmin
"""
import random as rnd

darabszam=0
# Oldja meg, hogy a ciklus után látható legyen, hogy hányszor futott le
# a ciklus
ciklusszamlalo=0
#legyen a bemenő adat egy véletlen szám
szam=rnd.randint(-100,100)

#ciklus, amíg 0-t nem adnak meg
while(szam!=0):
    if(szam%2==0):
        print(str(szam)+" osztható 2-vel")
        darabszam+=1
    else:
        print(str(szam)+" nem osztható 2-vel")
    szam=rnd.randint(-100,100)
    ciklusszamlalo+=1
    
print("Ennyi osztható 2-vel:"+str(darabszam))    
print("Ennyiszer futott a ciklus:"+str(ciklusszamlalo))


