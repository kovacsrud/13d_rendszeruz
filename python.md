
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
