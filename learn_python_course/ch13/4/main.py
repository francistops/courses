def factorial(num):
    total = 1
    if num == 0:
        return 1
    for factor in range(1, num + 1):
        total *= factor
    return total
