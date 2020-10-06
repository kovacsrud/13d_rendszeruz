# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:03:50 2020

@author: SysAdmin
"""

pozitiv=0
negativ=0

ho=int(input())

while(ho!=0):
    if(ho>0):
        pozitiv+=1
    else:
        negativ+=1
    ho=int(input())    
        
  

print("Pozitív:"+str(pozitiv))      
print("Negatív:"+str(negativ))      