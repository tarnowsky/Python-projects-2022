file = open('festyn.txt', 'r')
wyniki = open('zadanie4.txt', 'w')
wiersze = file.readlines()
wiersze = [wiersz.strip() for wiersz in wiersze]

def czy_zestrzelona(widocznosc, sekunda_strzalu):
    widoczna_od = widocznosc[0]
    widoczna_przez = widocznosc[1]
    widoczna_do = widoczna_od + widoczna_przez - 1
    if widoczna_od <= sekunda_strzalu <= widoczna_do:
        return True
    return False

sekunda_widocznosc_tab = []
momentyStrzalu = []
index = 0
while index < len(wiersze):
    liczba_tarcz = int(wiersze[index])
    sekunda_widocznosc_tab.append([[int(y) for y in x.split()] for x in wiersze[index + 1:index + liczba_tarcz + 1]])
    index += liczba_tarcz + 1
    liczba_strzalow = int(wiersze[index])
    momentyStrzalu.append([int(x) for x in wiersze[index + 1:index + liczba_strzalow + 1]])
    index += liczba_strzalow + 1

#zadanie 1
wyniki.write('ZADANIE 4.1.\n')
for nr_zestawu in range(3):
    wynik = 0
    zestrzelone_tablice = []
    for sekunda_strzal in momentyStrzalu[nr_zestawu]:
        for widocznosc_tarczy in sekunda_widocznosc_tab[nr_zestawu]:
            if czy_zestrzelona(widocznosc_tarczy, sekunda_strzal) and widocznosc_tarczy not in zestrzelone_tablice:
                wynik += 1
                zestrzelone_tablice.append(widocznosc_tarczy)
    wyniki.write(f'zestaw {nr_zestawu + 1}: {wynik}\n')


#zadanie 2
wyniki.write('\nZADANIE 4.2.\n')
for nr_zestawu in range(3):
    max_widocznosc = 0
    for sekunda in sekunda_widocznosc_tab[nr_zestawu]:
        widocznosc = sekunda[1]
        max_widocznosc = max(max_widocznosc, widocznosc)
    wyniki.write(f'zestaw {nr_zestawu + 1}: {max_widocznosc}\n')

#zadanie 3
wyniki.write('\nZADANIE 4.3.\n')
for nr_zestawu in range(3):
    max_liczba_zestrzelonych_tarcz = 0
    for sekunda_strzal in range(1, 300 + 1):
        liczba_zestrzelonych_tarcz = 0
        for widocznosc_tarczy in sekunda_widocznosc_tab[nr_zestawu]:
            if czy_zestrzelona(widocznosc_tarczy, sekunda_strzal):
                liczba_zestrzelonych_tarcz += 1
        if liczba_zestrzelonych_tarcz > max_liczba_zestrzelonych_tarcz:
            optymalna_sekunda_strzalu = sekunda_strzal
            max_liczba_zestrzelonych_tarcz = liczba_zestrzelonych_tarcz
    wyniki.write(f'zestaw {nr_zestawu + 1}: {optymalna_sekunda_strzalu}\n')

#zadanie 4
wyniki.write('\nZADANIE 4.4.\n')
for nr_zestawu in range(3):
    wynik = 0
    for sekunda_strzal in momentyStrzalu[nr_zestawu]:
        for sekunda in sekunda_widocznosc_tab[nr_zestawu]:
            if sekunda[0] <= sekunda_strzal <= sekunda[0] + sekunda[1] - 1:
                wynik += 1
    wyniki.write(f'zestaw {nr_zestawu + 1}: {wynik}\n')

