import math

def prime_if(max_number):
# prime factors
    #max_number = 11
    i = 0
    for divider in range(2, math.floor((max_number+1)**0.5)):
        #print(math.floor((max_number+1)**0.5))
        #print(divider)
        if max_number % divider == 0:
            i = i + 1
        else:
            continue

    if i > 0:
        return False
    elif i == 0:
        return True


# find the largest prime factor
def main():
    number = 600851475143 
    
    back = math.floor(number**0.5)
    if number <= 1:
        print("The number have not got the prime number.")
    elif number == 2:
        print('The highest prime number is %s.' %number )
    while back >= 2:
        if number % back == 0: #check if the number can be divided without the rest
            if prime_if(back) == True: #chcek if the number is the prime factor
                print('The highest prime number is %s' %back)
                break
        #print(back)
        back = back - 1 


    
    #prime_T_F = prime_if(number)
    #print(prime_T_F)
    


if __name__ == "__main__":
    main()
