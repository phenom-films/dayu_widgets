#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2018.5
# Email : muyanru345@163.com
###################################################################

import collections
import datetime as dt
import os

from singledispatch import singledispatch

from qt import *


MenuEvent = collections.namedtuple('MenuEvent', ['view', 'selection', 'extra'])


# default_qss_file = request_file('qss/main.qss')
# with open(default_qss_file, 'r+') as f:
#     default_qss = f.read().replace('url(', 'url({}/'.format(os.path.dirname(default_qss_file).replace('\\', '/')))


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


def dayu_css(css_content=None):
    def wrapper1(func):
        def new_init(*args, **kwargs):
            result = func(*args, **kwargs)
            instance = args[0]
            instance.setStyleSheet(css_content if css_content else default_qss)
            return result

        return new_init

    return wrapper1


def show_loading():
    def wrapper1(waste_time_func):
        def new_init(*args, **kwargs):
            from loading_widget import MLoadingWidget, MLoadingThread
            instance = args[0]
            loading_widget = MLoadingWidget(instance)
            print instance.pos(), instance.mapFromParent(instance.pos()), instance.mapToGlobal(instance.pos())
            start_point = instance.pos()  # instance.mapToGlobal(instance.pos())
            loading_widget.setGeometry(start_point.x(), start_point.y(), instance.width(), instance.height())
            loading_widget.show()
            th = MLoadingThread(instance)
            th.set_func(waste_time_func, *args, **kwargs)
            th.sig_finished.connect(getattr(instance, waste_time_func.__name__ + '_finished'))
            th.finished.connect(loading_widget.close)
            th.start()
            return

        return new_init

    return wrapper1


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
    setting_list = [('icon', '{}'), ('thumbnail_path', '{}'), ('meaning', 'icon-{}.png'),
                    ('__tablename__', 'icon-{}.png')]
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
