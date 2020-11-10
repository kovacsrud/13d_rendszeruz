# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 12:33:30 2020

@author: SysAdmin
"""

#gyakorló feladat: 
# Készítsen véletlen számokból egy 100 elemű listát
# alakítsa numpy tömbbé, adja meg a tömb elemeinek
# összegét, átlagát, legkisebb, legnagyobb elemet

gyakorlo=[]

for i in range(0,100):
    gyakorlo.append(rnd.randint(-100,100))
    

npgyakorlo=np.array(gyakorlo)    

print(npgyakorlo)
print(npgyakorlo.sum())
print(npgyakorlo.mean())
print(npgyakorlo.min())
print(npgyakorlo.max())

print(npgyakorlo[npgyakorlo<0])
print(npgyakorlo[npgyakorlo>=0])
