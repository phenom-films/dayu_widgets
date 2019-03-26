#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MLabel import MLabel
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.qt import *
from dayu_widgets import dayu_theme


class MBreadcrumb(QWidget):
    def __init__(self, separator='/', size=None, parent=None):
        super(MBreadcrumb, self).__init__(parent)
        self._separator = separator
        self._main_layout = QHBoxLayout()
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.addStretch()
        self.setLayout(self._main_layout)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self._button_group = QButtonGroup()
        self._size = size or dayu_theme.default_size
        self.separator_class_dict = {
            dayu_theme.size.huge: MLabel.h1,
            dayu_theme.size.large: MLabel.h2,
            dayu_theme.size.medium: MLabel.h3,
            dayu_theme.size.small: MLabel,
            dayu_theme.size.tiny: MLabel.help,
        }
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
        button = MToolButton(text=data_dict.get('text'),
                             icon=data_dict.get('icon'),
                             type=MToolButton.BreadcrumbType,
                             size=data_dict.get('size') or self._size,
                             parent=self)
        if data_dict.get('tooltip'):
            button.setProperty('toolTip', data_dict.get('tooltip'))
        if data_dict.get('clicked'):
            button.clicked.connect(data_dict.get('clicked'))

        if len(self._button_group.buttons()) != 0:
            separator = self.separator_class_dict.get(self._size)(self._separator)
            self._label_list.append(separator)
            self._main_layout.insertWidget(self._main_layout.count() - 1, separator)
        self._main_layout.insertWidget(self._main_layout.count() - 1, button)

        if index is None:
            self._button_group.addButton(button)
        else:
            self._button_group.addButton(button, index)
