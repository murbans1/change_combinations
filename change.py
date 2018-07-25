DENOMINATIONS = [1, 0.25, 0.10, 0.05, 0.01]


def calculate_changes(n, coins=DENOMINATIONS):
    combinations = change_combinations(n, coins)
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


def change_combinations(n, coins):
    permutations = _change_permutations(n, coins)
    sorted_permutations = [sorted(x) for x in permutations]
    distinct_combinations = list(set(tuple(x) for x in sorted_permutations))
    combinations = [list(x) for x in distinct_combinations]
    return combinations


def _change_permutations(n, coins):
    if n < 0:
        return []
    if n == 0:
         return [[]]
    all_changes = []

    for last_used_coin in coins:
        combos = _change_permutations(n - last_used_coin, coins)
        for combo in combos:
            combo.append(last_used_coin)
            all_changes.append(combo)

    return all_changes
