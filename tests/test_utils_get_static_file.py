#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test get_static_file function.
"""
import os

import pytest

from dayu_widgets import utils, DEFAULT_STATIC_FOLDER, CUSTOM_STATIC_FOLDERS


@pytest.fixture(scope='module', name='custom_folder')
def setup_custom_folder(tmpdir_factory):
    """Create a folder to represent user's custom static folder"""
    # user has his custom static folder
    # put this icons or images in it
    tmp_folder = tmpdir_factory.mktemp('my_static')

    # create a file in base dir
    tmp_folder.join('add_line.svg').ensure()
    # create a sub folder and a file in the sub folder
    tmp_folder.join('sub_folder', 'sub_file.png').ensure()
    return tmp_folder


@pytest.mark.parametrize('input_path, output_path', (
    ('add_line.svg', os.path.join(DEFAULT_STATIC_FOLDER, 'add_line.svg')),
    ('check.svg', os.path.join(DEFAULT_STATIC_FOLDER, 'check.svg')),
    ('', None),
    ('a_not_exists_file', None),
    (os.path.join(os.path.dirname(__file__), 'for_test.txt'),
     os.path.join(os.path.dirname(__file__), 'for_test.txt')),  # user give a full path file, return
    ('main.qss', os.path.join(DEFAULT_STATIC_FOLDER, 'main.qss')),
))
def test_get_static_file(input_path, output_path):
    """Only default static file. Test different situation input."""
    assert utils.get_static_file(input_path) == output_path


def test_custom_static_folder(custom_folder):
    """Test when user append a custom static folder."""
    CUSTOM_STATIC_FOLDERS.append(str(custom_folder))
    for input_file, result in (
            ('add_line.svg', os.path.join(DEFAULT_STATIC_FOLDER, 'add_line.svg')),
            ('check.svg', os.path.join(DEFAULT_STATIC_FOLDER, 'check.svg')),
            ('', None),
            ('a_not_exists_file', None),
            (os.path.join(os.path.dirname(__file__), 'for_test.txt'),
             # user give a full path file, return
             os.path.join(os.path.dirname(__file__), 'for_test.txt')),
            ('sub_folder/sub_file.png',
             os.path.join(str(custom_folder), 'sub_folder/sub_file.png')),
    ):
        assert utils.get_static_file(input_file) == result


@pytest.mark.parametrize('input_file, error_type', (
    (3, 'int'),
    (set(), 'set'),
    ({}, 'dict'),
    (['g'], 'list'),
    ((2,), 'tuple'),
    (object(), 'object'),
))
def test_with_wrong_type(input_file, error_type):
    """Make sure when user give a wrong type arg, raise TypeError"""
    with pytest.raises(TypeError) as exc_info:
        utils.get_static_file(input_file)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Input argument 'path' should be basestring type, " \
                            "but get <type '{}'>".format(error_type)
