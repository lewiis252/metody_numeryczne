import math

def metoda_stycznych(f = lambda x: x**4-2*x-4, f_prim = lambda x: 4*x**3-2, dokladnosc=0.01, lewy_koniec=0, prawy_koniec=1.7, miejsc_po_przecinku = 4):
    '''Oblicza przybliżone miejsce zerowe funkcji na zadanym przedziale metodą stycznych'''

    if f(lewy_koniec) * f(prawy_koniec) > 0:
        print('Brak miejsc zerowych na przedziale.')
        return False
    elif f(lewy_koniec) == 0 or f(prawy_koniec) == 0:
        print('Jednym z pierwiastków jest granica przedziału.')
    else:
        x_0 = prawy_koniec

        x = [x_0]
        index = 1
        while abs(round(f(x[index-1]), miejsc_po_przecinku)) > dokladnosc:
            print(f'x_{index-1} = {x[index-1]}')
            print(f'f(x_{index-1}) = {round(f(x[index-1]), miejsc_po_przecinku)}\n')
            x_new = round(x[index-1] - f(x[index-1])/f_prim(x[index-1]),miejsc_po_przecinku)
            x.append(x_new)
            index = index + 1


        print(f'x_{index - 1} = {x[index - 1]}')
        print(f'f(x_{index - 1}) = {round(f(x[index-1]), miejsc_po_przecinku)}')
        print(f'Lista przybliżeń: {x}')

metoda_stycznych(f=lambda x: x**2-1, lewy_koniec=0, prawy_koniec=2)