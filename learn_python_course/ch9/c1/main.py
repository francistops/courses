def get_odds_and_evens(numbers):
    num_odds = 0
    num_evens = 0

    # Don't touch above this line

    for num in numbers:
        if num % 2 == 0:
            num_evens += 1
        elif num % 2 >= 1:
            num_odds += 1
        else:
            print('ERROR')
    return num_odds, num_evens
