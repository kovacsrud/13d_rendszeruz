# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 12:38:00 2020

@author: SysAdmin
"""

#Összegzés 
szamok=[122,41,567,78,299,69,19,736,344]

#Állapítsuk meg, hogy mennyi a lista elemeinek összege

osszeg=0

#for ciklus a lehető legegyszerűbben
for i in szamok:
    osszeg+=i
    
print("Az összeg:"+str(osszeg))    
