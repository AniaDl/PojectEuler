
def wpisz_wartosc():
    #Wpisanie w kolsoli wartości 
    max_sum = int(input('Wpisz do jakiej wartości ma dodawać do siebie wielokrotności 3 i 5:'))
    print("Zostanie dodana wielokroność 3 i 5 do wartości %s." % max_sum)

    return(max_sum)
    

def suma_3i5(max_sum):
    #Utworzenie list
    lista_3 = list(range(3, max_sum, 3))
    lista_5 = list(range(5, max_sum, 5))

    #Utworzenie zbiorów
    zbior_3 =set(lista_3)
    zbior_5 =set(lista_5)

    #Część wspólna
    wspolna_lista = list(zbior_3.intersection(zbior_5))
    #print(wspolna)

    #Suma
    suma_lista_3 = sum(lista_3)
    suma_lista_5 = sum(lista_5)
    suma_wspolna = sum(wspolna_lista)

    suma = suma_lista_3 + suma_lista_5 - suma_wspolna

    return(suma)

def main():
    wartosc = wpisz_wartosc()
    suma = suma_3i5(wartosc)
    print('Suma wielokrotności 3 i 5 do wartości to %s' %suma)

if __name__ == "__main__":
    main()
