#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import *

from dayu_widgets.MTheme import global_theme
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import *

qss = '''
QToolButton[breadcrumb=true] {{
    border: none;
    background-color: transparent;
    qproperty-toolButtonStyle: ToolButtonTextBesideIcon;
}}
QToolButton[breadcrumb=true]:hover{{
    color: {primary_light};
}}
QToolButton[breadcrumb=true]:pressed{{
    color: {primary_dark};
}}
'''.format(**global_theme)


class MBreadcrumb(QWidget):
    def __init__(self, separator='/', size=MView.DefaultSize, parent=None):
        super(MBreadcrumb, self).__init__(parent)
        self._separator = separator
        self._main_layout = QHBoxLayout()
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.addStretch()
        self.setLayout(self._main_layout)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self._button_group = QButtonGroup()
        self._size = size
        self._label_list = []

    def set_item_list(self, data_list):
        for button in self._button_group.buttons():
            self._button_group.removeButton(button)
            self._main_layout.removeWidget(button)
            button.setVisible(False)
        for sep in self._label_list:
            self._button_group.removeButton(sep)
            self._main_layout.removeWidget(sep)
            sep.setVisible(False)

        for index, data_dict in enumerate(data_list):
            self.add_item(data_dict, index)

    def add_item(self, data_dict, index=None):
        button = MToolButton(icon_only=False, parent=self)
        button.setProperty('button_size', self._size)
        button.setProperty('breadcrumb', True)
        if isinstance(data_dict, basestring):
            data_dict = {'text': data_dict}
        elif isinstance(data_dict, QIcon):
            data_dict = {'icon': data_dict}
        if data_dict.get('text'):
            button.setProperty('text', data_dict.get('text'))
        if data_dict.get('icon'):
            button.setProperty('icon', data_dict.get('icon'))
        if data_dict.get('tooltip'):
            button.setProperty('toolTip', data_dict.get('tooltip'))
        if data_dict.get('clicked'):
            button.clicked.connect(data_dict.get('clicked'))

        button.setStyleSheet(u'{}\n{}'.format(button.styleSheet(), qss))
        if len(self._button_group.buttons()) != 0:
            separator = MLabel.help(self._separator)
            self._label_list.append(separator)
            self._main_layout.insertWidget(self._main_layout.count() - 1, separator)
        self._main_layout.insertWidget(self._main_layout.count() - 1, button)

        if index is None:
            self._button_group.addButton(button)
        else:
            self._button_group.addButton(button, index)
