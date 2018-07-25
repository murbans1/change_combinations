import pytest

from change import (
    calculate_changes,
    change_combinations,
    INT_DENOMINATIONS,
)


@pytest.mark.parametrize("coins,amount,expected", [
    ([2, 5, 3, 6], 10, [[2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 2, 6], [2, 5, 3], [5, 5]]),
])
def test_change_combinations(coins, amount, expected):
    assert change_combinations(amount, coins) == expected


@pytest.mark.parametrize("coins,amount,expected", [
    ([2, 5, 3, 6], 10, [[5, 0, 0, 0], [2, 2, 0, 0], [2, 0, 0, 1], [1, 1, 1, 0], [0, 0, 2, 0]]),
    (INT_DENOMINATIONS, int(0.14 * 100), [[0, 1, 0, 0, 4], [0, 0, 0, 2, 4], [0, 0, 0, 1, 9], [0, 0, 0, 0, 14]]),
])
def test_calculate_changes(coins, amount, expected):
    assert calculate_changes(amount, coins=coins) == expected
