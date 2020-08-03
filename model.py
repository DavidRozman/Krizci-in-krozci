



class Igra:

    def __init__(self, prazna_polja, zasedena_polja, igralceva_polja, racunalnikova_polja):
        self.prazna_polja = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.zasedena_polja = []
        self.igralceva_polja = []
        self.racunalnikova_polja = []

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

        


    