#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

import functools

from dayu_widgets.check_box import MCheckBox
from dayu_widgets.menu import MMenu
from dayu_widgets.push_button import MPushButton
from dayu_widgets.radio_button import MRadioButton
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import *
from dayu_widgets import dayu_theme


@property_mixin
class MButtonGroupBase(QWidget):
    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(MButtonGroupBase, self).__init__(parent=parent)
        self._main_layout = QBoxLayout(
            QBoxLayout.LeftToRight if orientation == Qt.Horizontal else QBoxLayout.TopToBottom)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._main_layout)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self._button_group = QButtonGroup()
        self._orientation = 'horizontal' if orientation == Qt.Horizontal else 'vertical'

    def set_spacing(self, value):
        self._main_layout.setSpacing(value)

    def get_button_group(self):
        return self._button_group

    def create_button(self, data_dict):
        raise NotImplementedError()

    def add_button(self, data_dict, index=None):
        if isinstance(data_dict, basestring):
            data_dict = {'text': data_dict}
        elif isinstance(data_dict, QIcon):
            data_dict = {'icon': data_dict}
        button = self.create_button(data_dict)
        button.setProperty('combine', self._orientation)
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

        if index is None:
            self._button_group.addButton(button)
        else:
            self._button_group.addButton(button, index)
        self._main_layout.insertWidget(self._main_layout.count(), button)

    def set_button_list(self, button_list):
        for button in self._button_group.buttons():
            self._button_group.removeButton(button)
            self._main_layout.removeWidget(button)
            button.setVisible(False)
        for index, data_dict in enumerate(button_list):
            self.add_button(data_dict, index)


class MPushButtonGroup(MButtonGroupBase):
    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(MPushButtonGroup, self).__init__(orientation=orientation, parent=parent)
        self.set_spacing(1)
        self._dayu_type = MPushButton.PrimaryType
        self._dayu_size = dayu_theme.default_size
        self._button_group.setExclusive(False)

    def create_button(self, data_dict):
        button = MPushButton(text=data_dict.get('text'),
                             icon=data_dict.get('icon'),
                             parent=self
                             )
        button.set_dayu_size(data_dict.get('dayu_size', self._dayu_size))
        button.set_dayu_type(data_dict.get('dayu_type', self._dayu_type))
        return button

    def get_dayu_size(self):
        return self._dayu_size

    def get_dayu_type(self):
        return self._dayu_type

    def set_dayu_size(self, value):
        self._dayu_size = value

    def set_dayu_type(self, value):
        self._dayu_type = value

    dayu_size = Property(int, get_dayu_size, set_dayu_size)
    dayu_type = Property(str, get_dayu_type, set_dayu_type)


class MCheckBoxGroup(MButtonGroupBase):
    sig_checked_changed = Signal(list)

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(MCheckBoxGroup, self).__init__(orientation=orientation, parent=parent)
        self.set_spacing(15)
        self._button_group.setExclusive(False)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._slot_context_menu)

        self._button_group.buttonClicked[int].connect(self._slot_map_signal)
        self.set_value([])

    def create_button(self, data_dict):
        button = MCheckBox(text=data_dict.get('text'),
                           parent=self
                           )
        if data_dict.get('icon'):
            button.setIcon(data_dict.get('icon'))
        return button

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
            [check_box.text() for check_box in self._button_group.buttons() if
             check_box.isChecked()])

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
    sig_checked_changed = Signal(int)

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(MRadioButtonGroup, self).__init__(orientation=orientation, parent=parent)
        self.set_spacing(15)
        self._button_group.setExclusive(True)
        self._button_group.buttonClicked[int].connect(
            functools.partial(self.setProperty, 'checked'))
        self._button_group.buttonClicked[int].connect(self.sig_checked_changed)
        self.set_checked(-1)

    def create_button(self, data_dict):
        button = MRadioButton(text=data_dict.get('text'),
                              parent=self
                              )
        if data_dict.get('icon'):
            button.setIcon(data_dict.get('icon'), )
        return button

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
    sig_checked_changed = Signal(int)

    def __init__(self, size=None, type=None, exclusive=False, orientation=Qt.Horizontal,
                 parent=None):
        super(MToolButtonGroup, self).__init__(orientation=orientation, parent=parent)
        self.set_spacing(1)
        self._button_group.setExclusive(exclusive)
        self._size = size
        self._type = type
        self._button_group.buttonClicked[int].connect(self.set_checked)
        self._button_group.buttonClicked[int].connect(self.sig_checked_changed)
        self.set_checked(-1)

    def create_button(self, data_dict):
        button = MToolButton(text=data_dict.get('text'),
                             icon=data_dict.get('icon'),
                             type=data_dict.get('type') or self._type,
                             size=data_dict.get('size') or self._size,
                             parent=self
                             )
        button.setCheckable(data_dict.get('checkable', False))
        if data_dict.get('icon_checked'):
            button.setProperty('icon_checked', data_dict.get('icon_checked'))
            button.setProperty('icon_unchecked', data_dict.get('icon'))
        return button

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
