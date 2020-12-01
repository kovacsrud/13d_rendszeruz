import random as rnd
#Szótár adatszerkezet
# A szótár adatszerkezet kulcs-érték párokat tárol. A kulcs csak egyszer szerepelhet a szótárban.

magassagok={}
# Értékek megadása
magassagok['Zoltán']=175
magassagok['Imre']=188
magassagok['Ágnes']=171
magassagok['Jolán']=166

#Hozzáférés egy értékhez
print(magassagok['Zoltán'])
print(magassagok['Ágnes'])

#Kulcsok kiíratása
print(magassagok.keys())
print(magassagok.values())
print(magassagok.items())

# Kiíratás for ciklussal
for i in magassagok:
    print(i+","+str(magassagok[i]))

for i in magassagok.keys():
    print(i)
#kulcshoz tartozó érték módósítása
magassagok['Zoltán']=195

#kiíratás az elemek(items) alapján
for i,j in magassagok.items():
    print("Kulcs:{},érték:{}".format(i,j))

# elemek törlése

magassagok.pop('Zoltán')
print(magassagok.items())

#utolsó elem törlése
magassagok.popitem()
print(magassagok.items())

magassagok.clear()
print(magassagok.items())


nevek=["Tamás","Jolán","Elek","Imre","Róbert","Mihály","Anita","Zoltán"]

szamok=[12,120,44,55,66,77,88,99,66]

legm=list(filter(lambda x:x==max(x.mag),szamok))
print("legm:"+str(legm))

soknev=[]
elemszam=1000

for i in range(0,elemszam):
    soknev.append(nevek[rnd.randint(0,len(nevek)-1)])

print(soknev)

# Jelenítsük meg, hogy az egyes nevek hányszor szerepelnek a szótárban

nevgyujt={}

for i in soknev:
    if i in nevgyujt:
        nevgyujt[i]+=1
    else:
        nevgyujt[i]=1

for i,j in nevgyujt.items():
    print("{}:{}".format(i,j))


