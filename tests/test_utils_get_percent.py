"""
Test get_percent.
"""
# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from dayu_widgets import utils
import pytest


@pytest.mark.parametrize(
    "value, mini, maxi, result",
    (
        (0, 0, 100, 0),
        (100, 0, 100, 100),
        (1, 0, 100, 1),
        (99, 0, 100, 99),
        (-1, 0, 100, 0),
        (101, 0, 100, 100),
        (101, 10, 110, 91),
        (10, 100, 100, 100),
    ),
)
def test_get_percent(value, mini, maxi, result):
    """Test get_percent with normal arg."""
    assert utils.get_percent(value, mini, maxi) == result
