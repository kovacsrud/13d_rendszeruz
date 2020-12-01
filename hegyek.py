import numpy as np
class Hegycsucs:
    def __init__(self,hegycsucsneve,hegyseg,magassag):
        self.hegycsucsneve=hegycsucsneve
        self.hegyseg=hegyseg
        self.magassag=int(magassag)

hegycsucsok=[]

#fájl megnyitása
fajl=open("g:/hegyekMo.txt",'r',encoding="utf-8")

#Első sor átlépése
fajl.readline()

for i in fajl:
    elemek=i.strip().split(';')
    hegycsucs=Hegycsucs(elemek[0],elemek[1],elemek[2])
    hegycsucsok.append(hegycsucs)

fajl.close()

print("A hegyek száma a fájlban:{}".format(len(hegycsucsok)))

#Összegzés elemi algoritmus
osszmagassag=0

szamf=3123.122334

print("{:0.2f}".format(szamf).strip('0').strip('.'))

for i in hegycsucsok:
    osszmagassag+=i.magassag



print("Az átlagos magasság:{}".format(osszmagassag/len(hegycsucsok)))

#elemi algoritmus a legmagasabb hegy meghatározására
maxmagassag=0;

for i in hegycsucsok:
    if i.magassag>maxmagassag:
        maxmagassag=i.magassag

print(maxmagassag)

maxhegy=list(filter(lambda x:x.magassag==maxmagassag,hegycsucsok))

print(maxhegy[0].hegycsucsneve)

#Vajon a max nem tudja ezt?

maxhegy2=max(hegycsucsok,key=lambda x:x.magassag)

print("A legmagasabb hegycsúcs neve:{},magassága:{}".format(maxhegy2.hegycsucsneve,maxhegy2.magassag))

print("Adjon meg egy magasságot:",end="")
bemagassag=int(input())

borzsony=list(filter(lambda x:x.magassag>bemagassag and x.hegyseg=="Börzsöny",hegycsucsok))

if len(borzsony)>0:
    print("Van magasabb!")
else:
    print("Nincs magasabb")

magasabb3000=list(filter(lambda x:x.magassag*3.28>3000,hegycsucsok))

print("3000 lábnál magasabbak:{}".format(len(magasabb3000)))

#üres szótár létrehozása
hegysegstat={}

for i in hegycsucsok:
    if i.hegyseg in hegysegstat:
        hegysegstat[i.hegyseg]+=1
    else:
        hegysegstat[i.hegyseg] = 1

for i,j in hegysegstat.items():
    print("{} - {} db".format(i,j))

#szűrés a fájlba íráshoz
bukkvidek=list(filter(lambda x:x.hegyseg=="Bükk-vidék",hegycsucsok))

#fájlba írás
fajl=open("bukk-videk.txt",'w',encoding="utf-8")

fajl.write("Hegycsúcs neve;Magasság láb"+"\n")

for i in bukkvidek:
    fajl.write("{};{:0.1f}\n".format(i.hegycsucsneve,i.magassag*3.28).strip('0').strip('.'))

fajl.close()

