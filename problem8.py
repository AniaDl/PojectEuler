# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.

def main():
    long_number = (
    "73167176531330624919225119674426574742355349194934" +
    "96983520312774506326239578318016984801869478851843" +
    "85861560789112949495459501737958331952853208805511" +
    "12540698747158523863050715693290963295227443043557" +
    "66896648950445244523161731856403098711121722383113" +
    "62229893423380308135336276614282806444486645238749" +
    "30358907296290491560440772390713810515859307960866" +
    "70172427121883998797908792274921901699720888093776" +
    "65727333001053367881220235421809751254540594752243" +
    "52584907711670556013604839586446706324415722155397" +
    "53697817977846174064955149290862569321978468622482" +
    "83972241375657056057490261407972968652414535100474" +
    "82166370484403199890008895243450658541227588666881" +
    "16427171479924442928230863465674813919123162824586" +
    "17866458359124566529476545682848912883142607690042" +
    "24219022671055626321111109370544217506941658960408" +
    "07198403850962455444362981230987879927244284909188" +
    "84580156166097919133875499200524063689912560717606" +
    "05886116467109405077541002256983155200055935729725" +
    "71636269561882670428252483600823257530420752963450")

    # index list starting with 9
    nine_list = [ index for index in range(len(long_number)) if long_number.startswith('9', index)]

    product_list = []

    for index_nine in range(len(nine_list)):
        # calculate the next products
        every_product = 9
        i = 1
        j = 1
        quantity = 0

        while True:
            # check witch number is higher on the left or on the right
            quantity = quantity + 1
            if quantity == 13:
                break
            if nine_list[index_nine] - i < 0:
                every_product = every_product * int(long_number[nine_list[index_nine] + j])
            elif nine_list[index_nine] + j >= len(long_number):
                every_product = every_product * int(long_number[nine_list[index_nine] - i])
            elif int(long_number[nine_list[index_nine] - i]) <= int(long_number[nine_list[index_nine] + j]):
                every_product = every_product * int(long_number[nine_list[index_nine] + j])
                j = j + 1
            else:
                every_product = every_product * int(long_number[nine_list[index_nine] - i])
                i = i + 1
        product_list.append(every_product)

    print("The greatest product of the thirteen adjacent digits in the 1000-digit is %s." %max(product_list))


if __name__ == "__main__":
    main()
