#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2018.5
# Email : muyanru345@163.com
###################################################################
"""
Some helper functions for handling color and formatter.
"""

import collections
import datetime as dt
import math
import os

from singledispatch import singledispatch

from dayu_widgets import DEFAULT_STATIC_FOLDER, CUSTOM_STATIC_FOLDERS
from dayu_widgets.qt import QColor, QSortFilterProxyModel, QModelIndex, QFont, MIcon, QIcon

ItemViewMenuEvent = collections.namedtuple('ItemViewMenuEvent', ['view', 'selection', 'extra'])


def get_static_file(path):
    """
    A convenient function to get the file in dayu_widgets/static,
    User just give the name of the file.
    eg. get_static_file('add_line.svg')
    :param path: file name
    :return: if input file found, return the full path, else return None
    """
    if not isinstance(path, basestring):
        raise TypeError("Input argument 'path' should be basestring type, "
                        "but get {}".format(type(path)))
    full_path = next((os.path.join(prefix, path)
                      for prefix in ['', DEFAULT_STATIC_FOLDER] + CUSTOM_STATIC_FOLDERS
                      if os.path.isfile(os.path.join(prefix, path))),
                     path)
    if os.path.isfile(full_path):
        return full_path
    return None


def from_list_to_nested_dict(input_arg, sep='/'):
    """
    A help function to convert the list of string to nested dict
    :param input_arg: a list/tuple/set of string
    :param sep: a separator to split input string
    :return: a list of nested dict
    """
    if not isinstance(input_arg, (list, tuple, set)):
        raise TypeError("Input argument 'input' should be list or tuple or set, "
                        "but get {}".format(type(input_arg)))
    if not isinstance(sep, basestring):
        raise TypeError("Input argument 'sep' should be basestring, "
                        "but get {}".format(type(sep)))

    result = []
    for item in input_arg:
        components = item.strip(sep).split(sep)
        component_count = len(components)
        current = result
        for i, comp in enumerate(components):
            atom = next((x for x in current if x['value'] == comp), None)
            if atom is None:
                atom = {'value': comp, 'label': comp, 'children': []}
                current.append(atom)
            current = atom['children']
            if i == component_count - 1:
                atom.pop('children')
    return result


def fade_color(color, alpha):
    """
    Fade color with given alpha.
    eg. fade_color('#ff0000', '10%) => 'rgba(255, 0, 0, 10%)'
    :param color: string, hex digit format '#RRGGBB'
    :param alpha: string, percent 'number%'
    :return: qss/css color format rgba(r, g, b, a)
    """
    q_color = QColor(color)
    return 'rgba({}, {}, {}, {})'.format(q_color.red(), q_color.green(), q_color.blue(), alpha)


def generate_color(primary_color, index):
    """
    Reference to ant-design color system algorithm.
    :param primary_color: base color. #RRGGBB
    :param index: color step. 1-10 from light to dark
    :return: result color
    """
    # 这里生成颜色的算法，来自 Ant Design, 只做了语言的转换，和颜色的类型的转换，没对算法做任何修改
    # https://github.com/ant-design/ant-design/blob/master/components/style/color/colorPalette.less
    # https://zhuanlan.zhihu.com/p/32422584

    hue_step = 2
    saturation_step = 16
    saturation_step2 = 5
    brightness_step1 = 5
    brightness_step2 = 15
    light_color_count = 5
    dark_color_count = 4

    def _get_hue(color, i, is_light):
        h_comp = color.hue()
        if 60 <= h_comp <= 240:
            hue = h_comp - hue_step * i if is_light else h_comp + hue_step * i
        else:
            hue = h_comp + hue_step * i if is_light else h_comp - hue_step * i
        if hue < 0:
            hue += 359
        elif hue >= 359:
            hue -= 359
        return hue / 359.0

    def _get_saturation(color, i, is_light):
        s_comp = color.saturationF() * 100
        if is_light:
            saturation = s_comp - saturation_step * i
        elif i == dark_color_count:
            saturation = s_comp + saturation_step
        else:
            saturation = s_comp + saturation_step2 * i
        saturation = min(100.0, saturation)
        if is_light and i == light_color_count and saturation > 10:
            saturation = 10
        saturation = max(6.0, saturation)
        return round(saturation * 10) / 1000.0

    def _get_value(color, i, is_light):
        v_comp = color.valueF()
        if is_light:
            return min((v_comp * 100 + brightness_step1 * i) / 100, 1.0)
        return max((v_comp * 100 - brightness_step2 * i) / 100, 0.0)

    light = index <= 6
    hsv_color = QColor(primary_color) if isinstance(primary_color, basestring) else primary_color
    index = light_color_count + 1 - index if light else index - light_color_count - 1
    return QColor.fromHsvF(
        _get_hue(hsv_color, index, light),
        _get_saturation(hsv_color, index, light),
        _get_value(hsv_color, index, light)
    ).name()


@singledispatch
def real_model(source_model):
    """
    Get the source model whenever user give a source index or proxy index or proxy model.
    """
    return source_model


@real_model.register(QSortFilterProxyModel)
def _(proxy_model):
    return proxy_model.sourceModel()


@real_model.register(QModelIndex)
def _(index):
    return real_model(index.model())


def real_index(index):
    """
    Get the source index whenever user give a source index or proxy index.
    """
    model = index.model()
    if isinstance(model, QSortFilterProxyModel):
        return model.mapToSource(index)
    return index


def get_obj_value(data_obj, attr, default=None):
    """Get dict's key or object's attribute with given attr"""
    if isinstance(data_obj, dict):
        return data_obj.get(attr, default)
    return getattr(data_obj, attr, default)


