#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from qt import *
from static import request_file

qss = u'''
QRadioButton, QPushButton {
    color: grey;
    font-size: 12px;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}


MRadioGroup[button_size=large]{
    font-size:14px;
    padding: 1px 10px;
    height: 36px;
}
MRadioGroup[button_size=default]{
    padding: 0 12px;
    height: 32px;
}
MRadioGroup[button_size=small]{
    height: 24px;
}

QPushButton{
    color: grey;
    padding: 4px 12px;
    background-color: #f8f8f9;
    border: 1px solid #dcdee2;
}
QPushButton:hover{
    color: #2d8cf0;
    border-color: #5cadff;
}
QPushButton:pressed{
    color: #2b85e4;
    border-color: #2b85e4;
}
QPushButton:checked{
    color: #5cadff;
    border: 2px solid #5cadff;
}
'''


@property_mixin
class MRadioGroup(QWidget):
    def __init__(self, orientation=Qt.Horizontal, type=None, parent=None):
        super(MRadioGroup, self).__init__(parent=parent)
        self._button_group = QButtonGroup(self)
        self._main_layout = QBoxLayout(
            QBoxLayout.LeftToRight if orientation == Qt.Horizontal else QBoxLayout.TopToBottom)
        self._main_layout.addStretch()
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self.setProperty('type', type)
        self.setProperty('checked', -1)
        self.setLayout(self._main_layout)
        self.setStyleSheet(qss)

    def add_radio_list(self, button_list):
        button_class = QPushButton if self.property('type') == 'button' else QRadioButton
        for index, data_dict in enumerate(button_list):
            button = button_class(self)
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
