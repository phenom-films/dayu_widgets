"""
Test get_percent.
"""
import pytest

from dayu_widgets import utils


@pytest.mark.parametrize('value, mini, maxi, result', (
    (0, 0, 100, 0),
    (100, 0, 100, 100),
    (1, 0, 100, 1),
    (99, 0, 100, 99),
    (-1, 0, 100, 0),
    (101, 0, 100, 100),
    (101, 10, 110, 91),
))
def test_get_percent(value, mini, maxi, result):
    """Test get_percent with normal arg."""
    assert utils.get_percent(value, mini, maxi) == result


def test_with_wrong_num_type():
    """Test get_percent with min and max equaled """
    with pytest.raises(ValueError) as exc_info:
        utils.get_percent(20, 10, 10)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "minimum should not be equal to maximum."
