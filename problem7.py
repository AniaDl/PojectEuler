# What is the 10 001st prime number?
from is_prime import is_prime

def main():
    check_is_prime = 1
    next_prime_number = 0
    while True:
        check_is_prime = check_is_prime + 1
        # def is_prime
        if is_prime(check_is_prime) == True:
            next_prime_number = next_prime_number + 1
        if next_prime_number == 10001:
            print('The 10001 st prime number is: %s' %check_is_prime)
            break

if __name__ == "__main__":
    main()
