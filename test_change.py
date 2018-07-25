import pytest

from change import (
    calculate_changes,
    change_combinations,
)


@pytest.mark.parametrize("coins,test_value,expected", [
    ([2, 5, 3, 6], 10, [[5, 5], [2, 3, 5], [2, 2, 3, 3], [2, 2, 2, 2, 2], [2, 2, 6]]),
])
def test_change_combinations(coins, test_value, expected):
    assert change_combinations(test_value, coins) == expected


@pytest.mark.parametrize("coins,test_value,expected", [
    ([2, 5, 3, 6], 10, [[0, 0, 2, 0], [1, 1, 1, 0], [2, 2, 0, 0], [5, 0, 0, 0], [2, 0, 0, 1]]),
])
def test_calculate_changes(coins, test_value, expected):
    assert calculate_changes(test_value, coins=coins) == expected
