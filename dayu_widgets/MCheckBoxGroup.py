#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from qt import *
from MTheme import global_theme
from MCheckBox import MCheckBox
from MMenu import MMenu
import functools


@property_mixin
class MCheckBoxGroup(QWidget):
    sig_checked_changed = Signal(list)

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(MCheckBoxGroup, self).__init__(parent=parent)
        self._button_group = QButtonGroup()
        self._button_group.setExclusive(False)
        self._main_layout = QBoxLayout(
            QBoxLayout.LeftToRight if orientation == Qt.Horizontal else QBoxLayout.TopToBottom)
        if orientation == Qt.Horizontal:
            self._main_layout.addStretch()
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self._main_layout.setSpacing(15)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._main_layout)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._slot_context_menu)

        self.setProperty('orientation', 'horizontal' if orientation == Qt.Horizontal else 'vertical')
        self.set_value(None)

    @Slot(QPoint)
    def _slot_context_menu(self, point):
        context_menu = MMenu(parent=self)
        action_select_all = context_menu.addAction('Select All')
        action_select_none = context_menu.addAction('Select None')
        action_select_invert = context_menu.addAction('Select Invert')
        action_select_all.triggered.connect(functools.partial(self._slot_set_select, True))
        action_select_none.triggered.connect(functools.partial(self._slot_set_select, False))
        action_select_invert.triggered.connect(functools.partial(self._slot_set_select, None))
        context_menu.exec_(QCursor.pos() + QPoint(10, 10))

    @Slot(bool)
    def _slot_set_select(self, state):
        for check_box in self._button_group.buttons():
            if state is None:
                old_state = check_box.isChecked()
                check_box.setChecked(not old_state)
            else:
                check_box.setChecked(state)
        self._slot_map_signal()

    def add_check_box_list(self, button_list):
        for index, data_dict in enumerate(button_list):
            button = MCheckBox(parent=self)
            if isinstance(data_dict, basestring):
                button.setProperty('text', data_dict)
            elif isinstance(data_dict, dict):
                button.setProperty('text', data_dict.get('text'))
                if data_dict.get('icon'):
                    button.setProperty('icon', MIcon((data_dict.get('icon', '') + '.png')))
                if data_dict.get('data'):
                    button.setProperty('data', data_dict.get('data'))
                if data_dict.get('checked'):
                    button.setProperty('checked', data_dict.get('checked'))
            else:
                button.setProperty('text', str(data_dict))
            button.stateChanged.connect(self._slot_map_signal)
            self._button_group.addButton(button, index)
            self._main_layout.insertWidget(self._main_layout.count() - 1, button)

    @Slot(int)
    def _slot_map_signal(self, state=None):
        self.sig_checked_changed.emit(
            [check_box.text() for check_box in self._button_group.buttons() if check_box.isChecked()])

    def set_value(self, value):
        if not isinstance(value, list):
            value = [value]
        self.setProperty('value', value)

    def _set_value(self, value):
        edit_from_code = False
        for check_box in self._button_group.buttons():
            flag = Qt.Checked if check_box.text() in value else Qt.Unchecked
            if flag != check_box.checkState():
                # 更新来自代码
                edit_from_code = True
                check_box.setCheckState(flag)
        if edit_from_code:
            self.sig_checked_changed.emit(value)
