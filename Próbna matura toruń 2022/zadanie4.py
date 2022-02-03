from pprint import pprint

file = open('wykreslanka.txt', 'r')
wyniki = open('zadanie4.txt', 'w')

wiersze = file.readlines()
wykreslanka = [wiersz.strip() for wiersz in wiersze]

#ZADANIE 4.1
SZUKANE_SLOWO = 'matura'
DL_SLOWA = len(SZUKANE_SLOWO)

def czy_w_wierszu(wiersz):
    for i in range(200 - DL_SLOWA + 1):
        if wykreslanka[wiersz][i:DL_SLOWA+i] == SZUKANE_SLOWO:
            return True
    return False

def czy_w_kolumnie(kolumna):
    for wiersz in range(100 - DL_SLOWA + 1):
        slowo = ''
        for i in range(DL_SLOWA):
            slowo += wykreslanka[i+wiersz][kolumna]
        if slowo == SZUKANE_SLOWO:
            return True
    return False

slowo_w_wierszu = []
slowo_w_kolumnie = []
for i in range(100):
    if czy_w_wierszu(i):
        slowo_w_wierszu += [i+1]
for i in range(200):
    if czy_w_kolumnie(i):
        slowo_w_kolumnie += [i+1]
# print(slowo_w_kolumnie, slowo_w_wierszu)
wyniki.write(f'ZADANIE 4.1\nwiersze: {slowo_w_wierszu}\nkolumny: {slowo_w_kolumnie}\n\n')

#ZADANIE 4.2
wyniki.write('ZADANIE 4.2\n')
max_litera = ''
wiersz_dlCiagu = {i: 0 for i in range(100)}
the_max_dlugosc_ciagu = 0
wiersze_z_najdluzszym_ciagiem = []
#okreslanie maksymalnych wartosci w kazdym wierszu
for wiersz in range(100):
    dl_ciagu = 1
    max_dl_ciagu = 0
    for litera in range(199):
        aktualna_litera = wykreslanka[wiersz][litera]
        nastepna_litera = wykreslanka[wiersz][litera+1]
        if aktualna_litera == nastepna_litera:
            dl_ciagu += 1
        if dl_ciagu > max_dl_ciagu:
            max_dl_ciagu = dl_ciagu
        if aktualna_litera != nastepna_litera:
            dl_ciagu = 1
    if max_dl_ciagu >= the_max_dlugosc_ciagu:
        wiersze_z_najdluzszym_ciagiem.append(wiersz + 1)
        if max_dl_ciagu > the_max_dlugosc_ciagu:
            wiersze_z_najdluzszym_ciagiem.clear()
            wiersze_z_najdluzszym_ciagiem.append(wiersz + 1)
            the_max_dlugosc_ciagu = max_dl_ciagu

wyniki.write(f'wiersze z najdluzszym ciagiem: {wiersze_z_najdluzszym_ciagiem}\n'
             f'dlugosc ciagu: {the_max_dlugosc_ciagu}\n\n')

#ZADANIE 4.3
def dlugosc_setu_w_wierszu(wiersz, kolumna):
    tablica_liter.clear()
    tablica_liter.append(wykreslanka[wiersz][kolumna])
    dlugosc = 1
    kolumna += 1
    while kolumna < 199:
        if wykreslanka[wiersz][kolumna] not in tablica_liter:
            tablica_liter.append(wykreslanka[wiersz][kolumna])
            dlugosc += 1
            kolumna += 1
        else: break
        if dlugosc == 26:
            break
    return dlugosc

def wysokosc_setu_w_kolumnie(wiersz, kolumna):
    wysokosc = 1
    wiersz += 1
    while wiersz < 99:
        if czy_rozne_litery_na_dlugosci(wiersz, kolumna, dlugosc):
            wysokosc += 1
            wiersz += 1
        else: break
    return wysokosc

def czy_rozne_litery_na_dlugosci(wiersz, kolumna, dlugosc):
    for i in range(dlugosc):
        if wykreslanka[wiersz][kolumna+i] not in tablica_liter:
            tablica_liter.append(wykreslanka[wiersz][kolumna+i])
        else: return False
    return True

tablica_liter = []
max_wymiary = 0
for wiersz in range(100):
    for kolumna in range(200):
        dlugosc = dlugosc_setu_w_wierszu(wiersz, kolumna)
        wysokosc = wysokosc_setu_w_kolumnie(wiersz, kolumna)
        pierwsza_komorka = (wiersz, kolumna)
        if dlugosc*wysokosc > max_wymiary:
            max_wymiary = dlugosc*wysokosc
            max_dlugosc = dlugosc
            max_wysokosc = wysokosc
            max_pierwsza_komorka = pierwsza_komorka

# print(max_pierwsza_komorka, max_dlugosc, max_wysokosc)
wyniki.write(f'ZADANIE 4.3\n'
             f'wysokosc: {max_wysokosc}\n'
             f'szerokosc: {max_dlugosc}\n'
             f'wspolrzedne lewego gornego rogu: {max_pierwsza_komorka}')





