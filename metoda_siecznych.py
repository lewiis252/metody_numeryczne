
def metoda_siecznych(f = lambda x: x**3+x**2-3*x-3 , dokladnosc=0.001, lewy_koniec=1, prawy_koniec=2, miejsc_po_przecinku = 5):
    '''Oblicza przybliżone miejsce zerowe funkcji na zadanym przedziale'''
    if f(lewy_koniec) * f(prawy_koniec) > 0:
        print('Brak miejsc zerowych na przedziale.')
        return False
    else:
        lista_x = []
        x_0 = lewy_koniec
        x_1 = prawy_koniec

        x = round(x_1 - ((x_1 - x_0) * f(x_1)/(f(x_1) - f(x_0))), miejsc_po_przecinku)
        lista_x = [x_0, x_1, x]
        index = 1
        while abs(round(f(x), miejsc_po_przecinku)) > dokladnosc:

            print(f'x_{index} = {x_1}')
            print(f'x_{index-1} = {x_0}')
            print(f'Nowe przybliżenie x = {x}')
            print(f'f(x) = {round(f(x), miejsc_po_przecinku)}\n')
            x_0, x_1 = x_1, x

            index = index+1

            x = round(x_1 - ((x_1 - x_0) * f(x_1)/(f(x_1) - f(x_0))), miejsc_po_przecinku)
            lista_x.append(x)

        print(f'x_{index} = {x_1}')
        print(f'x_{index - 1} = {x_0}')
        print(f'Nowe przybliżenie x = {x}')
        print(f'f(x) = {f(x)}\n')
        print(f'Poszukiwany pierwiastek to {x}')
        print(f'Lista kolejnych x_i: {lista_x} ')



metoda_siecznych()