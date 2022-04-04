import math
def bisekcja(f = lambda x: x+math.exp(x), dokladnosc=0.01, lewy_koniec=-1, prawy_koniec=0, miejsc_po_przecinku=3):
    if f(lewy_koniec) * f(prawy_koniec) > 0:
        print('Brak miejsc zerowych na przedziale.')
        return False
    elif f(lewy_koniec) > 0 and f(prawy_koniec) < 0:
        ostatnia_dodatnia = lewy_koniec
        ostatnia_ujemna = prawy_koniec
    elif f(lewy_koniec) < 0 and f(prawy_koniec) > 0:
        ostatnia_dodatnia = prawy_koniec
        ostatnia_ujemna = lewy_koniec
    else:
        print('Jednym z zer jest granica przedziału.')
        return False

    x_srodek = round((ostatnia_ujemna+ostatnia_dodatnia)/2,miejsc_po_przecinku)

    while abs(ostatnia_ujemna-ostatnia_dodatnia) > dokladnosc:
        if f(x_srodek) > 0:
            ostatnia_dodatnia = x_srodek
            print((f'Nowy przedział to {sorted([ostatnia_ujemna, ostatnia_dodatnia])}\n'))
            x_srodek = round((ostatnia_ujemna + ostatnia_dodatnia) / 2, miejsc_po_przecinku)
        elif f(x_srodek) < 0:
            ostatnia_ujemna = x_srodek
            print((f'Nowy przedział to {sorted([ostatnia_ujemna, ostatnia_dodatnia])}\n'))
            x_srodek = round((ostatnia_ujemna + ostatnia_dodatnia) / 2, miejsc_po_przecinku)
        else:
            print(f'Miejsce zerowe to {x_srodek}\n')
            break

    print(f'Poszukiwany pierwiastek to {x_srodek}')

bisekcja()

bisekcja(f=lambda x: x, lewy_koniec=-1, prawy_koniec=1)