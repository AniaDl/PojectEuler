import math
from is_prime import is_prime

# find the largest prime factor
def main():
    number = 600851475143 
    
    back = math.floor(number**0.5)
    if number <= 1:
        print("The number have not got the prime number.")
    elif number == 2:
        print('The highest prime number is %s.' %number )
    while back >= 2:
        if number % back == 0: # check if the number can be divided without the rest
            if is_prime(back) == True: # check if the number is the prime factor
                print('The highest prime number is %s' %back)
                break
        back = back - 1


if __name__ == "__main__":
    main()
