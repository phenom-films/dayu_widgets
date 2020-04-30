"""
Test the display_formatter icon_formatter font_formatter
"""
import datetime

import pytest

from dayu_widgets import utils
from dayu_widgets.qt import MCacheDict


class _HasNameObject(object):
    def __init__(self, name, age):
        super(_HasNameObject, self).__init__()
        self.name = name
        self.age = age


class _HasCodeObject(object):
    def __init__(self, code, age):
        super(_HasCodeObject, self).__init__()
        self.code = code
        self.age = age


class _HasNameAndCodeObject(object):
    def __init__(self, name, code, age):
        super(_HasNameAndCodeObject, self).__init__()
        self.name = name
        self.code = code
        self.age = age


class _NoNameAndCodeObject(object):
    def __str__(self):
        return 'MyNoNameAndCodeObject()'


class _HasIconObject(object):
    def __init__(self, icon=None):
        super(_HasIconObject, self).__init__()
        self.icon = icon


@pytest.mark.parametrize('input_value, result', (
    ({'name': 'Jim', 'age': 18}, 'Jim'),
    ([{'name': 'Jim', 'age': 18}, {'name': 'Tom', 'age': 16}], 'Jim,Tom'),
    ({'code': 'pl_0010', 'id': 111}, 'pl_0010'),
    ([{'code': 'pl_0010', 'id': 111}, {'code': 'pl_0020', 'id': 112}], 'pl_0010,pl_0020'),
    ({'id': 111, 'age': 18}, "{'age': 18, 'id': 111}"),
    ([{'id': 111, 'age': 18}, {'id': 112, 'age': 19}],
     "{'age': 18, 'id': 111},{'age': 19, 'id': 112}"),
    ('test', 'test'),
    (['test', 'test2'], 'test,test2'),
    (u'test', u'test'),
    ([u'test', 'test2'], 'test,test2'),
    (None, '--'),
    ([None, 'hello'], '--,hello'),
    (_HasNameObject('Jim', 18), 'Jim'),
    ([_HasNameObject('Jim', 18), _HasNameObject('Tom', 19)], 'Jim,Tom'),
    (_HasCodeObject('pl_0010', 18), 'pl_0010'),
    (_HasNameAndCodeObject('Jim', 'pl_0010', 18), 'Jim'),
    (_NoNameAndCodeObject(), 'MyNoNameAndCodeObject()'),
    (datetime.datetime(2019, 1, 1), '2019-01-01 00:00:00'),
    (20, '20'),
    (20.051, '20.05'),
    (20.058, '20.06'),
    ([20, 20.058], '20,20.06'),
    (set(), 'set([])'),
))
def test_utils_default_formatter(input_value, result):
    """Test default_formatter with all kinds of input type"""
    assert utils.display_formatter(input_value) == result


@pytest.mark.parametrize('underline', (True, False))
@pytest.mark.parametrize('bold', (True, False))
def test_font_formatter(underline, bold):
    """Test font_formatter with different arg values"""
    font = utils.font_formatter({'underline': underline, 'bold': bold})
    assert font.underline() == underline
    assert font.bold() == bold


@pytest.mark.parametrize('input_data, result', (
    ({'icon': 'check.svg'}, 'check.svg'),
    ({'icon': 'add_line.svg'}, 'add_line.svg'),
    ({'icon': {'icon': 'add_line.svg'}}, 'add_line.svg'),
    (('check.svg', '#f00'), 'check.svg-#f00'),
    ('add_line.svg', 'add_line.svg'),
    ({'name': 'xiaoming'}, 'confirm_fill.svg'),
    (None, 'confirm_fill.svg'),
    (object(), 'confirm_fill.svg'),
    (_HasIconObject(), 'confirm_fill.svg'),
    (_HasIconObject(icon='check.svg'), 'check.svg'),
    (_HasIconObject(icon=_HasIconObject('check.svg')), 'check.svg'),
))
def test_icon_formatter(monkeypatch, input_data, result):
    """Test icon_formatter with different input type."""
    def _new_call(self, path, color=None):
        """Mock function for MIcon()"""
        if color:
            return '{}-{}'.format(path, color)
        return path

    monkeypatch.setattr(MCacheDict, '__call__', _new_call)
    assert utils.icon_formatter(input_data) == result
