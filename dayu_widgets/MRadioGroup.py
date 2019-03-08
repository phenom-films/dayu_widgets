#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from qt import *
from MTheme import global_theme
from MFieldMixin import MFieldMixin
import functools

qss = '''
QRadioButton, QPushButton {{
    {text_font}
    {font_family}
}}


QPushButton#radio{{
    padding: 4px 12px;
    background-color: {background};
    border: 1px solid {border};
}}
QPushButton#radio:hover{{
    color: {primary_light};
    border-color: {primary_light};
}}
QPushButton#radio:pressed{{
    color: {primary_dark};
    border-color: {primary_dark};
}}
QPushButton#radio:checked{{
    color: {primary};
    border: 2px solid {primary};
}}
'''.format(**global_theme)


@property_mixin
class MRadioGroup(QWidget, MFieldMixin):
    '''
    props:
        checked: int
            signal: sig_value_changed

    '''
    RadioType = 'radio'
    ButtonType = 'button'
    sig_checked_changed = Signal(int)

    def __init__(self, orientation=Qt.Horizontal, type=None, parent=None):
        super(MRadioGroup, self).__init__(parent=parent)
        self._button_group = QButtonGroup(self)
        self._button_group.buttonClicked[int].connect(functools.partial(self.setProperty, 'checked'))
        self._button_group.buttonClicked[int].connect(self.sig_checked_changed)

        self._main_layout = QBoxLayout(
            QBoxLayout.LeftToRight if orientation == Qt.Horizontal else QBoxLayout.TopToBottom)
        if orientation == Qt.Horizontal:
            self._main_layout.addStretch()
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self.setProperty('type', type or MRadioGroup.RadioType)
        self.set_checked(-1)
        self.setLayout(self._main_layout)
        self.setStyleSheet(qss)

    def set_radio_list(self, button_list):
        for button in self._button_group.buttons():
            self._button_group.removeButton(button)
            self._main_layout.removeWidget(button)
            button.setVisible(False)

        button_class = QPushButton if self.property('type') == MRadioGroup.ButtonType else QRadioButton
        for index, data_dict in enumerate(button_list):
            button = button_class(self)
            button.setObjectName('radio')
            button.setCheckable(True)
            if isinstance(data_dict, basestring):
                button.setProperty('text', data_dict)
            elif isinstance(data_dict, dict):
                button.setProperty('text', data_dict.get('text'))
                if data_dict.get('icon'):
                    button.setProperty('icon', data_dict.get('icon'))
                if data_dict.get('data'):
                    button.setProperty('data', data_dict.get('data'))
            else:
                button.setProperty('text', str(data_dict))
            self._button_group.addButton(button, index)
            self._main_layout.insertWidget(self._main_layout.count() - 1, button)

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
