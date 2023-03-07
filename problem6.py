#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#The list of numbers 1 to 100
to_100 = list(range(1,100+1))

#The sum of the squares of the first hundred natural numbers is:
the_sum_of_squares = sum([next_squares**2 for next_squares in to_100])
#print(the_sum_of_squares)

#The square of the sum of the first ten natural numbers is:
the_square_of_sum = sum([next_number for next_number in to_100])**2
#print(the_square_of_sum)

#the difference between the sum of the squares of the first hundred natural numbers and the square of the sum is:
difference = the_square_of_sum - the_sum_of_squares
print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is: %s " %difference)

   