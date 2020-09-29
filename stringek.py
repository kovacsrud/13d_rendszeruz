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








