import pytest
from dayu_widgets import utils


class MyTestObject(object):
    def __init__(self, name, age):
        super(MyTestObject, self).__init__()
        self.name = name
        self.age = age


@pytest.mark.parametrize('input_dict', (
        {
            'obj': {'name': 'xiaoming', 'age': 18},
            'attr': 'name',
            'default': 'hhh',
            'result': 'xiaoming'
        },
        {
            'obj': {'name': 'xiaoming', 'age': 18},
            'attr': 'age',
            'default': 0,
            'result': 18
        },
        {
            'obj': {'name': 'xiaoming', 'age': 18},
            'attr': 'score',
            'default': 0,
            'result': 0
        },
        {
            'obj': MyTestObject('xiaoming', 18),
            'attr': 'name',
            'default': 'hhh',
            'result': 'xiaoming'
        },
        {
            'obj': MyTestObject('xiaoming', 18),
            'attr': 'age',
            'default': 0,
            'result': 18
        },
        {
            'obj': MyTestObject('xiaoming', 18),
            'attr': 'score',
            'default': 0,
            'result': 0
        },
))
def test_get_obj_value(input_dict):
    assert utils.get_obj_value(input_dict['obj'],
                               input_dict['attr'],
                               default=input_dict['default']) == input_dict['result']


@pytest.mark.parametrize('input_dict', (
        {
            'obj': {'name': 'xiaoming', 'age': 18},
            'attr': 'score',
            'value': 80
        }, {
            'obj': {'name': 'xiaoming', 'age': 18},
            'attr': 'name',
            'value': 'Tom'
        },
        {
            'obj': MyTestObject('xiaoming', 18),
            'attr': 'score',
            'value': 80
        },
        {
            'obj': MyTestObject('xiaoming', 18),
            'attr': 'name',
            'value': 'Tom'
        }))
def test_set_obj_value(input_dict):
    utils.set_obj_value(input_dict['obj'],
                        input_dict['attr'],
                        input_dict['value'])
    assert utils.get_obj_value(input_dict['obj'],
                               input_dict['attr']) == input_dict['value']


@pytest.mark.parametrize('input_dict', (
        {
            'obj': {'name': 'xiaoming', 'age': 18},
            'attr': 'score',
            'result': False
        }, {
            'obj': {'name': 'xiaoming', 'age': 18},
            'attr': 'name',
            'result': True
        },
        {
            'obj': MyTestObject('xiaoming', 18),
            'attr': 'score',
            'result': False
        },
        {
            'obj': MyTestObject('xiaoming', 18),
            'attr': 'name',
            'result': True
        }))
def test_has_obj_value(input_dict):
    assert utils.has_obj_value(input_dict['obj'],
                               input_dict['attr']) == input_dict['result']
