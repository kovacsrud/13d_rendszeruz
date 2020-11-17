import random as rnd


class Szemely:
    def __init__(self,vezeteknev,keresztnev,szuletesiev,szuletesihely):
        self.vezteknev=vezeteknev
        self.keresztnev=keresztnev
        self.szuletesiev=szuletesiev
        self.szuletesihely=szuletesihely
    def Eletkor(self):
        return 2020-self.szuletesiev


vezeteknevek=["Kiss","Kovács","Horváth","Nagy","Tipi","Kertész","Áchim"]
keresztnevek=["István","Péter","Jolán","Zoltán","Anita","Dániel","Aranka"]
helyisegek=["Békéscsaba","Gyula","Szeged","Bélmegyer","Sopron","Lenti","Csorvás","Gerendás"]

szemelyek=[]

adatmennyiseg=500

for i in range(0,adatmennyiseg):
    szemely=Szemely(
        vezeteknevek[rnd.randint(0,len(vezeteknevek)-1)],
        keresztnevek[rnd.randint(0,len(keresztnevek)-1)],
        rnd.randint(1930,2020),
        helyisegek[rnd.randint(0,len(helyisegek)-1)]
    )
    szemelyek.append(szemely)

print(len(szemelyek))

for i in range(0,len(szemelyek)):
    print(szemelyek[i].vezteknev+","+szemelyek[i].keresztnev+","+str(szemelyek[i].szuletesiev)+","+szemelyek[i].szuletesihely)


#1975-ben születettek

szuletes1975=list(filter(lambda x:x.szuletesiev==1975,szemelyek))

print(len(szuletes1975))

for i in range(0,len(szuletes1975)):
    print(szuletes1975[i].vezteknev)

# születési év egy tartományba esik pl. 1975-1999

szuletes7599=list(filter(lambda x:x.szuletesiev>=1975 and x.szuletesiev<=1990,szemelyek))

print(len(szuletes7599))

for i in range(0,len(szuletes7599)):
    print(szuletes7599[i].vezteknev)

kovacsok=list(filter(lambda x:x.vezteknev=="Kovács",szemelyek))

print(len(kovacsok))

huszevesek=list(filter(lambda x:x.Eletkor()==20,szemelyek))

print(len(huszevesek))

idosek=list(filter(lambda x:x.Eletkor()>=60 and x.Eletkor()<=90,szemelyek))

print(len(idosek))