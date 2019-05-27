#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import pytest

from dayu_widgets import utils, STATIC_FOLDERS


@pytest.fixture(scope='module')
def custom_static_folder(tmpdir_factory):
    """Create a folder to represent user's custom static folder"""
    # user has his custom static folder
    # put this icons or images in it
    custom_folder = tmpdir_factory.mktemp('my_static')

    # create a file in base dir
    custom_folder.join('add_line.svg').ensure()
    # create a sub folder and a file in the sub folder
    custom_folder.join('sub_folder', 'sub_file.png').ensure()
    return custom_folder


@pytest.fixture(scope='module')
def default_static_folder():
    """Get dayu_widgets default static folder"""
    return STATIC_FOLDERS[0]


def test_get_static_file(default_static_folder):
    for input_file, result in (
            ('add_line.svg', os.path.join(default_static_folder, 'add_line.svg')),
            ('check.svg', os.path.join(default_static_folder, 'check.svg')),
            ('', None),
            ('a_not_exists_file', None),
            (os.path.join(os.path.dirname(__file__), 'for_test.txt'),
             os.path.join(os.path.dirname(__file__), 'for_test.txt')),  # user give a full path file, return
            ('main.qss', os.path.join(default_static_folder, 'main.qss')),
    ):
        assert utils.get_static_file(input_file) == result


def test_get_custom_insert_static_folder(default_static_folder, custom_static_folder):
    STATIC_FOLDERS.insert(0, str(custom_static_folder))
    for input_file, result in (
            ('add_line.svg',
             os.path.join(str(custom_static_folder), 'add_line.svg')),
            ('check.svg',
             os.path.join(default_static_folder, 'check.svg')),
            ('',
             None),
            ('a_not_exists_file',
             None),
            (os.path.join(os.path.dirname(__file__), 'for_test.txt'),
             os.path.join(os.path.dirname(__file__), 'for_test.txt')),  # user give a full path file, return
            ('sub_folder/sub_file.png',
             os.path.join(str(custom_static_folder), 'sub_folder/sub_file.png')),
    ):
        assert utils.get_static_file(input_file) == result
    STATIC_FOLDERS.pop(0)


def test_get_custom_append_static_folder(default_static_folder, custom_static_folder):
    STATIC_FOLDERS.append(str(custom_static_folder))
    for input_file, result in (
            ('add_line.svg', os.path.join(default_static_folder, 'add_line.svg')),
            ('check.svg', os.path.join(default_static_folder, 'check.svg')),
            ('', None),
            ('a_not_exists_file', None),
            (os.path.join(os.path.dirname(__file__), 'for_test.txt'),
             os.path.join(os.path.dirname(__file__), 'for_test.txt')),  # user give a full path file, return
            ('sub_folder/sub_file.png', os.path.join(str(custom_static_folder), 'sub_folder/sub_file.png')),
    ):
        assert utils.get_static_file(input_file) == result
    STATIC_FOLDERS.pop(-1)


@pytest.mark.parametrize('input_file, error_type', (
        (3, 'int'),
        (set(), 'set'),
        ({}, 'dict'),
        (['g'], 'list'),
        ((2,), 'tuple'),
        (object(), 'object'),
))
def test_get_static_file_with_wrong_type(input_file, error_type):
    """Make sure when user give a wrong type arg, raise TypeError"""
    with pytest.raises(TypeError) as exc_info:
        utils.get_static_file(input_file)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Input argument 'path' should be basestring type, but get <type '{}'>".format(error_type)
