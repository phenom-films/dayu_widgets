#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets import STATIC_FOLDERS
from dayu_widgets.MTheme import global_theme
from dayu_widgets.qt import *

qss = '''
QTabWidget[type=line]::pane {{
    border-top: 1px solid {border};
    background-color: {background};
}}

QTabWidget::tab-bar {{
}}

QTabBar[type=line]::tab {{
    {text_font}
    color: #657180;
    border: 0  solid {border};
    margin-right: 4px;
}}
QTabBar[type=line]::tab:selected {{
    color: {primary};
    border-bottom: 2px solid {primary}; 
}}
QTabBar[type=line]::tab:hover {{
    color: {primary};
}}

QTabWidget[type=card]::pane {{
    border-top: 1px solid {border};
    background-color: {background};
    top: -1px;
}}
QTabBar[type=card]::tab {{
    {text_font}
    color: #657180;
    border: 1px solid {border};
    border-bottom: none;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    margin-right: 4px;
}}
QTabBar[type=card]::tab:selected {{
    background-color: {background};
    color: {primary};
}}
QTabBar[type=card]::tab:hover {{
    color: {primary};
}}
QTabBar::close-button {{
    subcontrol-origin: content;
    subcontrol-position: right center;
    margin-right: 5px;
    image: url(close_line.svg)
}}
QTabBar::close-button:hover {{
    border: 1px solid {primary};
}}

QTabBar QToolButton {{
    border-width: 2px;
}}

QTabBar QToolButton::right-arrow {{
    image: url(right_fill.svg);
}}

QTabBar QToolButton::left-arrow {{
    image: url(left_fill.svg);
}}

'''.format(**global_theme)
qss = qss.replace('url(', 'url({}/'.format(STATIC_FOLDERS[0].replace('\\', '/')))


@property_mixin
class MTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(MTabWidget, self).__init__(parent=parent)
        self.setStyleSheet(qss)
        self.bar = MTabBar()
        self.setTabBar(self.bar)

    def set_type(self, value):
        self.setProperty('type', value)
        self.bar.set_type(value)


@property_mixin
class MTabBar(QTabBar):
    def __init__(self, size=None, parent=None):
        super(MTabBar, self).__init__(parent=parent)
        self.setProperty('line_size', size or MView.DefaultSize)
        self.setDrawBase(False)
        self.setStyleSheet(qss)

    def tabSizeHint(self, index):
        tab_text = self.tabText(index)
        if self.tabsClosable():
            return QSize(self.fontMetrics().width(tab_text) + 70, self.fontMetrics().height() + 20)
        else:
            return QSize(self.fontMetrics().width(tab_text) + 50, self.fontMetrics().height() + 20)

    def set_type(self, value):
        self.setProperty('type', value)

    def _set_type(self, value):
        self.style().polish(self)
