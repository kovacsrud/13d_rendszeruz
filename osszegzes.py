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
print("Átlag:"+str(osszeg/len(szamok)))

osszeg=0

#for ciklus a range használatával
for i in range(0,len(szamok)):
    osszeg+=szamok[i]
    print(str(i)+","+str(szamok[i]))

print("Az összeg:"+str(osszeg))    
print("Átlag:"+str(osszeg/len(szamok)))

osszeg=0
# valósítsuk meg az összegzést while ciklussal
szamlalo=0
while(szamlalo<len(szamok)):
    osszeg+=szamok[szamlalo]
    print(str(szamlalo)+","+str(szamok[szamlalo]))
    szamlalo+=1
    
print("Az összeg:"+str(osszeg))    
print("Átlag:"+str(osszeg/len(szamok)))    
    
#min, max kiválasztás
min=szamok[0]
max=szamok[0]

for i in range(0,len(szamok)):
    if(szamok[i]<min):
        min=szamok[i]
    if(szamok[i]>max):
        max=szamok[i]
        
print("Min:"+str(min))
print("Max:"+str(max))

#min, max while ciklussal