# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 08:43:31 2020

@author: SysAdmin
"""


# Írjon programot, amely hőmérséklet adatokat
# kér be. A bekérés addig folytatódjon, amíg
# negatív értéket nem adnak meg.
# Számoljuk meg, hogy hány darab értéket adtak meg

ho=int(input())
darabszam=1

while(ho>-1):
    print(ho)
    print("Darabszám:"+str(darabszam))
    ho=int(input())
    darabszam+=1
    
print(darabszam)    
    