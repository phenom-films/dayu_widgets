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
QLabel{{
    padding: 2px;
}}
QLabel[type=main_head]{{
    {main_head_font}
    {font_family}
}}
QLabel[type=sub_head]{{
    {sub_head_font}
    {font_family}
}}
QLabel[type=small_head]{{
    {small_head_font}
    {font_family}
}}
QLabel[type=text]{{
    {text_font}
    {font_family}
}}
QLabel[type=help]{{
    {help_font}
    {font_family}
}}

QLabel[link=true]{{
    color: {primary};
}}
QLabel[link=true]:hover{{
    color: {primary_light};
}}
QLabel[link=true]:pressed{{
    color: {primary_dark};
}}

QLabel[error=true]{{
    color: {error_light};
}}

QLabel:disabled{{
    {disabled_font}
    {font_family}
}}
'''.format(**global_theme)


@property_mixin
class MLabel(QLabel):
    '''
    自定义 props:
        type: enum
        link: bool
    '''
    MainHeadType = 'main_head'
    SubHeadType = 'sub_head'
    SmallHeadType = 'small_head'
    TextType = 'text'
    HelpType = 'help'

    def __init__(self, text='', type=None, link=False, parent=None, flags=0):
        super(MLabel, self).__init__(text, parent, flags)
        self.setProperty('type', type or MLabel.TextType)
        self.setTextInteractionFlags(Qt.TextBrowserInteraction | Qt.LinksAccessibleByMouse)
        self.setStyleSheet(qss)
        self.set_link(link)

    def _set_link(self, value):
        self.setCursor(Qt.PointingHandCursor if value else Qt.ArrowCursor)
        self.style().polish(self)

    def set_link(self, value):
        self.setProperty('link', value)
