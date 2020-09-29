# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:31:04 2020

@author: SysAdmin
"""
# Műveletek szövegekkel

a="valami szöveg"
b="ValAmi sZöveG"


if(a.lower()==b.lower()):
    print("Megegyeznek")
else:
    print("Nem egyeznek meg")    
    
print(a.upper())    
print(b.lower())

# Kezdődés, végződés vizsgálata

print(a.startswith("val"))
print(a.startswith("van"))

print(b.endswith("eG"))
print(b.endswith("eg"))


#Tartalmaz-e egy szöveget egy másik
print(a.find("lal"))

# Hányszor tartalmazza, ha tartalmazza
print(a.count("x"))

#Kartakterek cseréje a szövegben
print(a.replace("a","x"))

#Szöveg darabolás

adat="Kozma Ubul,1986,Szeged,112667"

adatok=adat.split(",")

# Egy adott tömbelem kiíratása
print(adatok)

# Részletek kiemelése egy szövegből

datum="2018.12.26"

ev=datum[0:4]
honap=datum[5:7]
nap=datum[8:]

print(ev)
print(honap)
print(nap)

#Csak az utolsó 3 karakter
print(datum[-3:])

#Az utolsó 3 karakter kivételével minden
print(datum[:-3])

# Vizsgálatok

c="2"
print(c.isdigit())
print(c.isalpha())
print(c.isalnum())







