
def suma_fibonacci(liczba):

    krok1 = 1 
    krok2 = 2
    krok3 = 0
    suma_ciagu = 2
    while True:
        #obliczenie kolejnego elementu ciągu fibonacciego
        krok3 = krok2 + krok1
        if krok3 >= liczba:
            break
        krok1 = krok2
        krok2 = krok3

        # obliczenie sumy parzystych elementów ciągu fibonacciego
        if krok3 % 2 == 0:
            suma_ciagu = suma_ciagu + krok3

    return(suma_ciagu)


def main():
    max = 4000000
    print(suma_fibonacci(max))


if __name__ == "__main__":
    main()
