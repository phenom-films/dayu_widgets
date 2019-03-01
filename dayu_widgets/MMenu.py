#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
import functools
from MTheme import global_theme
from MButton import MButton
from MLabel import MLabel
from MAvatar import MAvatar
import utils
from qt import *

qss = '''
QMenu {{
    {text_font}
    background-color: {background};
    padding: 0;
    border-radius: 2px;
    border: 1px solid {border};
}} 
QMenu[checked=true]{{
    color: {primary};
    background-color: {background_selected};
}}
QMenu::item {{
    padding: 2px 2px;
}}
QMenu::indicator {{
    left: 6px;
}}
QMenu::item {{
    padding: 8px auto;
}}
QMenu::item:checked  {{
    color: {primary};
    background-color: {background_selected};
}}
QMenu::item:selected  {{
    background-color: {background_selected};
}}
'''.format(**global_theme)


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


@property_mixin
class MMenu(QMenu):
    sig_value_changed = Signal(list)
    sig_index_changed = Signal(int)

    def __init__(self, exclusive=True, cascader=False, title='', parent=None):
        super(MMenu, self).__init__(title=title, parent=parent)
        self.setProperty('cascader', cascader)
        self.setCursor(Qt.PointingHandCursor)
        self._action_group = QActionGroup(self)
        self._action_group.setExclusive(exclusive)
        self._action_group.triggered.connect(self.slot_on_action_triggered)
        self._load_data_func = None
        self.set_value('')
        self.set_separator('/')
        self.setStyleSheet(qss)

    def set_separator(self, chr):
        self.setProperty('separator', chr)

    def set_load_callback(self, func):
        assert callable(func)
        self._load_data_func = func
        self.aboutToShow.connect(self.slot_fetch_data)

    def slot_fetch_data(self):
        data_list = self._load_data_func()
        self.set_data(data_list)

    def set_value(self, data):
        assert isinstance(data, (basestring, list, int))
        if isinstance(data, int):
            action = self._action_group.actions()[data]
            data = action.property('value')
        elif self.property('cascader') and isinstance(data, basestring):
            data = data.split(self.property('separator'))
        self.setProperty('value', data)

    def _set_value(self, value):
        data_list = value if isinstance(value, list) else [value]
        flag = False
        for act in self._action_group.actions():
            checked = act.property('value') in data_list
            if act.isChecked() != checked:  # 更新来自代码
                act.setChecked(checked)
                flag = True
        if flag:
            self.sig_value_changed.emit(value)

    def _add_menu(self, parent_menu, data_dict):
        if 'children' in data_dict:
            menu = QMenu(title=data_dict.get('label'), parent=self)
            menu.setProperty('value', data_dict.get('value'))
            parent_menu.addMenu(menu)
            if not (parent_menu is self):
                menu.setProperty('parent_menu', parent_menu)
            for i in data_dict.get('children'):
                self._add_menu(menu, i)
        else:
            action = self._action_group.addAction(utils.default_formatter(data_dict.get('label')))
            action.setProperty('value', data_dict.get('value'))
            action.setCheckable(True)
            action.setProperty('parent_menu', parent_menu)
            parent_menu.addAction(action)

    def set_data(self, option_list):
        assert isinstance(option_list, list)
        if all(isinstance(i, basestring) for i in option_list):
            option_list = from_list_to_nested_dict(option_list, sep=self.property('separator'))
        self.setProperty('data', option_list)

    def _set_data(self, option_list):
        self.clear()
        for act in self._action_group.actions():
            self._action_group.removeAction(act)

        for data_dict in option_list:
            self._add_menu(self, data_dict)

    def _get_parent(self, result, obj):
        if obj.property('parent_menu'):
            parent_menu = obj.property('parent_menu')
            result.insert(0, parent_menu.title())
            self._get_parent(result, parent_menu)

    @Slot(QAction)
    def slot_on_action_triggered(self, action):
        current_data = action.property('value')
        if self.property('cascader'):
            selected_data = [current_data]
            self._get_parent(selected_data, action)
        else:
            if self._action_group.isExclusive():
                selected_data = current_data
            else:
                selected_data = [act.property('value') for act in self._action_group.actions() if act.isChecked()]
        self.set_value(selected_data)
        self.sig_value_changed.emit(selected_data)
        self.sig_index_changed.emit(self._action_group.actions().index(action))

    def set_loader(self, func):
        self._load_data_func = func
