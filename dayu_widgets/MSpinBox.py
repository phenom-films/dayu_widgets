#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from MTheme import global_theme
from qt import *
from . import STATIC_FOLDERS

qss = '''
QAbstractSpinBox {{
    spacing: 4px;
    {text_font}
    {font_family}
}}
QAbstractSpinBox{{
    {text_font}
    border: 1px solid {border};
    border-radius: 3px;
}}

QAbstractSpinBox:focus{{
    border: 1px solid {primary};
}}

QAbstractSpinBox::up-button {{
    subcontrol-origin: border;
    subcontrol-position: top right;
    margin-top: 1px;
    margin-right: 1px;
    border-left: 1px solid {border};
}}

QAbstractSpinBox::up-button:hover {{
    border-left: 1px solid {primary};
}}

QAbstractSpinBox::up-arrow {{
    image: url(up_line.svg);
}}
QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off {{
    background-color: {disabled};
}}

QAbstractSpinBox::down-button {{
    subcontrol-origin: border;
    subcontrol-position: bottom right; /* position at bottom right corner */
    margin-bottom: 1px;
    margin-right: 1px;
    border-left: 1px solid {border};
    border-top: 1px solid {border};
}}

QAbstractSpinBox::down-button:hover {{
    border-left: 1px solid {primary};
}}

QAbstractSpinBox::down-arrow {{
    image: url(down_line.svg);
}}

QAbstractSpinBox::down-arrow:disabled,
QAbstractSpinBox::down-arrow:off {{
    background-color: {disabled};
}}


QAbstractSpinBox[line_size=default]{{
    min-height: {default_size}px;
    max-height: {default_size}px;
}}
QAbstractSpinBox[line_size=large]{{
    font-size: 16px;
    border-radius: 4px;
    min-height: {large_size}px;
    max-height: {large_size}px;
}}
QAbstractSpinBox[line_size=small]{{
    border-radius: 2px;
    min-height: {small_size}px;
    max-height: {small_size}px;
}}

QAbstractSpinBox[line_size=large]::up-button {{
    width: 26px;
}}
QAbstractSpinBox[line_size=default]::up-button {{
    width: 24px;
}}
QAbstractSpinBox[line_size=small]::up-button {{
    width: 20px;
}}

QAbstractSpinBox[line_size=large]::up-arrow {{
    width: 12px;
    height: 12px;
}}
QAbstractSpinBox[line_size=default]::up-arrow {{
    width: 10px;
    height: 10px;
}}
QAbstractSpinBox[line_size=small]::up-arrow {{
    width: 8px;
    height: 8px;
}}

QAbstractSpinBox[line_size=large]::down-button {{
    width: 26px;
}}
QAbstractSpinBox[line_size=default]::down-button {{
    width: 24px;
}}
QAbstractSpinBox[line_size=small]::down-button {{
    width: 20px;
}}

QAbstractSpinBox[line_size=large]::down-arrow {{
    width: 12px;
    height: 12px;
}}
QAbstractSpinBox[line_size=default]::down-arrow {{
    width: 10px;
    height: 10px;
}}
QAbstractSpinBox[line_size=small]::down-arrow {{
    width: 8px;
    height: 8px;
}}
'''.format(**global_theme)
qss = qss.replace('url(', 'url({}/'.format(STATIC_FOLDERS[0].replace('\\', '/')))


@property_mixin
class MSpinBox(QSpinBox):
    def __init__(self, size=None, parent=None):
        super(MSpinBox, self).__init__(parent=parent)
        self.setProperty('line_size', size or MView.DefaultSize)
        self.setStyleSheet(qss)

    def enterEvent(self, *args, **kwargs):
        QApplication.setOverrideCursor(Qt.PointingHandCursor if self.isEnabled() else Qt.ForbiddenCursor)
        return super(MSpinBox, self).enterEvent(*args, **kwargs)

    def leaveEvent(self, *args, **kwargs):
        QApplication.restoreOverrideCursor()
        return super(MSpinBox, self).leaveEvent(*args, **kwargs)
