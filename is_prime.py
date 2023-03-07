import math

def is_prime(max_number):
    """This function checks if a number is prime.
    input: the number what we want to check
    output: return True if the number is prime, false if not
    """

    i = 0
    if max_number == 4 or max_number == 1:
        return False

    for divider in range(2, int(math.sqrt(max_number)) + 1):
        if max_number % divider == 0:
            i = i + 1

    if i > 0:
        return False
    elif i == 0:
        return True
