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
}}


QPushButton[button_size=large]{{
    font-size:14px;
    padding: 1px 10px;
    height: 36px;
}}
QPushButton[button_size=default]{{
    padding: 0 12px;
    height: 32px;
}}
QPushButton[button_size=small]{{
    height: 24px;
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
    background-color: {background};
}}
'''.format(**global_theme)


class MButton(QPushButton):
    def __init__(self, text='', type='default', button_size='default', button_icon=None, parent=None):
        super(MButton, self).__init__(parent=parent)
        if button_icon:
            self.setProperty('icon', MIcon(request_file(button_icon or '' + '.png')))

        self.setProperty('text', text)
        self.setProperty('type', type)
        self.setProperty('button_size', button_size)
        self.setStyleSheet(qss)
