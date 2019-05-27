import datetime

import pytest

from dayu_widgets import utils


class MyHasNameObject(object):
    def __init__(self, name, age):
        super(MyHasNameObject, self).__init__()
        self.name = name
        self.age = age


class MyHasCodeObject(object):
    def __init__(self, name, age):
        super(MyHasCodeObject, self).__init__()
        self.name = name
        self.age = age


class MyHasNameAndCodeObject(object):
    def __init__(self, name, code, age):
        super(MyHasNameAndCodeObject, self).__init__()
        self.name = name
        self.code = code
        self.age = age


class MyNoNameAndCodeObject(object):
    def __init__(self):
        super(MyNoNameAndCodeObject, self).__init__()

    def __str__(self):
        return 'MyNoNameAndCodeObject()'


@pytest.mark.parametrize('input_value, result', (
        ({'name': 'Jim', 'age': 18}, 'Jim'),
        ({'code': 'pl_0010', 'id': 111}, 'pl_0010'),
        ({'id': 111, 'age': 18}, "{'age': 18, 'id': 111}"),
        ('test', 'test'),
        (u'test', u'test'),
        (None, '--'),
        (MyHasNameObject('Jim', 18), 'Jim'),
        (MyHasCodeObject('pl_0010', 18), 'pl_0010'),
        (MyHasNameAndCodeObject('Jim', 'pl_0010', 18), 'Jim'),
        (MyNoNameAndCodeObject(), 'MyNoNameAndCodeObject()'),
        (datetime.datetime(2019, 1, 1), '2019-01-01 00:00:00'),
        (20, '20'),
        (20.051, '20.05'),
        (20.058, '20.06'),
))
def test_utils_default_formatter(input_value, result):
    assert utils.default_formatter(input_value) == result
