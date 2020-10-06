# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 08:21:53 2020

@author: SysAdmin
"""

# Írjon programot, amely bekér két
# számot,(a,b) majd elvégzi a következő műveletet
# c=a/b, és kiíratja c értékét

a=int(input())
b=int(input())

# b értékének nem fogadhatunk el 0-t!
while(b==0):
    print("0-val nem lehet osztani!")
    b=int(input())
    

c=a/b

print(c)



