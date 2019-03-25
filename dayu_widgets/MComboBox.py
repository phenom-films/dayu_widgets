#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
import dayu_widgets.utils as utils
from dayu_widgets import dayu_theme
from dayu_widgets.mixin import property_mixin, cursor_mixin
from dayu_widgets.qt import *


@property_mixin
@cursor_mixin
class MComboBox(QComboBox):
    Separator = '/'
    sig_value_changed = Signal(list)

    def __init__(self, size=None, parent=None):
        super(MComboBox, self).__init__(parent)
        size = size or dayu_theme.default_size
        self._root_menu = None
        self._display_formatter = utils.default_formatter
        self.setProperty('dayu_size', size)
        self.setEditable(True)
        line_edit = self.lineEdit()
        line_edit.setReadOnly(True)
        line_edit.setTextMargins(4, 0, 4, 0)
        line_edit.setProperty('dayu_size', size)
        line_edit.setStyleSheet('background-color:transparent')
        line_edit.setCursor(Qt.PointingHandCursor)
        line_edit.installEventFilter(self)
        self._has_custom_view = False
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

    def setView(self, *args, **kwargs):
        self._has_custom_view = True
        super(MComboBox, self).setView(*args, **kwargs)

    def showPopup(self):
        if self._has_custom_view:
            super(MComboBox, self).showPopup()
        else:
            QComboBox.hidePopup(self)
            self._root_menu.popup(self.mapToGlobal(QPoint(0, self.height())))

    def setCurrentIndex(self, index):
        raise NotImplementedError

    def eventFilter(self, widget, event):
        if widget is self.lineEdit():
            if event.type() == QEvent.MouseButtonPress:
                self.showPopup()
        return super(MComboBox, self).eventFilter(widget, event)
