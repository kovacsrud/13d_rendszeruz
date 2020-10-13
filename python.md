
# A Python nyelv

Általános, nagyon széles körben használt interpretált programnyelv. Számos rugalmasan használható adatszerkezetet lehet használni benne, néha pont ettől nehéz.

Az első Python program:
```python
print("Hello world!")
```

A print utasítás kiírja (ha nincs hiba) az adott kifejezés eredményét, vagy egy változó értékét

```python
print(2+2+6)

print(2+(6*10))

print(10/3)

print(10/0)
```
A 0-val való osztáskor hibát kapunk.

### Szövegekkel való műveletek
A + jel hatására a karakter vagy szöveg típusú adatok össze lesznek fűzve.

```python
print("2"+"2")
print("valami "+"szöveg")
```
A Python automatikusan kezeli a változók típusát. Emiatt figyelni kell arra, hogy egy művelet különböző típusokkal végrehajtva
más eredményt adhat.

```python
a=12
b=25



print(a+b)

a="12"
b="25"

print(a+b)
```

Ha az egyik változó szöveg, a másik szám, akkor valamilyen szöveges eredményt fogunk kapni egy művelet elvégzésekor.

```python
a="valami"
b=3

print(a*b)
```
Az eredmény:valamivalamivalami

Értékadó utasítások:

```python
a=10
b=2
a+=b
print(a)

a-=b
print(a)

a*=b
print(a)

a/=b
print(a)
```
### Felhasználói adatbevitel

Az **input()** függvény segítségével lehet bekérni adatot egy változóba a felhasználótól. A beolvasott adat típusa ebben az esetben mindig **string** azaz szöveges adat.

```python
a=input()
b=input()

print(a+b)
```

Amennyiben számként akarjuk kezelni a beolvasott adatot, az int() függvénnyel konvertálni kell az input() által beolvasott értéket a 
megfelelő típusra.

```python
print("A:")
a=int(input())

print("B:")
b=int(input())

print(a+b)
```

Ha a bevitelkor nem egész számokat akarunk megadni, akkor a **float()** függvénnyel kell a bevitt értéket konvertálni. Ellenkező
esetben hibát kapunk futtatáskor.

```python
print("A:")
a=float(input())

print("B:")
b=float(input())

print(a+b)
```
### Összehasonlító műveletek

Eredményük mindig egy logikai érték (igaz/hamis) vagy másképpen (true/false)

```python
a=12
b=21
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
```
### Elágazások a Pythonban

**Egyszeres egyágú elágazás**
```python
a=5

if (a>3):
    print("Nagyobb")
    
    
print("Itt a vége")
```
**Egyszeres, kétágú elágazás**

Ebben az esetben az ELSE ág az elágazás másik ága

```python
if (a>=3):
    print("Nagyobb v. egyenlő")    
else:
    print("Kisebb")  
```
**Többszörös elágazás**
```py
b=6

if (b==10):
    print("Tíz") 
elif(b==2):
       print("Kettő")
elif(b==6):
       print("Hat")
else:
    print("Egyéb")    
     
print("Itt a vége")
```    
### Műveletek szöveges változókkal

```py
a="valami"
b="ValAmi"
```
**Megjelenítés kisbetűsen**
```py
print(b.lower())
```
**Megjelenítés nagybetűsen**
```py
print(a.upper())
```

**Szövegek összehasonlítása**
```py
a="valami"
b="ValAmi"

if(a==b):
    print("Megegyeznek")
else:
    print("Nem egyeznek meg")   
```
A fenti kódot futtatva azt kapjuk, hogy a szövegek nem egyeznek meg. Tartalmilag igen, de az eltérő írásmód miatt különbözőnek tekinti őket a program.

Amennyiben arra vagyunk kíváncsiak, hogy a tartalmuk is egyezik-e, úgy azonos írásmóddal (kisbetűs, nagybetűs) kell őket összehasonlítani.
```py
a="valami"
b="ValAmi"

if(a.upper()==b.upper()):
    print("Megegyeznek")
else:
    print("Nem egyeznek meg")   
```

Így azt kapjuk, hogy megegyeznek.

### Egy string kezdete, vége megegyezik egy másik szöveggel?

```py
a="valami"
b="ValAmi"
print(a.startswith("va"))    
print(a.endswith("ami"))   
```

**Szövegrész keresése egy másik szövegben**
```py
a="valami"
print(a.find("laza"))
```
A find funkció -1 et ad vissza, ha az megadott szöveg nem szerepel a szöveges változóban. Ha a megadott szöveget tartalmazza a változó, akkor a szövegrész kezdő indexét adja vissza.

**Hányszor tartalmazza az adott szöveg a megadottat**
A count() fogja ezt megmondani.
```py
print(a.count("la"))
```
**Szövegrészek cseréje**
```py
a="valami"
print(a.replace("a","b"))
```

**Logikai vizsgálatok**
```py
c="a"
print(c.isdigit())
print(c.isalnum())
```
Az első esetben vizsgáljuk, hogy c szám-e, a másodikban, hogy c alfanumerikus karakter-e.

