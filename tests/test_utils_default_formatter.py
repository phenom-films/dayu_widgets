import datetime

import pytest

from dayu_widgets import utils


class MyHasNameObject(object):
    def __init__(self, name, age):
        super(MyHasNameObject, self).__init__()
        self.name = name
        self.age = age


class MyHasCodeObject(object):
    def __init__(self, code, age):
        super(MyHasCodeObject, self).__init__()
        self.code = code
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
        ([{'name': 'Jim', 'age': 18}, {'name': 'Tom', 'age': 16}], 'Jim,Tom'),
        ({'code': 'pl_0010', 'id': 111}, 'pl_0010'),
        ([{'code': 'pl_0010', 'id': 111}, {'code': 'pl_0020', 'id': 112}], 'pl_0010,pl_0020'),
        ({'id': 111, 'age': 18}, "{'age': 18, 'id': 111}"),
        ([{'id': 111, 'age': 18}, {'id': 112, 'age': 19}], "{'age': 18, 'id': 111},{'age': 19, 'id': 112}"),
        ('test', 'test'),
        (['test', 'test2'], 'test,test2'),
        (u'test', u'test'),
        ([u'test', 'test2'], 'test,test2'),
        (None, '--'),
        ([None, 'hello'], '--,hello'),
        (MyHasNameObject('Jim', 18), 'Jim'),
        ([MyHasNameObject('Jim', 18), MyHasNameObject('Tom', 19)], 'Jim,Tom'),
        (MyHasCodeObject('pl_0010', 18), 'pl_0010'),
        (MyHasNameAndCodeObject('Jim', 'pl_0010', 18), 'Jim'),
        (MyNoNameAndCodeObject(), 'MyNoNameAndCodeObject()'),
        (datetime.datetime(2019, 1, 1), '2019-01-01 00:00:00'),
        (20, '20'),
        (20.051, '20.05'),
        (20.058, '20.06'),
        ([20, 20.058], '20,20.06'),
        (set(), 'set([])'),
))
def test_utils_default_formatter(input_value, result):
    assert utils.default_formatter(input_value) == result
