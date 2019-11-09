import random


class gracz:
    def __init__(self):
        self.talia_kart = []

    def __repr__(self):
        return f'Gracz - {self.talia_kart}'

    def __str__(self):
        return f'Utworzono gracza do gry WOJNA, z następującą talią kart na ręku: {self.talia_kart}'


opis_kart = {2: (1, '2 pik'), 15: (1, '2 trefl'), 28: (1, '2 karo'), 41: (1, '2 kier'), 3: (2, '3 pik'), 16: (2, '3 trefl'), 29: (2, '3 karo'),
             42: (2, '3 kier'), 4: (3, '4 pik'), 17: (3, '4 trefl'), 30: (3, '4 karo'), 43: (3, '4 kier'), 5: (4, '5 pik'), 18: (4, '5 trefl'),
             31: (4, '5 karo'), 44: (4, '5 kier'), 6: (5, '6 pik'), 19: (5, '6 trefl'), 32: (5, '6 karo'), 45: (5, '6 kier'), 7: (6, '7 pik'),
             20: (6, '7 trefl'), 33: (6, '7 karo'), 46: (6, '7 kier'), 8: (7, '8 pik'), 21: (7, '8 trefl'), 34: (7, '8 karo'), 47: (7, '8 kier'),
             9: (8, '9 pik'), 22: (8, '9 trefl'), 35: (8, '9 karo'), 48: (8, '9 kier'), 10: (9, '10 pik'), 23: (9, '10 trefl'), 36: (9, '10 karo'),
             49: (9, '10 kier'), 11: (10, 'Jopek pik'), 24: (10, 'Jopek trefl'), 37: (10, 'Jopek karo'), 50: (10, 'Jopek kier'), 12: (11, 'Dama pik'),
             25: (11, 'Dama trefl'), 38: (11, 'Dama karo'), 51: (11, 'Dama kier'), 13: (12, 'Król pik'), 26: (12, 'Król trefl'), 39: (12, 'Król karo'),
             52: (12, 'Król kier'), 14: (13, 'As pik'), 27: (13, 'As trefl'), 40: (13, 'As karo'), 53: (13, 'As kier')}


def rozdaj_karty(ilosc_kart):
    cala_talia = range(2,54)
    wylosowana_talia = random.sample(cala_talia, 2 * ilosc_kart)
    karty1 = wylosowana_talia[:ilosc_kart]
    karty2 = wylosowana_talia[ilosc_kart:]
    return karty1, karty2


def utworz_graczy(karty1, karty2, opis_kart):
    gracz1 = gracz()
    gracz2 = gracz()
    for item in karty1:
        gracz1.talia_kart.append(opis_kart[item])
    for kitem in karty2:
        gracz2.talia_kart.append((opis_kart[kitem]))
    return gracz1, gracz2


def tryb_rozgrywki():
    print('Wybierz tryb rozgrywki, masz do wyboru tryb z odrzucaniem kart po walce do stosu kart odrzuconych [0]  \n'
          'lub rozgrywkę, w której zwycięzca pojedynku zabiera wszystkie karty biorące udział w aktualnej bitwie do swojej talii [1]')
    print()
    tryb = -1
    while tryb < 0 or tryb > 1:
        tryb = int(input('Który tryb wybierasz: '))
    print()
    return tryb