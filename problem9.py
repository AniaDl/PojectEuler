# find a Pythagorean triplet for which a + b + c = 1000
# a < b < c
# then find product abc

def main():
    a = 3
    b = 4
    c = 5
    while a + b + c <= 1001:
        while a + b + c <= 1001: 
            while a + b + c <= 1001:
                # firstly c is increased by 1 until a + b + c <= 1000
                c += 1
                if a + b + c == 1000:
                    if a**2 + b**2 == c**2:
                        print(a*b*c)
                        break
            # secondly b is increased by 1
            b += 1  
            c = b
        # thirdly a is increased by 1
        a += 1
        b = a
        b += 1  
        c = b


if __name__ == "__main__":
    main()
