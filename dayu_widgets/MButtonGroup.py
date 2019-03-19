#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

import functools

from dayu_widgets.MCheckBox import MCheckBox
from dayu_widgets.MMenu import MMenu
from dayu_widgets.MPushButton import MPushButton
from dayu_widgets.MRadioButton import MRadioButton
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import *


@property_mixin
class MButtonGroupBase(QWidget):
    button_class = MPushButton

    def __init__(self, orientation=Qt.Horizontal, size=MView.DefaultSize, parent=None):
        super(MButtonGroupBase, self).__init__(parent=parent)
        self._main_layout = QBoxLayout(
            QBoxLayout.LeftToRight if orientation == Qt.Horizontal else QBoxLayout.TopToBottom)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._main_layout)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self._button_group = QButtonGroup()
        self._orientation = 'horizontal' if orientation == Qt.Horizontal else 'vertical'
        self._size = size

    def _set_exclusive(self, value):
        self._button_group.setExclusive(value)

    def set_spacing(self, value):
        self._main_layout.setSpacing(value)

    def get_button_group(self):
        return self._button_group

    def add_button(self, data_dict, index=None):
        button = self.button_class(parent=self)
        button.setProperty('combine', self._orientation)
        button.setProperty('button_size', self._size)
        if isinstance(data_dict, basestring):
            data_dict = {'text': data_dict}
        elif isinstance(data_dict, QIcon):
            data_dict = {'icon': data_dict}
        if data_dict.get('text'):
            button.setProperty('text', data_dict.get('text'))
        if data_dict.get('icon'):
            button.setProperty('icon', data_dict.get('icon'))
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

        self._after_created(button, data_dict)
        if index is None:
            self._button_group.addButton(button)
        else:
            self._button_group.addButton(button, index)
        # offset = -1 if self._main_layout.direction() == QBoxLayout.LeftToRight else 0
        self._main_layout.insertWidget(self._main_layout.count(), button)

    def set_button_list(self, button_list):
        for button in self._button_group.buttons():
            self._button_group.removeButton(button)
            self._main_layout.removeWidget(button)
            button.setVisible(False)
        for index, data_dict in enumerate(button_list):
            self.add_button(data_dict, index)

    def _after_created(self, button, data_dict):
        pass


class MPushButtonGroup(MButtonGroupBase):
    button_class = MPushButton

    def __init__(self, orientation=Qt.Horizontal, size=MView.DefaultSize, parent=None):
        super(MPushButtonGroup, self).__init__(orientation=orientation, size=size, parent=parent)
        self.set_spacing(1)
        self._set_exclusive(False)

    def _after_created(self, button, data_dict):
        if data_dict.get('type'):
            button.set_type(data_dict.get('type'))


class MCheckBoxGroup(MButtonGroupBase):
    button_class = MCheckBox
    sig_checked_changed = Signal(list)

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(MCheckBoxGroup, self).__init__(orientation=orientation, parent=parent)
        self.set_spacing(15)
        self._set_exclusive(False)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._slot_context_menu)

        self._button_group.buttonClicked[int].connect(self._slot_map_signal)
        self.set_value(-1)

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


class MRadioButtonGroup(MButtonGroupBase):
    button_class = MRadioButton
    sig_checked_changed = Signal(int)

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(MRadioButtonGroup, self).__init__(orientation=orientation, parent=parent)
        self.set_spacing(15)
        self._set_exclusive(True)
        self._button_group.buttonClicked[int].connect(functools.partial(self.setProperty, 'checked'))
        self._button_group.buttonClicked[int].connect(self.sig_checked_changed)
        self.set_checked(-1)

    def _set_checked(self, value):
        assert isinstance(value, int)
        if value != self._button_group.checkedId():
            # 更新来自代码
            button = self._button_group.button(value)
            if button:
                button.setChecked(True)
            self.sig_checked_changed.emit(value)

    def set_checked(self, value):
        self.setProperty('checked', value)


class MToolButtonGroup(MButtonGroupBase):
    button_class = MToolButton

    sig_checked_changed = Signal(int)

    def __init__(self, orientation=Qt.Horizontal, size=MView.DefaultSize, icon_only=True, checkable=False, parent=None):
        super(MToolButtonGroup, self).__init__(orientation=orientation, size=size, parent=parent)
        self.set_spacing(1)
        self._set_exclusive(True)
        self._checkable = checkable
        self._size = size
        self._icon_only = icon_only
        self._button_group.buttonClicked[int].connect(self.set_checked)
        self._button_group.buttonClicked[int].connect(self.sig_checked_changed)

    def _set_checked(self, value):
        assert isinstance(value, int)
        if value != self._button_group.checkedId():
            # 更新来自代码
            button = self._button_group.button(value)
            if button:
                button.setChecked(True)
            self.sig_checked_changed.emit(value)

    def set_checked(self, value):
        self.setProperty('checked', value)

    def _after_created(self, button, data_dict):
        button.setCheckable(self._checkable)
        button.set_icon_only(self._icon_only)
        button.set_button_size(self._size)
        if data_dict.get('icon_checked'):
            button.setProperty('icon_checked', data_dict.get('icon_checked'))
            button.setProperty('icon_unchecked', data_dict.get('icon'))
