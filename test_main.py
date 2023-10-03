"""Module for testing the main file."""


import pytest

from main import get_degree

test_data = (
    ((100, 2400, 600, 4), 73.79),
    ((0, 0, 0), 0),
    ((10, 20, 30, 40), 153.8),
)


@pytest.mark.parametrize('args, expected', test_data)
def test_get_degree(args, expected) -> None:
    """Check if the counts degrees well or not.

    Args:
        args (_type_): _description_
        expected (_type_): The right answer we should receive.
    """
    assert get_degree(*args) == expected
