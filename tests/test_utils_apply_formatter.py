from dayu_widgets import utils
import pytest


def callable_for_test(*args, **kwargs):
    return '{};{}'.format(';'.join([str(i) for i in args]),
                          ';'.join(['{}:{}'.format(k, v) for k, v in kwargs.items()]))


@pytest.mark.parametrize('formatter,result,args,kwargs', (
        (None, 'xiaoming', ('xiaoming',), {'age': 19}),
        ({'error': '#f00', 'ok': '#0f0', 'warning': '#ff0'}, '#f00', ('error',), {}),
        ({'error': '#f00', 'ok': '#0f0', 'warning': '#ff0'}, '#f00', ('error', 3), {'age': 19}),
        ({'error': '#f00', 'ok': '#0f0', 'warning': '#ff0'}, '#0f0', ('ok',), {}),
        ({'error': '#f00', 'ok': '#0f0', 'warning': '#ff0'}, '#ff0', ('warning',), {}),
        ({'error': '#f00', 'ok': '#0f0', 'warning': '#ff0'}, None, ('other',), {}),
        (lambda x, y: x + y, 3, (1, 2), {}),
        (lambda x, y: x + y, 'helloxiaoming', ('hello', 'xiaoming'), {}),
        (callable_for_test, '1;2;age:18;name:xiaoming', (1, 2), {'name': 'xiaoming', 'age': 18}),
        ('Show Me', 'Show Me', ('xiaoming',), {'age': 19}),
        ('Show Me', 'Show Me', (1, 2), {'age': 19}),
        (100, 100, ('xiaoming',), {'age': 19}),
        (100, 100, (1, 2), {'age': 19}),
))
def test_apply_formatter(formatter, result, args, kwargs):
    print formatter, result, args, kwargs
    assert utils.apply_formatter(formatter, *args, **kwargs) == result
