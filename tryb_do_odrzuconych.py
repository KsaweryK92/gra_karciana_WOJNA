def wojna_do_odrzuconych(gracz1, gracz2, licznik_potyczek):
    przebieg_rozgrywki = ''
    licznik_bitew = 0
    # for i in range(licznik_potyczek + 1, len(gracz1) - 1):
    for i in range(licznik_potyczek + 1, len(gracz1)):
        print(f'\tGracz1 wylosował kartę {gracz1[i][1]} a Gracz2 wylosował kartę {gracz2[i][1]}')
        przebieg_rozgrywki += f'\tGracz1 wylosował kartę {gracz1[i][1]} a Gracz2 wylosował kartę {gracz2[i][1]}\n'
        if gracz1[i][0] > gracz2[i][0]:
            print('\tZwycięża gracz1')
            przebieg_rozgrywki += '\tZwycięża gracz1\n'
            zwyciezca = 'gracz1'
            licznik_bitew += 1
            return licznik_bitew, zwyciezca, przebieg_rozgrywki
        elif gracz1[i][0] < gracz2[i][0]:
            print('\tZwycięża gracz2')
            przebieg_rozgrywki += '\tZwycięża gracz2\n'
            zwyciezca = 'gracz2'
            licznik_bitew += 1
            return licznik_bitew, zwyciezca, przebieg_rozgrywki
        else:
            print('\tREMIS')
            przebieg_rozgrywki += '\tREMIS\n'
            licznik_bitew += 1
    print('\tNiemożliwe stało się możliwe, gracze mieli TAKIE SAME TALIE')
    przebieg_rozgrywki += '\tNiemożliwe stało się możliwe, gracze mieli TAKIE SAME TALIE\n'
    zwyciezca = 'REMIS'
    return licznik_bitew, zwyciezca, przebieg_rozgrywki


def tryb_do_odrzuconych(gracz1, gracz2):
    przebieg_rozgrywki = ''
    przebieg_wojna = ''
    licznik_gracz1 = 0
    licznik_gracz2 = 0
    licznik_bitew = 0
    for i in range(len(gracz1)):
        print(f'Gracz1 wylosował kartę {gracz1[i][1]} a Gracz2 wylosował kartę {gracz2[i][1]}')
        przebieg_rozgrywki += f'Gracz1 wylosował kartę {gracz1[i][1]} a Gracz2 wylosował kartę {gracz2[i][1]}\n'
        if gracz1[i][0] > gracz2[i][0]:
            print('Zwycięża gracz1')
            przebieg_rozgrywki += 'Zwycięża gracz1\n'
            licznik_gracz1 += 1
            licznik_bitew = 0
        elif gracz1[i][0] < gracz2[i][0]:
            print('Zwycięża gracz2')
            przebieg_rozgrywki += 'Zwycięża gracz2\n'
            licznik_gracz2 += 1
            licznik_bitew = 0
        else:
            print('Mamy REMIS')
            przebieg_rozgrywki += 'Mamy REMIS\n'
            licznik_bitew, zwyciezca_bitwy, przebieg_wojna = wojna_do_odrzuconych(gracz1, gracz2, i)
            przebieg_rozgrywki += przebieg_wojna
            if zwyciezca_bitwy == 'gracz1':
                licznik_gracz1 += 1
            elif zwyciezca_bitwy == 'gracz2':
                licznik_gracz2 += 1
            elif zwyciezca_bitwy == 'REMIS':
                wygrany = 'REMIS'
                return wygrany
        i += licznik_bitew
        if i == len(gracz1):
            break
        input('Nacisnij ENTER, aby kontynuować rozgrywke \n')
    if licznik_gracz1 > licznik_gracz2:
        wygrany = 'gracz1'
    elif licznik_gracz1 < licznik_gracz2:
        wygrany = 'gracz2'
    else:
        wygrany = 'REMIS'
    return wygrany, przebieg_rozgrywki