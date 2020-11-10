# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 08:34:03 2020

@author: SysAdmin
"""

# Írjon függvényt, amely két szám közül visszaadja
# a kisebbet!

# Írjon függvényt, amely egy szöveget, valamint egy
# karaktert kap bemenő adatként. A függvény számolja meg,
# hogy a kapott karakter hányszor szerepel a szövegben
# pl. karszam("abaaba","a")

def nagyobb(a,b):
    if(a>b):
        return a
    else:
        return b
    
def karszam(szoveg,betu):
    db=0
    for i in szoveg:
        if(i==betu):
            db+=1
    return db        
    
#♦print(nagyobb(4,2))    
#print(nagyobb(2,4))    

print(karszam("ababbab","b"))
print(karszam("ababbab","a"))
print(karszam("ababbab","x"))

#Írjon egy olyan függvényt amely egy szövegről eldönti,
#hogy IP-cím-e(IPv4) ! 126.244.11.67

a=234
ip="122.122.ezo.122"

ipparts=ip.split('.')
print(ipparts)


for i in ipparts:
    if(i.isnumeric()):
        print("Szám")


