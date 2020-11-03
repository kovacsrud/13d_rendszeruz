# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 07:52:50 2020

@author: SysAdmin
"""

#Keresés és kiválogatás

szamok=[10,-2,122,-31,-19,26,33,-121,59]
#Üres lista
negativak=[]

#ciklus a szamok listan
for i in range(0,len(szamok)):
    if(szamok[i]<0):
        negativak.append(szamok[i])

        
print(negativak)        

#Megszámlálás
darab=0

for i in range(0,len(szamok)):
    if(szamok[i]>-1):
        #darab=darab+1
        darab+=1

print(darab)

#Összegzés    
osszeg=0

for i in range(0,len(szamok)):
    osszeg+=szamok[i]
    
print(osszeg)    

#Csak a pozitívak összege
osszeg=0

for i in range(0,len(szamok)):
    if(szamok[i]>-1):
        osszeg+=szamok[i]

print(osszeg)        

#Minimum, maximum kiválasztása
min=szamok[0]
max=szamok[0]