**Szövegek darabolása**
Gyakori feladat, hogy felosszunk egy szöveget, több részre. A **split** funkció fogja ezt elvégezni, amelynek azt a karaktert kell megadni,
amelyik mentén a szöveget fel akarjuk darabolni. A darabolás eredményeképpen egy tömb jön létre.
```py
adat="Kiss Elek,1989,Szeged,442669"
adatok=adat.split(",")
print(adatok)
```

**Szövegrész kiemelése az adott szöveges változóból**

Nézzük az alábbi szöveges változót, ami egy dátumot tárol:
```py
datum="2019.12.23"
```
Hogyan lehet kiemelni csak az évet?
```py
ev=datum[0:4]
```
A szögletes zárójelek között azt adjuk meg, hogy mely karaktertől kezdve, mely karakterig emeljük(másoljuk) ki a szövegből.
```py
honap=datum[5:7]
nap=datum[8:]
```
**További megoldások:**
A szöveg utolsó 3 karaktere:
```py
print(datum[-3:])
```
A szöveg összes karaktere az utolsó 3 kivételével
```py
print(datum[:-3])
```

### Tömbök

Azonos típusú elemeket tartalmazó adatszerkezet.
Az elemek számozása 0-tól kezdődik.
```py
szamok=[1,236,554,677,12,998,332,67,191,111,704,268]
```
**Adott indexű elem kiíratása**
```py
print(szamok[0])
print(szamok[3])
```

**Tömb elemszámának kiíratása**
```py
print(len(szamok))
```
**Tömb/lista elemeinek bővítése**
```py
nevek=[]
nevek.append('Ubul')
nevek.append('Zénó')
```
Az **append** paranccsal a lista végére tudunk új elemet beszúrni.

**Beszúrás a lista egy adott helyére**
```py
nevek.insert(0,'Jolán')
nevek.insert(2,'Janka')
```
Az **insert** parancsnak meg tudjuk adni azt az indexet, ahová be kell szúrni az új elemet, így már létező elemek közé is be tudunk szúrni újat.

**Lista kiürítése**
```py
nevek.clear()
```
A **clear()** parancs használata után a lista üres.

### FOR ciklus

Ez a ciklus jó választás egy adatszerkezet elemeinek bejárására.
Tömb elemeinek a kiíratása FOR-al:
```py
for i in szamok:
    print(i)
```
Fontos, hogy a FOR-hoz tartozó utasításoknak ugyanakkora behúzással kell szerepelniük.

### A Range() függvény
A RANGE() függvény egy számsort készít, amely felhasználható egy adatszerkezet bejárásakor.

```py
r=range(0,20)
print(*r)
```

A RANGE() gyakran szerepel a FOR ciklusban is.

```py
for i in range(0,len(szamok)):
    szamok[i]+=10;
    print(str(i)+":"+str(szamok[i]))
```

### Elöltesztelő ciklus, WHILE

A WHILE ciklusnál egy belépési feltételt kell megfogalmazni, a ciklus mindaddig fut, amíg a belépési feltétel teljesül.
Fontos gondoskodni arról, hogy a ciklus futása véget tudjon érni.

**Egy elrontott WHILE**
```py
a=0
while (a<20):
    print(a)
```
Észre kell venni, hogy a értéke nem módosul, ezért ez a ciklus egy ún. végtelen ciklus.

**Az előbbi példa helyesen**
```py
while (a<20):
    print(a)
    a+=1
```
Látszik, hogy **a** értéke minden egyes végrehajtáskor nő, így a ciklus **a=20** értéknél befejezi a futását.

### Keresés listában
A  klasszikus módszer az az hogy egy ciklussal végigmegyek a listán, minden elemet összehasonlítok a keresett elemmel. Ha van a keresett elemmel megegyező elem, akkor
egy logikai változó értékének az True-ra állításával jelzem ez, illetve a **break** parancs használatával megszakítom a ciklust, hogy ne fusson tovább feleslegesen.

```py
nevek=['Ubul','Elek','Jakab','Tamás','Eleonóra']
keres='Ubul'
megvan=True
for i in nevek:
    if(i==keres):
        megvan=False
        break
print(megvan)        
```
Nyilván ezt fáradtságos lenne mindig megírni, ezért a Python-ban (és más nyelvekben is természetesen) van beépített funkció arra, meg meg tudjuk nézni, hogy egy elem szerepel-e egy listában. Python-ban az ***in*** operátor vizsgálja meg, hogy egy érték megtalálható-e egy listában. Eredményül mindig egy logikai értéket(True/False) kapunk.
```py
nevek=['Ubul','Elek','Jakab','Tamás','Eleonóra']
keres='Ubul'
print(keres in nevek)
```

### Véletlen számok generálása

Véletlen számok generálásához Python-ban be kell tölteni a random modult. A betöltött modulnak az **as** kulccszóval adunk egy olyan nevet, amelyen a programból hivakozunk rá.
```py
import random as rnd
```
Egy véletlen érték generálása a **randint** paranccsal végezhető el, meg kell adnunk, hogy milyen határok között akarunk értékeket generálni. A parancs a modul nevén belül szerepel, ponttal elválasztva.
```py
veletlenszam=rnd.randint(0,100)
```
