# WIP
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number + 1):
        if number % i == 0 and number != i:
            # print("keep searching... 1", number)
            continue
        elif number % i > 0:
            # print("keep searching... 2", number)
            continue
        else:
            # print("prime! 3", number)
            return True
    return False
