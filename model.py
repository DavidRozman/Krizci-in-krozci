import uuid

class Igralec:
    def __init__(self, ime=None, je_racunalnik=None):
        self.ime = ime
        self.je_racunalnik = je_racunalnik
        self.tocke = 0


class Plosca:
    class POLJA:
        PRAZNO_POLJE = 0
        KRIZEC = 1
        KROGEC = 2
    
    def __init__(self, igralec1=None, igralec2=None):
        self.polja = [[0,0,0], [0,0,0], [0,0,0]]
        self.igralec1 = igralec1
        self.igralec2 = igralec2
        self.id = uuid.uuid4().int
        self.konec = False
        self.zmagovalec = None
    def narisi(self):
        for vrstica in self.polja:
            for stolpec in vrstica:
                print(stolpec, end= ' ')
            print()
    def vnos(self, x, y, igralec):
        # preveri ali je polje prosto
        # preveri ali polje obstaja 
        self.polja[y][x] = igralec
        if self.polja[0][0] == 1:
            self.konec = True
            self.zmagovalec = self.igralec1
    


