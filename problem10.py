# The Sieve of Erastothenes

def get_idx_from_number(number):
    index = (number-3) >> 1
    return index


def get_number_from_index(index):
    number = 2*index + 3
    return number


def SieveOfErastothenes(n):
    n_list = []
    for i in range(3, n, 2):
        n_list.append(True)

    sum = 2
    for j in range(len(n_list)):

        if n_list[j] == False:
            continue

        number = get_number_from_index(j) # get numb from idx

        for k in range(number**2, n, number):
            n_list[get_idx_from_number(k)] = False # get idx from numb

        if n_list[j] == True:
            sum += number # get number from idx

    return sum


def main():
    print(SieveOfErastothenes(2000000))


if __name__ == "__main__":
    main()
