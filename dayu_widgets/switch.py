#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
"""
MSwitch
"""
from dayu_widgets import dayu_theme
from dayu_widgets.mixin import cursor_mixin
from dayu_widgets.qt import QSize, QRadioButton, Property


@cursor_mixin
class MSwitch(QRadioButton):
    """
    Switching Selector.

    Property:
        dayu_size: the size of switch widget. int
    """

    def __init__(self, parent=None):
        super(MSwitch, self).__init__(parent)
        self._dayu_size = dayu_theme.default_size
        self.setAutoExclusive(False)

    def minimumSizeHint(self):
        """
        Override the QRadioButton minimum size hint. We don't need the text space.
        :return:
        """
        height = self._dayu_size * 1.2
        return QSize(height, height / 2)

    def get_dayu_size(self):
        """
        Get the switch size.
        :return: int
        """
        return self._dayu_size

    def set_dayu_size(self, value):
        """
        Set the switch size.
        :param value: int
        :return: None
        """
        self._dayu_size = value
        self.style().polish(self)

    dayu_size = Property(int, get_dayu_size, set_dayu_size)

    def huge(self):
        """Set MSwitch to huge size"""
        self.set_dayu_size(dayu_theme.huge)
        return self

    def large(self):
        """Set MSwitch to large size"""
        self.set_dayu_size(dayu_theme.large)
        return self

    def medium(self):
        """Set MSwitch to medium size"""
        self.set_dayu_size(dayu_theme.medium)
        return self

    def small(self):
        """Set MSwitch to small size"""
        self.set_dayu_size(dayu_theme.small)
        return self

    def tiny(self):
        """Set MSwitch to tiny size"""
        self.set_dayu_size(dayu_theme.tiny)
        return self
