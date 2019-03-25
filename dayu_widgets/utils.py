#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2018.5
# Email : muyanru345@163.com
###################################################################

import collections
import datetime as dt

from qt import *
from singledispatch import singledispatch

ItemViewMenuEvent = collections.namedtuple('ItemViewMenuEvent', ['view', 'selection', 'extra'])


def get_static_file(path):
    from dayu_widgets import STATIC_FOLDERS
    full_path = next((os.path.join(prefix, path) for prefix in [''] + STATIC_FOLDERS if
                      os.path.isfile(os.path.join(prefix, path))), path)
    if os.path.isfile(full_path):
        return full_path
    return None


def from_list_to_nested_dict(input, sep='/'):
    result = []
    for item in input:
        components = item.strip(sep).split(sep)
        component_count = len(components)
        current = result
        for i, c in enumerate(components):
            atom = next((x for x in current if x['value'] == c), None)
            if atom is None:
                atom = {'value': c, 'label': c, 'children': []}
                current.append(atom)
            current = atom['children']
            if i == component_count - 1:
                atom.pop('children')
    return result


@singledispatch
def real_model(obj):
    return obj


@real_model.register(QSortFilterProxyModel)
def _(obj):
    return obj.sourceModel()


@real_model.register(QModelIndex)
def _(obj):
    return real_model(obj.model())


def real_index(index):
    model = index.model()
    if isinstance(model, QSortFilterProxyModel):
        return model.mapToSource(index)
    return index


def get_obj_value(data_obj, attr, default=None):
    if isinstance(data_obj, dict):
        return data_obj.get(attr, default)
    else:
        return getattr(data_obj, attr, default)


def set_obj_value(data_obj, attr, value):
    if isinstance(data_obj, dict):
        return data_obj.update({attr: value})
    else:
        return setattr(data_obj, attr, value)


def has_obj_value(data_obj, attr):
    if isinstance(data_obj, dict):
        return attr in data_obj.keys()
    else:
        return hasattr(data_obj, attr)


def apply_formatter(obj, *args, **kwargs):
    if obj is None:  # 压根就没有配置
        return args[0]
    elif isinstance(obj, dict):  # 字典选项型配置
        return obj.get(args[0], None)
    elif callable(obj):  # 回调函数型配置
        return obj(*args, **kwargs)
    else:  # 直接值型配置
        return obj


@singledispatch
def default_formatter(obj):
    return obj


@default_formatter.register(dict)
def _(obj):
    if 'name' in obj.keys():
        return default_formatter(obj.get('name'))
    elif 'code' in obj.keys():
        return default_formatter(obj.get('code'))
    else:
        return str(dict)


@default_formatter.register(list)
def _(obj):
    result = []
    for i in obj:
        result.append(default_formatter(i))
    return ','.join(result)


@default_formatter.register(str)
def _(obj):
    # ['utf-8', 'windows-1250', 'windows-1252', 'ISO-8859-1']
    return obj.decode('windows-1252')
    # return obj.decode()


@default_formatter.register(unicode)
def _(obj):
    return obj


@default_formatter.register(type(None))
def _(obj):
    return '--'


@default_formatter.register(object)
def _(obj):
    if hasattr(obj, 'name'):
        return default_formatter(getattr(obj, 'name'))
    if hasattr(obj, 'code'):
        return default_formatter(getattr(obj, 'code'))
    return str(obj)


@default_formatter.register(dt.datetime)
def _(obj):
    return obj.strftime('%Y-%m-%d %H:%M:%S')


def get_font(underline=False, bold=False):
    _font = QFont()
    _font.setUnderline(underline)
    _font.setBold(bold)
    return _font


@singledispatch
def icon_formatter(obj):
    return obj


@icon_formatter.register(dict)
def _(data_obj):
    setting_list = [('icon', '{}')]
    for attr, formatter in setting_list:
        path = get_obj_value(data_obj, attr)
        if path:
            return icon_formatter(formatter.format(path))
    return icon_formatter('confirm_fill.svg')


@icon_formatter.register(object)
def _(data_obj):
    setting_list = [('icon', '{}'), ('thumbnail_path', '{}'), ('__tablename__', 'entity_{}.svg')]
    for attr, formatter in setting_list:
        path = get_obj_value(data_obj, attr)
        if path:
            return icon_formatter(formatter.format(path))
    return icon_formatter('confirm_fill.svg')


@icon_formatter.register(basestring)
def _(path):
    return MIcon(path)


@icon_formatter.register(tuple)
def _(path):
    return MIcon(*path)


def dump_structure(obj, spaceCount):
    print "{0}{1} : {2}".format(
        " " * spaceCount,
        obj.metaObject().className(),
        obj.objectName())

    for child in obj.children():
        dump_structure(child, spaceCount + 4)


if __name__ == '__main__':
    import sys
    from dayu_widgets import MComboBox

    app = QApplication(sys.argv)
    button = MComboBox()
    dump_structure(button, 4)
    button.show()
    sys.exit(app.exec_())
