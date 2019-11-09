from datetime import datetime

def nazwa_pliku():
    data_dzis = datetime.today()
    data_dzis = str(data_dzis.date())

    data_dzis += '-'

    nazwa = input('Podaj nazwe pliku: ')
    nazwa = data_dzis + nazwa + '.txt'
    return nazwa


def zapis_do_pliku(nazwa_pliku, dane_do_zapisu):
    plik_do_zapisu = open(nazwa_pliku, 'a')
    plik_do_zapisu.write(dane_do_zapisu)
    plik_do_zapisu.close()
    return

