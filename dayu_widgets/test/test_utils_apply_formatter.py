"""Test utils.apply_formatter function."""
import pytest

from dayu_widgets import utils


def callable_for_test(*args, **kwargs):
    """A helper function for test when formatter is a complex callback function."""
    return "{};{}".format(
        ";".join([str(i) for i in args]),
        ";".join(["{}:{}".format(k, v) for k, v in kwargs.items()]),
    )


COLOR_CONFIG_DICT = {"error": "#f00", "ok": "#0f0", "warning": "#ff0"}


@pytest.mark.parametrize(
    "formatter,result,args,kwargs",
    (
        (None, "xiaoming", ("xiaoming",), {"age": 19}),
        (COLOR_CONFIG_DICT, "#f00", ("error",), {}),
        (COLOR_CONFIG_DICT, "#f00", ("error", 3), {"age": 19}),
        (COLOR_CONFIG_DICT, "#0f0", ("ok",), {}),
        (COLOR_CONFIG_DICT, "#ff0", ("warning",), {}),
        (COLOR_CONFIG_DICT, None, ("other",), {}),
        (lambda x, y: x + y, 3, (1, 2), {}),
        (lambda x, y: x + y, "helloxiaoming", ("hello", "xiaoming"), {}),
        # (callable_for_test, '1;2;age:18;name:xiaoming', (1, 2), {'name': 'xiaoming', 'age': 18}),
        ("Show Me", "Show Me", ("xiaoming",), {"age": 19}),
        ("Show Me", "Show Me", (1, 2), {"age": 19}),
        (100, 100, ("xiaoming",), {"age": 19}),
        (100, 100, (1, 2), {"age": 19}),
    ),
)
def test_apply_formatter(formatter, result, args, kwargs):
    """Test for apply_formatter with all situation."""
    assert utils.apply_formatter(formatter, *args, **kwargs) == result
