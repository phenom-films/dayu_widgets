#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets import STATIC_FOLDERS
from dayu_widgets.MTheme import global_theme
from dayu_widgets.mixin import property_mixin, cursor_mixin
from dayu_widgets.qt import *

qss = '''
QToolButton {{
    border-radius: 2px;
    padding: 1px;
    {font_family}
    {text_font}
}}

QToolButton[icon_only=false]{{
    {text_font}
    {font_family}
    background-color: {background};
    border: 1px solid {border};
    qproperty-toolButtonStyle: ToolButtonTextBesideIcon;
}}
QToolButton[icon_only=false]:hover{{
    color: {primary_light};
    border-color: {primary_light};
}}
QToolButton[icon_only=false]:pressed{{
    color: {primary_dark};
    border-color: {primary_dark};
}}
QToolButton[icon_only=false]:checked{{
    color: {primary};
    border: 2px solid {primary};
}}

QToolButton[icon_only=true]{{
    background-color: transparent;
    qproperty-toolButtonStyle: ToolButtonIconOnly;
}}
QToolButton[icon_only=true]:disabled{{
    background-color: {background_selected};
}}
QToolButton[icon_only=true]:pressed{{
    border-color: {primary_dark};
}}
QToolButton[icon_only=true]:hover{{
    border:1px solid {primary_light};
}}
QToolButton[icon_only=true]:checked{{
    border:1px solid {primary};
}}

QToolButton[combine=horizontal]{{
    border-radius: 0;
}}
QToolButton[combine=vertical]{{
    border-radius: 0;
}}


QToolButton[button_size=default]{{
    min-height: {default_size}px;
    max-height: {default_size}px;
    qproperty-iconSize: {default_icon_size}px {default_icon_size}px;
}}
QToolButton[button_size=large]{{
    font-size:16px;
    min-height: {large_size}px;
    max-height: {large_size}px;
    qproperty-iconSize: {large_icon_size}px {large_icon_size}px;
}}
QToolButton[button_size=small]{{
    min-height: {small_size}px;
    max-height: {small_size}px;
    qproperty-iconSize: {small_icon_size}px {small_icon_size}px;
}}
QToolButton[button_size=tiny]{{
    min-height: {tiny_size}px;
    max-height: {tiny_size}px;
    qproperty-iconSize: {tiny_icon_size}px {tiny_icon_size}px;
}}

QToolButton[button_size=default][icon_only=true]{{
    min-width: {default_size}px;
    max-width: {default_size}px;
}}
QToolButton[button_size=large][icon_only=true]{{
    min-width: {large_size}px;
    max-width: {large_size}px;
}}
QToolButton[button_size=small][icon_only=true]{{
    min-width: {small_size}px;
    max-width: {small_size}px;
}}
QToolButton[button_size=tiny][icon_only=true]{{
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
@cursor_mixin
class MToolButton(QToolButton):
    def __init__(self, icon=None, icon_checked=None, size=None, checkable=False, icon_only=True, parent=None):
        super(MToolButton, self).__init__(parent=parent)
        self.setProperty('icon_unchecked', icon)
        self.setProperty('icon_checked', icon_checked or icon)
        self.setAutoRaise(True)
        self.slot_polish_icon()
        self.toggled.connect(self.slot_polish_icon)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setStyleSheet(qss)
        self.setCheckable(checkable)
        self.set_button_size(size or MView.DefaultSize)
        self.set_icon_only(icon_only)

    @Slot(bool)
    def slot_polish_icon(self, checked=None):
        icon = self.property('icon_checked') if self.isChecked() else self.property('icon_unchecked')
        if icon:
            self.setIcon(icon)

    def _set_icon_only(self, value):
        self.style().polish(self)

    def set_icon_only(self, value):
        self.setProperty('icon_only', value)

    def _set_button_size(self, value):
        self.style().polish(self)

    def set_button_size(self, value):
        self.setProperty('button_size', value)
