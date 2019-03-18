#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from MTheme import global_theme
from dayu_widgets import STATIC_FOLDERS
from qt import *

qss = '''
QToolButton {{
    border-radius: 2px;
    padding: 1px;
}}

QToolButton[combine=horizontal]{{
    border-radius: 0;
    border-left: 1px solid {border};
    border-top: 1px solid {border};
    border-bottom: 1px solid {border};
}}
QToolButton[combine=vertical]{{
    border-radius: 0;
    border-top: 1px solid {border};
    border-left: 1px solid {border};
    border-right: 1px solid {border};
}}

QToolButton:disabled{{
    background-color: {background_selected};
}}

QToolButton:hover{{
    border:1px solid {primary_light};
    background-color: {background_selected};
}}

QToolButton[button_size=default]{{
    min-height: {default_size}px;
    max-height: {default_size}px;
    min-width: {default_size}px;
    max-width: {default_size}px;
}}
QToolButton[button_size=large]{{
    min-height: {large_size}px;
    max-height: {large_size}px;
    min-width: {large_size}px;
    max-width: {large_size}px;
}}
QToolButton[button_size=small]{{
    min-height: {small_size}px;
    max-height: {small_size}px;
    min-width: {small_size}px;
    max-width: {small_size}px;
}}
QToolButton[button_size=tiny]{{
    min-height: {tiny_size}px;
    max-height: {tiny_size}px;
    min-width: {tiny_size}px;
    max-width: {tiny_size}px;
}}

QToolButton::menu-indicator {{
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    right: 5px;
    bottom: 5px;
    height: 10px;
    width: 10px;
    image: url(down_fill.svg);
}}

'''.format(**global_theme)

qss = qss.replace('url(', 'url({}/'.format(STATIC_FOLDERS[0].replace('\\', '/')))


@property_mixin
class MToolButton(QToolButton):
    '''
    自定义 props:
        type:
        button_size:
    '''

    def __init__(self, icon, icon_checked=None, size=None, checkable=False, parent=None):
        super(MToolButton, self).__init__(parent=parent)
        self._icon = icon
        self._icon_checked = icon_checked
        if checkable:
            self.setCheckable(checkable)
            self.toggled.connect(self.slot_check_state_changed)
            self.setChecked(True)
        self.setAutoRaise(True)
        self.setStyleSheet(qss)
        self.slot_check_state_changed(self.isChecked())
        self.set_button_size(size or MView.DefaultSize)

    @Slot(bool)
    def slot_check_state_changed(self, checked):
        self.setIcon(self._icon_checked if checked else self._icon)

    def _set_button_size(self, value):
        self.setIconSize(QSize(global_theme.get(value + '_size') * 0.9, global_theme.get(value + '_size') * 0.9))
        self.style().polish(self)

    def set_button_size(self, value):
        self.setProperty('button_size', value)

    def enterEvent(self, *args, **kwargs):
        QApplication.setOverrideCursor(Qt.PointingHandCursor if self.isEnabled() else Qt.ForbiddenCursor)
        return super(MToolButton, self).enterEvent(*args, **kwargs)

    def leaveEvent(self, *args, **kwargs):
        QApplication.restoreOverrideCursor()
        return super(MToolButton, self).leaveEvent(*args, **kwargs)
