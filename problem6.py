# find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def enter_the_number():
    number = int(input('Please enter the number ')) #the task assumes that it is 100
    return number

def main():
    # the list of numbers 1 to enter number
    to_100 = list(range(1,enter_the_number()+1))

    # the sum of the squares of the first hundred natural numbers is:
    the_sum_of_squares = sum([next_squares**2 for next_squares in to_100])

    # the square of the sum of the first ten natural numbers is:
    the_square_of_sum = sum([next_number for next_number in to_100])**2

    # the difference between the sum of the squares of the first hundred natural numbers and the square of the sum is:
    difference = the_square_of_sum - the_sum_of_squares
    print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is: %s " %difference)


if __name__ == "__main__":
    main()
