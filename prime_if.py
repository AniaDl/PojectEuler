def prime_if(max_number):
# prime factors
    i = 0
    for divider in range(2, max_number):
        if max_number % divider == 0:
            i = i + 1
        else:
            continue

    if i > 0:
        return False
    elif i == 0:
        return True
