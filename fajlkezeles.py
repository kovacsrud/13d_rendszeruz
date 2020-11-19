
#Fájlok kezelése

# A fájl tartalmának beolvasása egyetlen változóba
fajl=open("g:/nevsor.txt",'r',encoding="utf8")

tartalom=fajl.read()

fajl.close()

#print(tartalom)

# A fájl olvasása listába

fajl=open("g:/nevsor.txt",'r',encoding="utf8")

nevek=fajl.readlines()


print(nevek)
print(nevek[0].strip())
print(nevek[3])

fajl.close()

fajl=open("g:/nevsor.txt",'r',encoding="utf8")

vnevek=[]
knevek=[]
szev=[]
szhely=[]

for sor in fajl:
    elemek=sor.strip().split(',')
    #print("Vezetéknév:"+elemek[0]+" Keresztnév:"+elemek[1])
    print(elemek)
    vnevek.append(elemek[0])
    knevek.append(elemek[1])
    szev.append(elemek[2])
    szhely.append((elemek[3]))


print(vnevek)
print(knevek)
print(szev)
print(szhely)

fajl.close()

#Írás fájlba

fajl=open("g:/kiirminta.txt",'w',encoding="utf-8")

ezt_kiirjuk="Valami szöveg ékezetes betűkkel"

fajl.write(ezt_kiirjuk)

fajl.close()

fajl=open("g:/kiirlista.txt",'w',encoding="utf-8")

for i in vnevek:
    fajl.write(i+"\n")



fajl.close()