#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
"""MToolButton"""

# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from Qt import QtCore
from Qt import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.mixin import cursor_mixin
from dayu_widgets.qt import MIcon


@cursor_mixin
class MToolButton(QtWidgets.QToolButton):
    """MToolButton"""

    def __init__(self, parent=None):
        super(MToolButton, self).__init__(parent=parent)
        self._dayu_svg = None
        self.setAutoExclusive(False)
        self.setAutoRaise(True)

        self._polish_icon()
        self.toggled.connect(self._polish_icon)
        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        self._dayu_size = dayu_theme.default_size

    @QtCore.Slot(bool)
    def _polish_icon(self, checked=None):
        if self._dayu_svg:
            if self.isCheckable() and self.isChecked():
                self.setIcon(MIcon(self._dayu_svg, dayu_theme.primary_color))
            else:
                self.setIcon(MIcon(self._dayu_svg))

    def enterEvent(self, event):
        """Override enter event to highlight the icon"""
        if self._dayu_svg:
            self.setIcon(MIcon(self._dayu_svg, dayu_theme.primary_color))
        return super(MToolButton, self).enterEvent(event)

    def leaveEvent(self, event):
        """Override leave event to recover the icon"""
        self._polish_icon()
        return super(MToolButton, self).leaveEvent(event)

    def get_dayu_size(self):
        """
        Get the push button height
        :return: integer
        """
        return self._dayu_size

    def set_dayu_size(self, value):
        """
        Set the avatar size.
        :param value: integer
        :return: None
        """
        self._dayu_size = value
        self.style().polish(self)
        if self.toolButtonStyle() == QtCore.Qt.ToolButtonIconOnly:
            self.setFixedSize(QtCore.QSize(self._dayu_size, self._dayu_size))

    def get_dayu_svg(self):
        """Get current svg path"""
        return self._dayu_svg

    def set_dayu_svg(self, path):
        """Set current svg path"""
        self._dayu_svg = path
        self._polish_icon()

    dayu_size = QtCore.Property(int, get_dayu_size, set_dayu_size)

    def huge(self):
        """Set MPushButton to PrimaryType"""
        self.set_dayu_size(dayu_theme.huge)
        return self

    def large(self):
        """Set MPushButton to SuccessType"""
        self.set_dayu_size(dayu_theme.large)
        return self

    def medium(self):
        """Set MPushButton to  WarningType"""
        self.set_dayu_size(dayu_theme.medium)
        return self

    def small(self):
        """Set MPushButton to DangerType"""
        self.set_dayu_size(dayu_theme.small)
        return self

    def tiny(self):
        """Set MPushButton to DangerType"""
        self.set_dayu_size(dayu_theme.tiny)
        return self

    def svg(self, path):
        """Set current svg path"""
        self.set_dayu_svg(path)
        return self

    def icon_only(self):
        """Set tool button style to icon only"""
        self.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.setFixedSize(QtCore.QSize(self._dayu_size, self._dayu_size))
        return self

    def text_only(self):
        """Set tool button style to text only"""
        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        return self

    def text_beside_icon(self):
        """Set tool button style to text beside icon"""
        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        return self

    def text_under_icon(self):
        """Set tool button style to text under icon"""
        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        return self
