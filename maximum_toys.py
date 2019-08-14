

def maximum_toys(prices, spending_money):
    num_toys = 0
    prices.sort()
    for price in prices:
        if spending_money - price >= 0:
            spending_money -= price
            num_toys += 1
    return num_toys


prices = [1, 2, 3, 4]
k = 7

print(maximum_toys(prices, k))
