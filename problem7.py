#What is the 10 001st prime number?
from prime_if import prime_if

def main():
    check_if_prime = 1
    next_prime_number = 0
    while True:
        check_if_prime = check_if_prime + 1
        #def prime_if
        if prime_if(check_if_prime) == True:
            next_prime_number = next_prime_number + 1
        if next_prime_number == 10001:
            print('The 10001 st prime number is: %s' %check_if_prime)
            break
        #chcek_if_prime = check_if_prime + 1
    
if __name__ == "__main__":
    main()