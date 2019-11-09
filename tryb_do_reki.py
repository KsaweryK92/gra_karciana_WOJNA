import random


def wojna_do_reki(gracz1, gracz2):
    przebieg_rozgrywki = ''
    lista_kart = []
    lista_kart.append(gracz1[0])
    lista_kart.append((gracz2[0]))
    licznik = 1  # ponieważ karta z pozycji [0] bieże udział w wojnie z powodu remisu
    # while bool(len(gracz1)) > 0 and bool(len(gracz2)) > 0:
    print('\tDOGRYWKA')
    przebieg_rozgrywki += '\tDOGRYWKA\n'
    while len(gracz1) and len(gracz2) and licznik < len(gracz1) and licznik < len(gracz2):
        print(f'\tGracz1 wylosował kartę {gracz1[licznik][1]} a Gracz2 wylosował kartę {gracz2[licznik][1]}')
        przebieg_rozgrywki += f'\tGracz1 wylosował kartę {gracz1[licznik][1]} a Gracz2 wylosował kartę {gracz2[licznik][1]}\n'
        lista_kart.append(gracz1[licznik])
        lista_kart.append((gracz2[licznik]))
        if gracz1[licznik][0] > gracz2[licznik][0]:
            print('Zwycięża gracz1')
            przebieg_rozgrywki += 'Zwycięża gracz1\n'
            for item in lista_kart:
                if not item in gracz1:
                    gracz1.append(item)
                if item in gracz2:
                    gracz2.remove(item)
            return gracz1, gracz2, przebieg_rozgrywki
        elif gracz1[licznik][0] < gracz2[licznik][0]:
            print('Zwycięża gracz2')
            przebieg_rozgrywki += 'Zwycięża gracz2\n'
            for item in lista_kart:
                if not item in gracz2:
                    gracz2.append(item)
                if item in gracz1:
                    gracz1.remove(item)
            return gracz1, gracz2, przebieg_rozgrywki
        elif gracz1[licznik][0] == gracz2[licznik][0]:
            print('Remis')
            przebieg_rozgrywki += 'Remis\n'
        licznik += 1
    print('Niemożliwe stało się możliwe, gracze mieli takie same karty')
    przebieg_rozgrywki += 'Niemożliwe stało się możliwe, gracze mieli takie same karty\n'
    gracz1 = []
    gracz2 = []
    return gracz1, gracz2, przebieg_rozgrywki



def tryb_do_reki(gracz1, gracz2):
    przebieg_rozgrywki = ''
    przebieg_wojna = ''
    licznik_gracz1 = 0
    licznik_gracz2 = 0
    # while bool(len(gracz1)) > 0 and bool(len(gracz2)) > 0:
    while len(gracz1) and len(gracz2):
        random.shuffle(gracz1)
        random.shuffle(gracz2)
        print(f'Gracz1 wylosował kartę {gracz1[0][1]} a Gracz2 wylosował kartę {gracz2[0][1]}')
        przebieg_rozgrywki += f'Gracz1 wylosował kartę {gracz1[0][1]} a Gracz2 wylosował kartę {gracz2[0][1]}\n'
        if gracz1[0][0] > gracz2[0][0]:
            print('Zwycięża gracz1')
            przebieg_rozgrywki += 'Zwycięża gracz1\n'
            gracz1.append(gracz2[0])
            del gracz2[0]
            licznik_gracz1 += 1
        elif gracz1[0][0] < gracz2[0][0]:
            print('Zwycięża gracz2')
            przebieg_rozgrywki += 'Zwycięża gracz2\n'
            gracz2.append(gracz1[0])
            del gracz1[0]
            licznik_gracz2 += 1
        else:
            print('Mamy REMIS')
            przebieg_rozgrywki += 'Zwycięża gracz1\n'
            gracz1, gracz2, przebieg_wojna = wojna_do_reki(gracz1, gracz2)
            przebieg_rozgrywki += przebieg_wojna
        input('Naciśnij ENTER, aby kontynuować.')
    if licznik_gracz1 > licznik_gracz2:
        zwyciezca = 'Gracz1'
    elif licznik_gracz2 > licznik_gracz1:
        zwyciezca = 'Gracz2'
    else:
        zwyciezca = 'REMIS'
    return zwyciezca, przebieg_rozgrywki