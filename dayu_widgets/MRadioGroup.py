#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from qt import *
from static import request_file
from MTheme import global_theme

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
class MRadioGroup(QWidget):
    sig_button_clicked = Signal(int)
    def __init__(self, orientation=Qt.Horizontal, type=None, button_size='default', parent=None):
        super(MRadioGroup, self).__init__(parent=parent)
        self._button_group = QButtonGroup(self)
        self._button_group.buttonClicked[int].connect(self.sig_button_clicked)
        self._main_layout = QBoxLayout(
            QBoxLayout.LeftToRight if orientation == Qt.Horizontal else QBoxLayout.TopToBottom)
        self._main_layout.addStretch()
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self.setProperty('type', type)
        self.setProperty('checked', -1)
        self.setProperty('button_size', button_size)
        self.setLayout(self._main_layout)
        self.setStyleSheet(qss)

    def add_radio_list(self, button_list):
        button_class = QPushButton if self.property('type') == 'button' else QRadioButton
        for index, data_dict in enumerate(button_list):
            button = button_class(self)
            button.setObjectName('radio')
            button.setCheckable(True)
            if isinstance(data_dict, basestring):
                button.setProperty('text', data_dict)
            elif isinstance(data_dict, dict):
                button.setProperty('text', data_dict.get('text'))
                if data_dict.get('icon'):
                    button.setProperty('icon', MIcon(request_file(data_dict.get('icon', '') + '.png')))
                if data_dict.get('data'):
                    button.setProperty('data', data_dict.get('data'))
            else:
                button.setProperty('text', str(data_dict))
            self._button_group.addButton(button, index)
            self._main_layout.insertWidget(self._main_layout.count() - 1, button)

    def button(self, id):
        return self._button_group.button(id)

    def checked_id(self):
        return self._button_group.checkedId()

    def checked_button(self):
        return self._button_group.checkedButton()

    def set_checked(self, value):
        button = self._button_group.button(value)
        if button:
            button.setChecked(True)
            self.sig_button_clicked.emit(value)
