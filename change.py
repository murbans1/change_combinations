DENOMINATIONS = [1, 0.25, 0.10, 0.05, 0.01]


def calculate_changes(amount, coins=DENOMINATIONS):
    combinations = change_combinations(amount, coins)
    results = []
    for combination in combinations:
        results.append(parse_result(combination, coins))
    return results


def parse_result(combination, coins):
    results = dict()
    for c in coins:
        results[c] = 0
    for comb in combination:
        results[comb] += 1
    return results.values()


def change_combinations(amount, coins):
    results = []
    for s in change_money(amount, coins, []):
        results.append(s)
    return results


def change_money(amount, coins, money_used):
    if sum(money_used) == amount:
        yield money_used
    elif sum(money_used) > amount:
        return
    elif not coins:
        return
    else:
        for change in change_money(amount, coins, money_used + [coins[0]]):
            yield change
        for change in change_money(amount, coins[1:], money_used):
            yield change
