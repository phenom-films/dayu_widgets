#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets import STATIC_FOLDERS
from dayu_widgets.MTheme import global_theme
from dayu_widgets.mixin import cursor_mixin
from qt import *

qss = '''
QRadioButton {{
    spacing: 4px;
    {text_font}
    {font_family}
}}
QRadioButton:disabled {{
    color: {disabled};
}}

QRadioButton::indicator{{
    width: 14px;
    height: 14px;
    border-radius: 8px;
    border: 1px solid {border};
    background-color: white;
}}
QRadioButton::indicator:disabled{{
    border: 1px solid {border};
    background-color: {background_selected};
}}

QRadioButton::indicator:hover{{
    border: 1px solid {primary_light};
    background-color: white;
}}

QRadioButton::indicator:checked{{
    background-color: {primary};
    image: url(circle.svg);
}}

QRadioButton::indicator:checked:disabled{{
    background-color: {disabled};
}}
'''.format(**global_theme)
qss = qss.replace('url(', 'url({}/'.format(STATIC_FOLDERS[0].replace('\\', '/')))


@cursor_mixin
class MRadioButton(QRadioButton):
    def __init__(self, text='', parent=None):
        super(MRadioButton, self).__init__(text=text, parent=parent)
        self.setStyleSheet(qss)
