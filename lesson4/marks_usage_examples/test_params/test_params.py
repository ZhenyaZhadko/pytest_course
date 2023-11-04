import pytest

@pytest.mark.parametrize("input, expected_output", [(5, 6), (7, 8), (99, 100)])
def test_add_one(input, expected_output):
    result = input + 1
    assert result == expected_output
