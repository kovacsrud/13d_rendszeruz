# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:19:29 2020

@author: SysAdmin
"""

import numpy as np

# Tömbök
# Azonos típusú elemeket tartalmazó adatszerkezet
# Az elemek számozása 0-tól kezdődik
szamok=[1,236,554,677,12,998,332,67,191,111,704,268]



print(szamok[0])
print(szamok[3])

print(len(szamok))

#Kiíratható
print(szamok)

#For ciklus
# A tömb elemeinek listázása

for i in szamok:
    print(i)
    
print("Ez már a for ciklus után van")    
    
# A range használata
# A range segítségével egy számsort készíthetünk

r=range(0,20)
print(*r)

# A for ciklus végig megy a tömbön és
# minden elemhez hozzáad 10-et

for i in range(0,len(szamok)):
    szamok[i]+=10;
    #szamok[i]=szamok[i]+10
    print(str(i)+":"+str(szamok[i]))
    
szovegek=["egy","kettő","három","négy","öt"]

for i in szovegek:
    print(i)
    

szovegek.append("hat")


print(szovegek)


