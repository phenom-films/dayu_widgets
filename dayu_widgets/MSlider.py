#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from MTheme import global_theme
from . import STATIC_FOLDERS
from qt import *

qss = '''
QSlider::groove:horizontal {{
    border-radius: 3px;
    height: 4px; 
}}

QSlider::handle:horizontal {{
    background: white;
    border: 2px solid {primary};
    width: 8px;
    height: 8px;
    border-radius: 6px;
    margin: -4px 0; 
}}

QSlider::groove:vertical {{
    border-radius: 3px;
    width: 4px; 
}}

QSlider::handle:vertical {{
    background: white;
    border: 2px solid {primary};
    width: 8px;
    height: 8px;
    border-radius: 6px;
    margin: 0 -4px; 
}}

QSlider::add-page {{
    background: {border};
}}

QSlider::sub-page {{
    background: {primary};
}}

'''.format(**global_theme)
qss = qss.replace('url(', 'url({}/'.format(STATIC_FOLDERS[0].replace('\\', '/')))


class MSlider(QSlider):
    def __init__(self, orientation=None, parent=None):
        super(MSlider, self).__init__(orientation, parent=parent)
        self.setStyleSheet(qss)
