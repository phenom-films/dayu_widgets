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
    '''
    A convenient function to get the file in dayu_widgets/static,
    User just give the name of the file.
    eg. get_static_file('add_line.svg')
    :param path: file name
    :return: if input file found, return the full path, else return None
    '''
    if not isinstance(path, basestring):
        raise TypeError("Input argument 'path' should be basestring type, but get {}".format(type(path)))
    from dayu_widgets import STATIC_FOLDERS
    full_path = next((os.path.join(prefix, path) for prefix in [''] + STATIC_FOLDERS if
                      os.path.isfile(os.path.join(prefix, path))), path)
    if os.path.isfile(full_path):
        return full_path
    return None


def from_list_to_nested_dict(input_arg, sep='/'):
    '''
    A help function to convert the list of string to nested dict
    :param input_arg: a list/tuple/set of string
    :param sep: a separator to split input string
    :return: a list of nested dict
    '''
    if not isinstance(input_arg, (list, tuple, set)):
        raise TypeError("Input argument 'input' should be list or tuple or set, but get {}".format(type(input_arg)))
    if not isinstance(sep, basestring):
        raise TypeError("Input argument 'sep' should be basestring, but get {}".format(type(sep)))

    result = []
    for item in input_arg:
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


def fade_color(color, alpha):
    c = QColor(color)
    return 'rgba({}, {}, {}, {})'.format(c.red(), c.green(), c.blue(), alpha)


def generate_color(primary_color, index):
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

    def get_hue(color, i, is_light):
        h = color.hue()
        if h >= 60 and h <= 240:
            hue = h - hue_step * i if is_light else h + hue_step * i
        else:
            hue = h + hue_step * i if is_light else h - hue_step * i
        if hue < 0:
            hue += 359
        elif hue >= 359:
            hue -= 359
        return hue / 359.0

    def get_saturation(color, i, is_light):
        s = color.saturationF() * 100
        if is_light:
            saturation = s - saturation_step * i
        elif i == dark_color_count:
            saturation = s + saturation_step
        else:
            saturation = s + saturation_step2 * i
        saturation = min(100.0, saturation)
        if is_light and i == light_color_count and saturation > 10:
            saturation = 10
        saturation = max(6.0, saturation)
        return round(saturation * 10) / 1000.0

    def get_value(color, i, is_light):
        v = color.valueF()
        if is_light:
            return min((v * 100 + brightness_step1 * i) / 100, 1.0)
        return max((v * 100 - brightness_step2 * i) / 100, 0.0)

    light = index <= 6
    hsv_color = QColor(primary_color) if isinstance(primary_color, basestring) else primary_color
    index = light_color_count + 1 - index if light else index - light_color_count - 1
    return QColor.fromHsvF(
        get_hue(hsv_color, index, light),
        get_saturation(hsv_color, index, light),
        get_value(hsv_color, index, light)
    ).name()


def draw_empty_content(view, text=None, pix_map=None):
    from dayu_widgets import dayu_theme
    pix_map = pix_map or MPixmap('empty.svg')
    text = text or view.tr('No Data')
    painter = QPainter(view)
    font_metrics = painter.fontMetrics()
    painter.setPen(QPen(dayu_theme.secondary_text_color))
    content_height = pix_map.height() + font_metrics.height()
    padding = 10
    proper_min_size = min(view.height() - padding * 2, view.width() - padding * 2, content_height)
    if proper_min_size < content_height:
        pix_map = pix_map.scaledToHeight(proper_min_size - font_metrics.height(), Qt.SmoothTransformation)
        content_height = proper_min_size
    painter.drawText(view.width() / 2 - font_metrics.width(text) / 2,
                     view.height() / 2 + content_height / 2 - font_metrics.height() / 2,
                     text)
    painter.drawPixmap(view.width() / 2 - pix_map.width() / 2,
                       view.height() / 2 - content_height / 2, pix_map)
    painter.end()


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
        return str(obj)


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


@default_formatter.register(int)
def _(obj):
    return str(obj)


@default_formatter.register(float)
def _(obj):
    return '{:.2f}'.format(round(obj, 2))


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


def dump_structure(obj, space_count):
    print "{0}{1} : {2}".format(
        " " * space_count,
        obj.metaObject().className(),
        obj.objectName())

    for child in obj.children():
        dump_structure(child, space_count + 4)


if __name__ == '__main__':
    import sys
    from dayu_widgets import MComboBox

    app = QApplication(sys.argv)
    button = MComboBox()
    dump_structure(button, 4)
    button.show()
    sys.exit(app.exec_())
