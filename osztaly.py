
class Ember:
    def __init__(self,nev,kor):
        self.nev=nev
        self.kor=kor

    def kiir(self):
        print(self.nev)



ember=Ember("Ubul",29)

ember.kiir()

print(ember.nev+":"+str(ember.kor))

ember2=Ember("Zénó",30)

emberek=[]

emberek.append(ember)
emberek.append(ember2)

print(emberek[0].nev)
emberek[1].kiir()