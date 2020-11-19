import datetime as dt

class Szemely:
    def __init__(self,vezeteknev,keresztnev,szuletesiev,szuletesihely):
        self.vezeteknev=vezeteknev
        self.keresztnev=keresztnev
        self.szuletesiev=int(szuletesiev)
        self.szuletesihely=szuletesihely
    def Eletkor(self):
        datum=dt.datetime.now()
        return datum.year-self.szuletesiev


fajl=open("g:/nevsor_20k.txt",'r')

adatok=[]

for sor in fajl:
    elemek=sor.strip().split(',')
    szemely=Szemely(elemek[0],elemek[1],elemek[2],elemek[3])
    adatok.append(szemely)

fajl.close()

print(len(adatok))

szuletes1980=list(filter(lambda x:x.szuletesiev==1980,adatok))

print(len(szuletes1980))

fajl=open("nevsor_1980.txt",'w',encoding="utf-8")

for sor in szuletes1980:
    fajl.write(sor.vezeteknev+","+sor.keresztnev+","+str(sor.szuletesiev)+","+sor.szuletesihely+"\n")

fajl.close()

negyvenesek=list(filter(lambda x:x.Eletkor()>=40 and x.Eletkor()<=50,adatok))

fajl=open("nevsor_40-50.txt",'w',encoding="utf-8")

for sor in negyvenesek:
    fajl.write(sor.vezeteknev+","+sor.keresztnev+","+str(sor.Eletkor())+","+sor.szuletesihely+"\n")

fajl.close()