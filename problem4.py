import math

def how_many_digit(number):
    # the function check how many digits have the number
    times = 0
    quotient = number
    while True:
        
        if quotient >= 1:
            times = times + 1
            quotient = quotient / 10
        elif quotient < 1 and quotient >= 0: 
            return times
        else:
            print('The number is negative')
            break


def if_palindrome(number):
    # the function chcec if the given number is palindrome

    num_digit = how_many_digit(number)
    half = math.floor(num_digit/2)
    l0 = []

    if num_digit == 1:
        return False

    while num_digit > 1:
        # the loop create the list with consecutive digits of a number
        l = math.floor(number / 10**(num_digit-1))
        l0.append(l)
        number = number - l*10**(num_digit-1)
        num_digit = num_digit - 1
    l0.append(number)

    for i in range(half):
        # the loop chcek numbers in the l0-list if are like a palindrome 
        if l0[i] != l0[-1-i]:
            return False

    return True


def main():
  
    x_list = list(range(100, 999))
    y_list = x_list
    palindrome_list = []

    # double loop create a product of two 3-digit numbers, and then check that this product is the palindrome
    for x in x_list:
        for y in y_list:
            product_x_y = y*x
            if if_palindrome(product_x_y) == True:
                palindrome_list.append(product_x_y)

    max_palindrom = max(palindrome_list)
    print('The largest palindrome made from the product of two 3-digit numbers is %s' %max_palindrom)


if __name__ == "__main__":
    main()
