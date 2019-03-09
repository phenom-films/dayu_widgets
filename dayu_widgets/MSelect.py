#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
import functools
from MTheme import global_theme
from MMenu import MMenu
import utils
from qt import *
from . import STATIC_FOLDERS

qss = '''
QComboBox{{
    {text_font}
    border: 1px solid {border};
    border-radius: 4px;
}}

QComboBox::drop-down {{
    subcontrol-origin: border;
    subcontrol-position: center right;
    right: 5px;
    height: 20px;
    width: 20px;
    image: url(down_line.svg);
}}

QComboBox:focus, QComboBox:hover{{
    border: 1px solid {primary};
}}

QComboBox[line_size=default]{{
    min-height: {default_size}px;
    max-height: {default_size}px;
}}
QComboBox[line_size=large]{{
    font-size: 16px;
    border-radius: 4px;
    min-height: {large_size}px;
    max-height: {large_size}px;
}}
QComboBox[line_size=large]::drop-down{{
    right: 6px;
    height: 24px;
    width: 24px;
}}
QComboBox[line_size=small]{{
    border-radius: 2px;
    min-height: {small_size}px;
    max-height: {small_size}px;
}}
QComboBox[line_size=small]::drop-down{{
    right: 4px;
    height: 18px;
    width: 18px;
}}
'''.format(**global_theme)

qss = qss.replace('url(', 'url({}/'.format(STATIC_FOLDERS[0].replace('\\', '/')))


@property_mixin
class MSelect(QComboBox):
    Separator = '/'
    sig_value_changed = Signal(list)

    def __init__(self, size=None, parent=None):
        super(MSelect, self).__init__(parent)
        size = size or MView.DefaultSize
        self._root_menu = None
        self._display_formatter = utils.default_formatter
        self.setProperty('line_size', size)
        self.setStyleSheet(qss)
        self.setCursor(Qt.PointingHandCursor)
        self.setEditable(True)
        line_edit = self.lineEdit()
        line_edit.setReadOnly(True)
        line_edit.setTextMargins(4, 0, 4, 0)
        line_edit.setStyleSheet('border-radius: 4px;')
        line_edit.setCursor(Qt.PointingHandCursor)
        line_edit.installEventFilter(self)
        self.set_value('')
        self.set_placeholder(u'请选择')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

    def set_formatter(self, func):
        self._display_formatter = func

    def set_placeholder(self, text):
        self.lineEdit().setPlaceholderText(text)

    def set_value(self, value):
        self.setProperty('value', value)

    def _set_value(self, value):
        self.lineEdit().setProperty('text', self._display_formatter(value))
        if self._root_menu:
            self._root_menu.set_value(value)

    def set_menu(self, menu):
        self._root_menu = menu
        self._root_menu.sig_value_changed.connect(self.sig_value_changed)
        self._root_menu.sig_value_changed.connect(self.set_value)

    def showPopup(self):
        QComboBox.hidePopup(self)
        self._root_menu.popup(self.mapToGlobal(QPoint(0, self.height())))

    def setCurrentIndex(self, index):
        raise NotImplementedError

    def eventFilter(self, widget, event):
        if widget is self.lineEdit():
            if event.type() == QEvent.MouseButtonPress:
                self.showPopup()
        return super(MSelect, self).eventFilter(widget, event)