def set_obj_value(data_obj, attr, value):
    """Set dict's key or object's attribute with given attr and value"""
    if isinstance(data_obj, dict):
        return data_obj.update({attr: value})
    return setattr(data_obj, attr, value)


def has_obj_value(data_obj, attr):
    """Return weather dict has the given key or object has the given attribute."""
    if isinstance(data_obj, dict):
        return attr in data_obj.keys()
    return hasattr(data_obj, attr)


def apply_formatter(formatter, *args, **kwargs):
    """
    Used for QAbstractModel data method.
    Config a formatter for one field, apply the formatter with the index data.
    :param formatter: formatter. It can be None/dict/callable or just any type of value
    :param args:
    :param kwargs:
    :return: apply the formatter with args and kwargs
    """
    if formatter is None:  # 压根就没有配置
        return args[0]
    elif isinstance(formatter, dict):  # 字典选项型配置
        return formatter.get(args[0], None)
    elif callable(formatter):  # 回调函数型配置
        return formatter(*args, **kwargs)
    # 直接值型配置
    return formatter


@singledispatch
def display_formatter(input_other_type):
    """
    Used for QAbstractItemModel data method for Qt.DisplayRole
    Format any input value to a string.
    :param input_other_type: any type value
    :return: basestring
    """
    return str(input_other_type)  # this function never reached


@display_formatter.register(dict)
def _(input_dict):
    if 'name' in input_dict.keys():
        return display_formatter(input_dict.get('name'))
    elif 'code' in input_dict.keys():
        return display_formatter(input_dict.get('code'))
    return str(input_dict)


@display_formatter.register(list)
def _(input_list):
    result = []
    for i in input_list:
        result.append(display_formatter(i))
    return ','.join(result)


@display_formatter.register(str)
def _(input_str):
    # ['utf-8', 'windows-1250', 'windows-1252', 'ISO-8859-1']
    return input_str.decode('windows-1252')
    # return obj.decode()


@display_formatter.register(unicode)
def _(input_unicode):
    return input_unicode


@display_formatter.register(type(None))
def _(input_none):
    return '--'


@display_formatter.register(int)
def _(input_int):
    return str(input_int)


@display_formatter.register(float)
def _(input_float):
    return '{:.2f}'.format(round(input_float, 2))


@display_formatter.register(object)
def _(input_object):
    if hasattr(input_object, 'name'):
        return display_formatter(getattr(input_object, 'name'))
    if hasattr(input_object, 'code'):
        return display_formatter(getattr(input_object, 'code'))
    return str(input_object)


@display_formatter.register(dt.datetime)
def _(input_datetime):
    return input_datetime.strftime('%Y-%m-%d %H:%M:%S')


def font_formatter(setting_dict):
    """
    Used for QAbstractItemModel data method for Qt.FontRole
    :param underline: font style underline
    :param bold: font style bold
    :return: a QFont instance with given style
    """
    _font = QFont()
    _font.setUnderline(setting_dict.get('underline') or False)
    _font.setBold(setting_dict.get('bold') or False)
    return _font


@singledispatch
def icon_formatter(input_other_type):
    """
    Used for QAbstractItemModel data method for Qt.DecorationRole
    A helper function to easy get QIcon.
    The input can be dict/object, string, None, tuple(file_path, fill_color)
    :param input_other_type:
    :return: a QIcon instance
    """
    return input_other_type  # this function never reached


@icon_formatter.register(dict)
def _(input_dict):
    attr_list = ['icon']
    path = next((get_obj_value(input_dict, attr) for attr in attr_list), None)
    return icon_formatter(path)


@icon_formatter.register(QIcon)
def _(input_dict):
    return input_dict


@icon_formatter.register(object)
def _(input_object):
    attr_list = ['icon']
    path = next((get_obj_value(input_object, attr) for attr in attr_list), None)
    return icon_formatter(path)


@icon_formatter.register(basestring)
def _(input_string):
    return MIcon(input_string)


@icon_formatter.register(tuple)
def _(input_tuple):
    return MIcon(*input_tuple)


@icon_formatter.register(type(None))
def _(input_none):
    return icon_formatter('confirm_fill.svg')


def overflow_format(num, overflow):
    """
    Give a integer, return a string.
    When this integer is large than given overflow, return "overflow+"
    """
    if not isinstance(num, int):
        raise ValueError("Input argument 'num' should be int type, "
                         "but get {}".format(type(num)))
    if not isinstance(overflow, int):
        raise ValueError("Input argument 'overflow' should be int type, "
                         "but get {}".format(type(overflow)))
    return str(num) if num <= overflow else '{}+'.format(overflow)


def get_percent(value, minimum, maximum):
    """
    Get a given value's percent in the range.
    :param value: value
    :param minimum: the range's minimum value
    :param maximum: the range's maximum value
    :return: percent float
    """
    if minimum == maximum:
        # reference from qprogressbar.cpp
        # If max and min are equal and we get this far, it means that the
        # progress bar has one step and that we are on that step. Return
        # 100% here in order to avoid division by zero further down.
        return 100
    return max(0, min(100, (value - minimum) * 100 / (maximum - minimum)))


def get_total_page(total, per):
    """
    Get the page count.
    :param total: total count
    :param per: count per page
    :return: page count int
    """
    return int(math.ceil(1.0 * total / per))


def get_page_display_string(current, per, total):
    """
    Get the format string x - x of xx
    :param current: current page
    :param per: count per page
    :param total: total count
    :return: str
    """
    return '{start} - {end} of {total}'.format(
        start=((current - 1) * per + 1) if current else 0,
        end=min(total, current * per),
        total=total)
