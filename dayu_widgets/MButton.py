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
QPushButton {{
    border-radius: 4px;
    {text_font}
    {font_family}
    color: white;
    padding: 10px;
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

QPushButton[button_size=large]{{
    font-size:14px;
    padding: 12px 20px;
}}
QPushButton[button_size=small]{{
    padding: none;
}}



'''.format(**global_theme)


class MButton(QPushButton):
    DefaultType = 'default'
    PrimaryType = 'primary'
    InfoType = 'info'
    SuccessType = 'success'
    WarningType = 'warning'
    ErrorType = 'error'
    LargeSize = 'large'
    DefaultSize = 'default'
    SmallSize = 'small'

    def __init__(self, text='', type=None, size=None, icon=None, parent=None):
        super(MButton, self).__init__(parent=parent)
        if icon:
            self.setProperty('icon', MIcon(request_file(icon or '' + '.png')))
        self.setProperty('text', text)
        self.setProperty('button_size', size)
        self.setProperty('type', type or MButton.DefaultType)
        self.setFixedHeight(global_theme.get((size or MButton.DefaultSize) + '_size'))
        self.setStyleSheet(qss)
