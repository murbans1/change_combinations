import pytest

from clean_input import clean_input


@pytest.mark.parametrize("input,expected", [
    ('00.18aaa', '00.18'),
    ('.18aaa', '0.18'),
    ('-0.18aaa', '0.18'),
])
def test_clean_input(input, expected):
    assert clean_input(input) == expected
