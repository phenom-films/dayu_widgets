"""
Test overflow_format.
"""
# Import third-party modules
import pytest

# Import local modules
from dayu_widgets import utils


@pytest.mark.parametrize(
    "num, overflow, result",
    (
        (0, 99, "0"),
        (100, 99, "99+"),
        (20, 99, "20"),
        (20, 50, "20"),
        (-1, 50, "-1"),
        (99, 50, "50+"),
    ),
)
def test_overflow_format(num, overflow, result):
    """Test overflow_format with normal arg."""
    assert utils.overflow_format(num, overflow) == result


@pytest.mark.parametrize(
    "num, overflow, error_type",
    ((0.0, 99, float), (20.0, 99.0, float), ("20", 50, str), (None, 50, type(None))),
)
def test_with_wrong_num_type(num, overflow, error_type):
    """Test overflow_format with wrong"""
    with pytest.raises(ValueError) as exc_info:
        utils.overflow_format(num, overflow)

    exception_msg = exc_info.value.args[0]
    assert (
        exception_msg == "Input argument 'num' should be int type, "
        "but get {}".format(error_type)
    )


@pytest.mark.parametrize(
    "num, overflow, error_type",
    (
        (100, 99.0, float),
        (10, "99", str),
        (0, None, type(None)),
    ),
)
def test_with_wrong_overflow_type(num, overflow, error_type):
    """Test overflow_format with wrong"""
    with pytest.raises(ValueError) as exc_info:
        utils.overflow_format(num, overflow)

    exception_msg = exc_info.value.args[0]
    assert (
        exception_msg == "Input argument 'overflow' should be int type, "
        "but get {}".format(error_type)
    )
