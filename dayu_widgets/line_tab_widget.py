#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
"""MLineTabWidget"""

from dayu_widgets.button_group import MButtonGroupBase
from dayu_widgets.divider import MDivider
from dayu_widgets.qt import Signal, QWidget, Property, Qt, QHBoxLayout, QVBoxLayout
from dayu_widgets.stacked_widget import MStackedWidget
from dayu_widgets.tool_button import MToolButton


class MUnderlineButton(MToolButton):
    """MUnderlineButton"""

    def __init__(self, parent=None):
        super(MUnderlineButton, self).__init__(parent)
        self.setCheckable(True)


class MUnderlineButtonGroup(MButtonGroupBase):
    """MUnderlineButtonGroup"""
    sig_checked_changed = Signal(int)

    def __init__(self, parent=None):
        super(MUnderlineButtonGroup, self).__init__(parent=parent)
        self.set_spacing(1)
        self._button_group.setExclusive(True)
        self._button_group.buttonClicked[int].connect(self.sig_checked_changed)

    def create_button(self, data_dict):
        button = MUnderlineButton(parent=self)
        if data_dict.get('svg'):
            button.svg(data_dict.get('svg'))
        if data_dict.get('text'):
            if data_dict.get('svg') or data_dict.get('icon'):
                button.text_beside_icon()
            else:
                button.text_only()
        else:
            button.icon_only()
        return button

    def set_dayu_checked(self, value):
        """Set current checked button's id"""
        button = self._button_group.button(value)
        button.setChecked(True)
        self.sig_checked_changed.emit(value)

    def get_dayu_checked(self):
        """Get current checked button's id"""
        return self._button_group.checkedId()

    dayu_checked = Property(int, get_dayu_checked, set_dayu_checked, notify=sig_checked_changed)


class MLineTabWidget(QWidget):
    """MLineTabWidget"""

    def __init__(self, alignment=Qt.AlignCenter, parent=None):
        super(MLineTabWidget, self).__init__(parent=parent)
        self.tool_button_group = MUnderlineButtonGroup()
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
        """Add a tab"""
        self.stack_widget.addWidget(widget)
        self.tool_button_group.add_button(data_dict, self.stack_widget.count() - 1)
