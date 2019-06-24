#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################


from dayu_widgets.button_group import MButtonGroupBase
from dayu_widgets.divider import MDivider
from dayu_widgets.stacked_widget import MStackedWidget
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.qt import *


class MLineButtonGroup(MButtonGroupBase):
    sig_checked_changed = Signal(int)

    def __init__(self, size=None, orientation=Qt.Horizontal, parent=None):
        super(MLineButtonGroup, self).__init__(orientation=orientation, parent=parent)
        self.set_spacing(1)
        self._button_group.setExclusive(True)
        self._size = size
        self._orientation = orientation
        self._button_group.buttonClicked[int].connect(self.set_checked)
        self._button_group.buttonClicked[int].connect(self.sig_checked_changed)
        self.set_checked(-1)

    def create_button(self, data_dict):
        button = MToolButton(text=data_dict.get('text'),
                             icon=data_dict.get('icon'),
                             type=MToolButton.LineType,
                             size=data_dict.get('size') or self._size,
                             parent=self
                             )
        button.setCheckable(True)
        if data_dict.get('icon') or data_dict.get('icon_checked'):
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


class MLineTabWidget(QWidget):
    def __init__(self, alignment=Qt.AlignCenter, size=None, parent=None):
        super(MLineTabWidget, self).__init__(parent=parent)
        self.tool_button_group = MLineButtonGroup(size=size)
        self.bar_layout = QHBoxLayout()
        self.bar_layout.setContentsMargins(0, 0, 0, 0)
        if alignment == Qt.AlignCenter:
            self.bar_layout.addStretch()
            self.bar_layout.addWidget(self.tool_button_group)
            self.bar_layout.addStretch()
        elif alignment == Qt.AlignLeft:
            self.bar_layout.addWidget(self.tool_button_group)
            self.bar_layout.addStretch()
        elif alignment == Qt.AlignRight:
            self.bar_layout.addStretch()
            self.bar_layout.addWidget(self.tool_button_group)
        self.stack_widget = MStackedWidget()
        self.tool_button_group.sig_checked_changed.connect(self.stack_widget.setCurrentIndex)
        main_lay = QVBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)
        main_lay.setSpacing(0)
        main_lay.addLayout(self.bar_layout)
        main_lay.addWidget(MDivider())
        main_lay.addSpacing(5)
        main_lay.addWidget(self.stack_widget)
        self.setLayout(main_lay)

    def add_tab(self, widget, data_dict):
        self.stack_widget.addWidget(widget)
        self.tool_button_group.add_button(data_dict, self.stack_widget.count() - 1)
