
PONOVLJENO_POLJE = 'o'
import random

class Igra:

    def __init__(self, prazna_polja, zasedena_polja, igralceva_polja, racunalnikova_polja, na_vrsti_igralec):
        self.prazna_polja = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.zasedena_polja = []
        self.igralceva_polja = []
        self.racunalnikova_polja = []
        self.na_vrsti_igralec = True

    def zaznaj_nevarnost(self):
        preprecijo_poraz = []
        if 1 in self.prazna_polja:
            if 2 in self.igralceva_polja and 3 in self.igralceva_polja:
                preprecijo_poraz.append(1)
            elif 5 in self.igralceva_polja and 9 in self.igralceva_polja:
                preprecijo_poraz.append(1)
            elif 4 in self.igralceva_polja and 7 in self.igralceva_polja:
                preprecijo_poraz.append(1)
        if 2 in self.prazna_polja:
            if 1 in self.igralceva_polja and 3 in self.igralceva_polja:
                preprecijo_poraz.append(2)
            elif 5 in self.igralceva_polja and 8 in self.igralceva_polja:
                preprecijo_poraz.append(2)
        if 3 in self.prazna_polja:
            if 2 in self.igralceva_polja and 1 in self.igralceva_polja:
                preprecijo_poraz.append(3)
            elif 5 in self.igralceva_polja and 7 in self.igralceva_polja:
                preprecijo_poraz.append(3)
            elif 6 in self.igralceva_polja and 9 in self.igralceva_polja:
                preprecijo_poraz.append(3)
        if 4 in self.prazna_polja:
            if 1 in self.igralceva_polja and 7 in self.igralceva_polja:
                preprecijo_poraz.append(4)
            elif 5 in self.igralceva_polja and 6 in self.igralceva_polja:
                preprecijo_poraz.append(4)
        if 5 in self.prazna_polja:
            if 2 in self.igralceva_polja and 8 in self.igralceva_polja:
                preprecijo_poraz.append(5)
            elif 4 in self.igralceva_polja and 6 in self.igralceva_polja:
                preprecijo_poraz.append(5)
            elif 1 in self.igralceva_polja and 9 in self.igralceva_polja:
                preprecijo_poraz.append(5)
            elif 7 in self.igralceva_polja and 3 in self.igralceva_polja:
                preprecijo_poraz.append(5)
        if 6 in self.prazna_polja:
            if 3 in self.igralceva_polja and 9 in self.igralceva_polja:
                preprecijo_poraz.append(6)
            elif 5 in self.igralceva_polja and 4 in self.igralceva_polja:
                preprecijo_poraz.append(6)
        if 7 in self.prazna_polja:
            if 1 in self.igralceva_polja and 4 in self.igralceva_polja:
                preprecijo_poraz.append(7)
            elif 5 in self.igralceva_polja and 3 in self.igralceva_polja:
                preprecijo_poraz.append(7)
            elif 8 in self.igralceva_polja and 9 in self.igralceva_polja:
                preprecijo_poraz.append(7)
        if 8 in self.prazna_polja:
            if 2 in self.igralceva_polja and 5 in self.igralceva_polja:
                preprecijo_poraz.append(8)
            elif 7 in self.igralceva_polja and 9 in self.igralceva_polja:
                preprecijo_poraz.append(8)
        if 9 in self.prazna_polja:
            if 1 in self.igralceva_polja and 5 in self.igralceva_polja:
                preprecijo_poraz.append(9)
            elif 3 in self.igralceva_polja and 6 in self.igralceva_polja:
                preprecijo_poraz.append(9)
            elif 7 in self.igralceva_polja and 8 in self.igralceva_polja:
                preprecijo_poraz.append(9)
        return preprecijo_poraz

    def zaznaj_zmago(self):
        zmagovalna_polja = []
        if 1 in self.prazna_polja:
            if 2 in self.racunalnikova_polja and 3 in self.racunalnikova_polja:
                zmagovalna_polja.append(1)
            elif 5 in self.racunalnikova_polja and 9 in self.racunalnikova_polja:
                zmagovalna_polja.append(1)
            elif 4 in self.racunalnikova_polja and 7 in self.racunalnikova_polja:
                zmagovalna_polja.append(1)
        if 2 in self.prazna_polja:
            if 1 in self.racunalnikova_polja and 3 in self.racunalnikova_polja:
                zmagovalna_polja.append(2)
            elif 5 in self.racunalnikova_polja and 8 in self.racunalnikova_polja:
                zmagovalna_polja.append(2)
        if 3 in self.prazna_polja:
            if 2 in self.racunalnikova_polja and 1 in self.racunalnikova_polja:
                zmagovalna_polja.append(3)
            elif 5 in self.racunalnikova_polja and 7 in self.racunalnikova_polja:
                zmagovalna_polja.append(3)
            elif 6 in self.racunalnikova_polja and 9 in self.racunalnikova_polja:
                zmagovalna_polja.append(3)
        if 4 in self.prazna_polja:
            if 1 in self.racunalnikova_polja and 7 in self.racunalnikova_polja:
                zmagovalna_polja.append(4)
            elif 5 in self.racunalnikova_polja and 6 in self.racunalnikova_polja:
                zmagovalna_polja.append(4)
        if 5 in self.prazna_polja:
            if 2 in self.racunalnikova_polja and 8 in self.racunalnikova_polja:
                zmagovalna_polja.append(5)
            elif 4 in self.racunalnikova_polja and 6 in self.racunalnikova_polja:
                zmagovalna_polja.append(5)
            elif 1 in self.racunalnikova_polja and 9 in self.racunalnikova_polja:
                zmagovalna_polja.append(5)
            elif 7 in self.racunalnikova_polja and 3 in self.racunalnikova_polja:
                zmagovalna_polja.append(5)
        if 6 in self.prazna_polja:
            if 3 in self.racunalnikova_polja and 9 in self.racunalnikova_polja:
                zmagovalna_polja.append(6)
            elif 5 in self.racunalnikova_polja and 4 in self.racunalnikova_polja:
                zmagovalna_polja.append(6)
        if 7 in self.prazna_polja:
            if 1 in self.racunalnikova_polja and 4 in self.racunalnikova_polja:
                zmagovalna_polja.append(7)
            elif 5 in self.racunalnikova_polja and 3 in self.racunalnikova_polja:
                zmagovalna_polja.append(7)
            elif 8 in self.racunalnikova_polja and 9 in self.racunalnikova_polja:
                zmagovalna_polja.append(7)
        if 8 in self.prazna_polja:
            if 2 in self.racunalnikova_polja and 5 in self.racunalnikova_polja:
                zmagovalna_polja.append(8)
            elif 7 in self.racunalnikova_polja and 9 in self.racunalnikova_polja:
                zmagovalna_polja.append(8)
        if 9 in self.prazna_polja:
            if 1 in self.racunalnikova_polja and 5 in self.racunalnikova_polja:
                zmagovalna_polja.append(9)
            elif 3 in self.racunalnikova_polja and 6 in self.racunalnikova_polja:
                zmagovalna_polja.append(9)
            elif 7 in self.racunalnikova_polja and 8 in self.racunalnikova_polja:
                zmagovalna_polja.append(9)
        return zmagovalna_polja


    def ali_je_zmagal_racunalnik(self):
        if 1 in self.racunalnikova_polja and 2 in self.racunalnikova_polja and 3 in self.racunalnikova_polja:
            return True
        elif 4 in self.racunalnikova_polja and 5 in self.racunalnikova_polja and 6 in self.racunalnikova_polja:
            return True
        elif 7 in self.racunalnikova_polja and 8 in self.racunalnikova_polja and 9 in self.racunalnikova_polja:
            return True
        elif 1 in self.racunalnikova_polja and 4 in self.racunalnikova_polja and 7 in self.racunalnikova_polja:
            return True
        elif 2 in self.racunalnikova_polja and 5 in self.racunalnikova_polja and 8 in self.racunalnikova_polja:
            return True
        elif 6 in self.racunalnikova_polja and 6 in self.racunalnikova_polja and 9 in self.racunalnikova_polja:
            return True
        elif 1 in self.racunalnikova_polja and 5 in self.racunalnikova_polja and 9 in self.racunalnikova_polja:
            return True
        elif 3 in self.racunalnikova_polja and 5 in self.racunalnikova_polja and 7 in self.racunalnikova_polja:
            return True
        return False
    
    def ali_je_zmagal_igralec(self):
        if 1 in self.igralceva_polja and 2 in self.igralceva_polja and 3 in self.igralceva_polja:
            return True
        elif 4 in self.igralceva_polja and 5 in self.igralceva_polja and 6 in self.igralceva_polja:
            return True
        elif 7 in self.igralceva_polja and 8 in self.igralceva_polja and 9 in self.igralceva_polja:
            return True
        elif 1 in self.igralceva_polja and 4 in self.igralceva_polja and 7 in self.igralceva_polja:
            return True
        elif 2 in self.igralceva_polja and 5 in self.igralceva_polja and 8 in self.igralceva_polja:
            return True
        elif 6 in self.igralceva_polja and 6 in self.igralceva_polja and 9 in self.igralceva_polja:
            return True
        elif 1 in self.igralceva_polja and 5 in self.igralceva_polja and 9 in self.igralceva_polja:
            return True
        elif 3 in self.igralceva_polja and 5 in self.racunalnikova_polja and 7 in self.racunalnikova_polja:
            return True
        return False
        
    def ali_je_remi(self):
        return not self.ali_je_zmagal_igralec() and not self.ali_je_zmagal_racunalnik and len(self.zasedena_polja) == 9
      
    def izberi_polje(self, polje):
        if polje in self.zasedena_polja:
            return PONOVLJENO_POLJE
        self.zasedena_polja.append(polje)
        self.prazna_polja.remove(polje)
        self.igralceva_polja.append(polje)
        if not self.ali_je_zmagal_igralec():
            if len(self.zasedena_polja) != 9:
                if len(self.zaznaj_zmago()) > 0:
                    racunalnikovo_polje = random.choice(self.zaznaj_zmago())
                    self.zasedena_polja.append(racunalnikovo_polje)
                    self.prazna_polja.remove(racunalnikovo_polje)
                    self.racunalnikova_polja.append(racunalnikovo_polje)
                elif len(self.zaznaj_nevarnost()) > 0:
                    racunalnikovo_polje = random.choice(self.zaznaj_nevarnost())
                    self.zasedena_polja.append(racunalnikovo_polje)
                    self.prazna_polja.remove(racunalnikovo_polje)
                    self.racunalnikova_polja.append(racunalnikovo_polje)
                else:
                    racunalnikovo_polje = random.choice(self.prazna_polja())
                    self.zasedena_polja.append(racunalnikovo_polje)
                    self.prazna_polja.remove(racunalnikovo_polje)
                    self.racunalnikova_polja.append(racunalnikovo_polje)


    