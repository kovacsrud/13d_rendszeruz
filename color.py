# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 07:34:40 2020

@author: SysAdmin
"""

#színek használata Python-ban

from colorama import Fore,Back,Style

print(Fore.GREEN+"Zöld betűk"+Style.RESET_ALL)
print(Fore.BLUE,Back.MAGENTA,Style.NORMAL+"Magenta háttér"+Style.RESET_ALL)
print("Nincs szín elvileg")


szamok=[19,233,45,68,122,411,62,69,76]

#Jelöljük meg háttér és szövegszínnel a szamok lista 2-vel osztható számait.
for i in szamok:
    if(i%2==0):
        print(Fore.RED+str(i)+Style.RESET_ALL)
    else:
        print(i)