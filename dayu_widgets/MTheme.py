#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
import UserDict
import json

from dayu_widgets.qt import MIcon


class MDict(UserDict.UserDict, object):
    def __init__(self, *args, **kwargs):
        super(MDict, self).__init__(*args, **kwargs)

    def __getattr__(self, item):
        return self.data.get(item)


class MIconDict(UserDict.UserDict, object):
    def __init__(self, *args, **kwargs):
        super(MIconDict, self).__init__(*args, **kwargs)

    def __getattr__(self, item):
        return MIcon(self.data.get(item) + '.svg')


class MTheme(object):
    def __init__(self, theme='light'):
        super(MTheme, self).__init__()
        from dayu_widgets import utils
        default_qss_file = utils.get_static_file('main.qss')
        with open(default_qss_file, 'r+') as f:
            self.default_qss = f.read()
        self.color = None
        self.font = None
        self.size = None
        self.icon = None
        self.full_dict = None
        self.set_theme(theme)

    def get_cascading_json(self, json_file, target_dict):
        from dayu_widgets import utils
        with open(json_file, 'r') as j_f:
            data_dict = json.load(j_f)
            parent_file = data_dict.get('include') and utils.get_static_file(data_dict.get('include'))
            if parent_file:
                self.get_cascading_json(parent_file, target_dict)
            for key in ['color', 'size', 'font', 'icon']:
                if key in data_dict:
                    target_dict[key].update(data_dict[key])

    def set_theme(self, theme):
        from dayu_widgets import utils, STATIC_FOLDERS
        theme_file = utils.get_static_file('{}.json'.format(theme))
        target_dict = {'color': {}, 'size': {}, 'font': {}, 'icon': {}}
        self.get_cascading_json(theme_file, target_dict)
        for key, icon in target_dict.get('icon').items():
            target_dict['icon'][key] = 'url({}/{})'.format(STATIC_FOLDERS[0].replace('\\', '/'), icon)
        self.color = MDict(target_dict.get('color'))
        self.font = MDict(target_dict.get('font'))
        self.size = MDict(target_dict.get('size'))
        self.icon = MDict(target_dict.get('icon'))
        self.full_dict = target_dict.get('color')
        self.full_dict.update(target_dict.get('font'))
        self.full_dict.update(target_dict.get('size'))
        self.full_dict.update(target_dict.get('icon'))
        self.default_size = self.size.medium

    def apply(self, widget):
        widget.setStyleSheet(self.default_qss.format(**self.full_dict))

    def deco(self, cls):
        original_init__ = cls.__init__

        def my__init__(instance, *args, **kwargs):
            original_init__(instance, *args, **kwargs)
            instance.setStyleSheet(self.default_qss.format(**self.full_dict))

        def polish(instance):
            instance.style().polish(instance)

        setattr(cls, '__init__', my__init__)
        setattr(cls, 'polish', polish)
        return cls
