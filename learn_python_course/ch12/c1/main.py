def purchase(price, money_available):
    if price > money_available:
        raise Exception('not enough money')
    else:
        return money_available - price
