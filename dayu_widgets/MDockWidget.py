#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets import STATIC_FOLDERS
from dayu_widgets.MTheme import global_theme
from dayu_widgets.qt import *

qss = '''
QDockWidget {{
    {small_head_font}
    {font_family}
    titlebar-close-icon: url(close_line.svg);
    titlebar-normal-icon: url(float.svg);

}}
QDockWidget::title {{
    background: {background_dark};
    text-align: left;
    padding-left: 10px;
}}

QDockWidget::close-button {{
    subcontrol-origin: margin;
    subcontrol-position: right center;
    right: 8px;
}}

QDockWidget::float-button {{
    subcontrol-origin: margin;
    subcontrol-position: right center;
    right: 30px;
}}
QDockWidget::close-button:hover, QDockWidget::float-button:hover {{
    border: 1px solid {primary};
}}
'''.format(**global_theme)
qss = qss.replace('url(', 'url({}/'.format(STATIC_FOLDERS[0].replace('\\', '/')))


class MDockWidget(QDockWidget):
    def __init__(self, title='', parent=None, flags=0):
        super(MDockWidget, self).__init__(title, parent=parent, flags=flags)
        self.setStyleSheet(qss)
