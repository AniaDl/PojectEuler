#problem5
#the smallest number that can be divided by each of the numbers from 1 to x without any remainder    
import math

def prime_if(max_number):
# prime factors
    i = 0
    for divider in range(2, max_number):
        if max_number % divider == 0:
            i = i + 1
        else:
            continue

    if i > 0:
        return False
    elif i == 0:
        return True


def main():
    #enter the number
    highest_divisor = int(input("Program will calculate the smallest number that can be divided by each of the numbers from 1 to x \
                                without any remainder.\nPlease enter the x: "))


    list_numbers = [next_numbers for next_numbers in range(2, highest_divisor+1)]
    #print("All divisiors: %s" %list_numbers)
    
    #check if number is prime factor 
    list_primes = []
    for next in list_numbers:
        if prime_if(next) == True:
            list_primes.append(next)
    #print("List of primes: %s" %list_primes)

    list_of_all = list_primes

    #powers of prime numbers...
    list_of_powers = []
    square_of_highest_divisor = math.floor(highest_divisor**0.5)
    for numbers in range (2, square_of_highest_divisor+1):
        if prime_if(numbers) == True:
            list_of_powers.append(numbers)
        #delate repeated powers
        if numbers in list_of_all:
            list_of_all.remove(numbers)
    #print("List of powers: %s" %list_of_powers)
    
    #find the result of the highest power 
    list_of_k = []
    for i in list_of_powers:
        power = 2
        k = 1
        while True:
            k = i**power
            if k < highest_divisor:
                list_of_k.append(k)
            else:
                list_of_all.append(max(list_of_k))
                list_of_k = []
                break
            power = power + 1   
    #print("List of result of the powers %s " %list_of_all)

    #result
    product_of_list_of_all = 1
    for i in list_of_all:
        product_of_list_of_all = product_of_list_of_all * i

    print("Result: %s" %product_of_list_of_all)

if __name__ == "__main__":
    main()



