#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets import dayu_theme
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import *


@property_mixin
class MToolBar(QToolBar):
    def __init__(self, size=None, parent=None):
        super(MToolBar, self).__init__(parent=parent)
        self.setFloatable(False)
        self.setMovable(False)
        self.setAllowedAreas(Qt.TopToolBarArea)
        self.setOrientation(Qt.Horizontal)
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self._main_layout = QHBoxLayout()
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.addStretch()
        self.setLayout(self._main_layout)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self._button_group = QButtonGroup()
        self.setProperty('dayu_size', size or dayu_theme.default_size)
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
        if isinstance(data_dict, basestring):
            data_dict = {'text': data_dict}
        elif isinstance(data_dict, QIcon):
            data_dict = {'icon': data_dict}
        button = MToolButton(type=MToolButton.BarType,
                             icon=data_dict.get('icon'),
                             text=data_dict.get('text'),
                             size=self.property('dayu_size'),
                             parent=self)
        if data_dict.get('data'):
            button.setProperty('data', data_dict.get('data'))
        if data_dict.get('checked'):
            button.setProperty('checked', data_dict.get('checked'))
        if data_dict.get('shortcut'):
            button.setProperty('shortcut', data_dict.get('shortcut'))
        if data_dict.get('tooltip'):
            button.setProperty('toolTip', data_dict.get('tooltip'))
        if data_dict.get('clicked'):
            button.clicked.connect(data_dict.get('clicked'))
        if data_dict.get('toggled'):
            button.toggled.connect(data_dict.get('toggled'))
        action = QWidgetAction(self)
        action.setDefaultWidget(button)
        self.addAction(action)
