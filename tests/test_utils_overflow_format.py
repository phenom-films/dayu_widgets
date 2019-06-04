from dayu_widgets import utils
import pytest


@pytest.mark.parametrize('num, overflow, result', (
        (0, 99, '0'),
        (100, 99, '99+'),
        (20, 99, '20'),
        (20, 50, '20'),
        (-1, 50, '-1'),
        (99, 50, '50+'),
))
def test_overflow_format(num, overflow, result):
    assert utils.overflow_format(num, overflow) == result


@pytest.mark.parametrize('num, overflow, arg, error_type', (
        (0.0, 99, 'num', 'float'),
        (100, 99.0, 'overflow', 'float'),
        (20.0, 99.0, 'num', 'float'),
        ('20', 50, 'num', 'str'),
        (None, 50, 'num', 'NoneType')
))
def test_overflow_format_with_wrong_type(num, overflow, arg, error_type):
    with pytest.raises(ValueError) as exc_info:
        utils.overflow_format(num, overflow)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Input argument '{}' should be int type, but get <type '{}'>".format(arg, error_type)
