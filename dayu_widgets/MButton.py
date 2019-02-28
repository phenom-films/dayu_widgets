#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from MTheme import global_theme
from qt import *

qss = '''
QPushButton {{
    border-radius: 5%;
    {text_font}
    {font_family}
    color: white;
    padding: 1% 10%;
}}

QPushButton[combine=horizontal]{{
    border-radius: 0;
    border-left: 1px solid {border};
}}
QPushButton[combine=vertical]{{
    border-radius: 0;
    border-top: 1px solid {border};
}}

QPushButton[type=default]{{
    color: {content};
    background-color: {background};
    border: 1px solid {border};
}}
QPushButton[type=default]:hover{{
    color: #2d8cf0;
    border-color: #5cadff;
}}
QPushButton[type=default]:pressed{{
    color: #2b85e4;
    border-color: #2b85e4;
}}

QPushButton[type=icon]{{
    background-color: transparent;
    border: none;
}}
QPushButton[type=icon]:checked{{
    background-color: {primary};
}}
QPushButton[type=icon]:hover{{
    border: 1px solid #5cadff;
}}
QPushButton[type=icon]:pressed{{
    border: 1px solid #2b85e4;
}}


QPushButton[type=primary]{{
    background-color: {primary};
}}
QPushButton[type=primary]:hover{{
    background-color: {primary_light};

}}
QPushButton[type=primary]:pressed{{
    background-color: {primary_dark};
}}


QPushButton[type=info]{{
    background-color: {info};
}}
QPushButton[type=info]:hover{{
    background-color: {info_light};
}}
QPushButton[type=info]:pressed{{
    background-color: {info_dark};
}}


QPushButton[type=success]{{
    background-color: {success};
}}
QPushButton[type=success]:hover{{
    background-color: {success_light};
}}
QPushButton[type=success]:pressed{{
    background-color: {success_dark};
}}


QPushButton[type=warning]{{
    background-color: {warning};
}}
QPushButton[type=warning]:hover{{
    background-color: {warning_light};
}}
QPushButton[type=warning]:pressed{{
    background-color: {warning_dark};
}}


QPushButton[type=error]{{
    background-color: {error};
}}
QPushButton[type=error]:hover{{
    background-color: {error_light};
}}
QPushButton[type=error]:pressed{{
    background-color: {error_dark};
}}



QPushButton:disabled{{
    color: {disabled};
    border: 2px dashed {border};
    padding: none;
    background-color: {background};
}}

QPushButton[button_size=default]{{
    min-height: {default_size}px;
    max-height: {default_size}px;
}}
QPushButton[button_size=large]{{
    font-size:14px;
    min-height: {large_size}px;
    max-height: {large_size}px;
}}
QPushButton[button_size=small]{{
    min-height: {small_size}px;
    max-height: {small_size}px;
}}



'''.format(**global_theme)


@property_mixin
class MButton(QPushButton):
    '''
    自定义 props:
        type:
        button_size:
    '''
    DefaultType = 'default'
    IconType = 'icon'
    PrimaryType = 'primary'
    InfoType = 'info'
    SuccessType = 'success'
    WarningType = 'warning'
    ErrorType = 'error'

    def __init__(self, icon=None, text='', type=None, size=None, parent=None):
        if icon:
            super(MButton, self).__init__(icon=icon, text=text, parent=parent)
        else:
            super(MButton, self).__init__(text=text, parent=parent)
        self.set_button_size(size or MView.DefaultSize)
        self.set_type(type or MButton.DefaultType)
        self.setStyleSheet(qss)

    def _set_button_size(self, value):
        self.style().polish(self)

    def _set_type(self, value):
        if value == MButton.IconType:
            self.setText('')
            self.setFixedWidth(global_theme.get(self.property('button_size') + '_size'))
        self.style().polish(self)

    def set_type(self, value):
        self.setProperty('type', value)

    def set_button_size(self, value):
        self.setProperty('button_size', value)
