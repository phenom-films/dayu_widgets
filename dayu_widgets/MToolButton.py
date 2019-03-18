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
    border: 1px solid {primary};
}}

QToolButton[combine=horizontal]{{
    border-radius: 0;
    border: 1px solid {border};
}}
QToolButton[combine=vertical]{{
    border-radius: 0;
    border: 1px solid {border};
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
class MToolButton(QToolButton):
    '''
    自定义 props:
        type:
        button_size:
    '''

    def __init__(self, icon, icon_checked=None, size=None, checkable=False, icon_only=True, parent=None):
        super(MToolButton, self).__init__(parent=parent)
        self._icon = icon
        self._icon_checked = icon_checked
        if checkable:
            self.setCheckable(checkable)
            self.toggled.connect(self.slot_check_state_changed)
            self.setChecked(True)
        self.setAutoRaise(True)
        self.slot_check_state_changed(self.isChecked())
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setStyleSheet(qss)
        self.set_button_size(size or MView.DefaultSize)
        self.set_icon_only(icon_only)

    @Slot(bool)
    def slot_check_state_changed(self, checked):
        self.setIcon(self._icon_checked if checked else self._icon)

    def _set_icon_only(self, value):
        self.style().polish(self)

    def set_icon_only(self, value):
        self.setProperty('icon_only', value)

    def _set_button_size(self, value):
        # config_size = global_theme.get(value + '_size')
        # self.setIconSize(QSize(config_size * 0.7, config_size * 0.7))
        # if self.toolButtonStyle() == Qt.ToolButtonIconOnly:
        #     self.setFixedWidth(config_size)
        self.style().polish(self)

    def set_button_size(self, value):
        self.setProperty('button_size', value)

    def minimumSizeHint(self):
        num = global_theme.get(self.property('button_size') + '_size')
        return QSize(num, num)

    def enterEvent(self, *args, **kwargs):
        QApplication.setOverrideCursor(Qt.PointingHandCursor if self.isEnabled() else Qt.ForbiddenCursor)
        return super(MToolButton, self).enterEvent(*args, **kwargs)

    def leaveEvent(self, *args, **kwargs):
        QApplication.restoreOverrideCursor()
        return super(MToolButton, self).leaveEvent(*args, **kwargs)
