file = open('liczby.txt', 'r')
wiersze = file.readlines()

def generator_liczb(wiersze):
    for liczba in wiersze:
        liczba = liczba.strip()
        yield liczba

print('ZADANIE 4.1.')
wynik = 0
for liczba in generator_liczb(wiersze):
    liczba = list(liczba)
    suma = 0
    for i in range(len(liczba)):
        suma += int(liczba[i])
    if suma < (len(liczba)/2):
        wynik += 1
print(wynik)

def bin_na_dec(liczba):
    return int(liczba,2)

podzielna_przez_2 = 0
podzielna_przez_8 = 0

print('ZADANIE 4.2.')
for liczba in generator_liczb(wiersze):
    if bin_na_dec(liczba) % 2 == 0:
        podzielna_przez_2 += 1
    if bin_na_dec(liczba) % 8 == 0:
        podzielna_przez_8 += 1
print('Podzielne przez dwa:', podzielna_przez_2)
print('Podzielne przez osiem:', podzielna_przez_8)

print('ZADANIE 4.3.')
max_liczba = 0
min_liczba = 76381731283

max_wiersz = 0
min_wiersz = 0

aktualna = 0
aktualny_wiersz = 1

for liczba in generator_liczb(wiersze):
    aktualna = bin_na_dec(liczba)
    if aktualna < min_liczba:
        min_liczba = aktualna
        min_wiersz = aktualny_wiersz
    if aktualna > max_liczba:
        max_liczba = aktualna
        max_wiersz = aktualny_wiersz
    aktualny_wiersz += 1
print('Wiersz w którym znajduje sie najmniejsza liczba:', min_wiersz)
print('Wiersz w którym znajduje sie największa liczba:', max_wiersz)