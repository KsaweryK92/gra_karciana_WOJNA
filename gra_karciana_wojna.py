from tryb_do_reki import tryb_do_reki
from tryb_do_odrzuconych import tryb_do_odrzuconych
from rozdaj_karty import rozdaj_karty, utworz_graczy, tryb_rozgrywki, opis_kart
from zapis_do_pliku import zapis_do_pliku, nazwa_pliku


przebieg_rozgrywki = ''
przebieg_rozgrywki_tryb_do_odrzuconych = ''
przebieg_rozgrywki_tryb_do_reki = ''


def info_o_rozgrywce():
    tekst = '''
    Talia kart(ilość kart w rozgrywce podasz sam) zostanie potasowana i rozdana między ciebie a komputerowego 
    gracza. Podczas każdej tury wykładacie po jednej karcie z wierzchu talii i ta z większym numerem(silniejsza 
    karta w talii) wygrywa. W przypadku remisu dobieracie po jeszcze jednej karcie i więsza wygrywa, w przeciwnym 
    wypadku wykładacie karty tak długo, aż ktoś zwycięży w pojedynku. Zwycięzcą całej rozgrywki jest gracz z
    większą liczbą zwycięstw pojedyńczych pojedynków(pojedynki wynikające z remisu liczą się jako 1 zwycięstwo.
    '''
    print(tekst)


if __name__ == '__main__':
    while True:
        ilosc_kart = int(input('Iloma kartami chcesz grać - posiadać na ręce(MAX 26): '))
        if ilosc_kart < 27:
            break
        print('Maksymalnie możesz mieć na ręce 26 kart!')

    karty1, karty2 = rozdaj_karty(ilosc_kart)

    info_o_rozgrywce()

    tryb = tryb_rozgrywki()

    gracz1, gracz2 = utworz_graczy(karty1, karty2, opis_kart)

    przebieg_rozgrywki += 'Gracz1 otrzymał następujący zestaw kart:\n'
    for item in gracz1.talia_kart:
        przebieg_rozgrywki += item[1] + ', '
    przebieg_rozgrywki += '\n'
    przebieg_rozgrywki += 'Gracz2 otrzymał następujący zestaw kart:\n'
    for item in gracz2.talia_kart:
        przebieg_rozgrywki += item[1] + ', '
    przebieg_rozgrywki += '\n'

    if not tryb:
        zwyciezca, przebieg_rozgrywki_tryb_do_odrzuconych = tryb_do_odrzuconych(gracz1.talia_kart, gracz2.talia_kart)
        przebieg_rozgrywki += przebieg_rozgrywki_tryb_do_odrzuconych
        print('THE WINNER is: ')
        przebieg_rozgrywki += 'THE WINNER is: \n'
        print(zwyciezca)
        przebieg_rozgrywki += zwyciezca
    elif tryb:
        zwyciezca, przebieg_rozgrywki_tryb_do_reki = tryb_do_reki(gracz1.talia_kart, gracz2.talia_kart)
        przebieg_rozgrywki += przebieg_rozgrywki_tryb_do_reki
        przebieg_rozgrywki += 'THE WINNER is: \n'
        print(zwyciezca)
        przebieg_rozgrywki += zwyciezca
    plik_z_rozgrywka = nazwa_pliku()
    zapis_do_pliku(plik_z_rozgrywka, przebieg_rozgrywki)