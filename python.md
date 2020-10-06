
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

### FOR ciklus

Ez a ciklus jó választás egy adatszerkezet elemeinek bejárására.
Tömb elemeinek a kiíratása FOR-al:
```py
for i in szamok:
    print(i)
```
Fontos, hogy a FOR-hoz tartozó utasításoknak ugyanakkora behúzással kell szerepelniük.

