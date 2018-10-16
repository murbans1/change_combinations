def get_ways(amount, coins):
    ways = []
    for i in range(amount + 1):
        ways.append([])
    ways[0].append([])

    for coin in coins:
        for calc_amount in range(coin, amount + 1):
            rest = calc_amount - coin
            for way in ways[rest]:
                ways[calc_amount].append([coin] + way)

    return ways[amount]

