#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
"""
MPushButton.
"""
from dayu_widgets import dayu_theme
from dayu_widgets.mixin import cursor_mixin, focus_shadow_mixin
from dayu_widgets.qt import QPushButton, Property


@cursor_mixin
@focus_shadow_mixin
class MPushButton(QPushButton):
    """
    QPushButton.

    Property:
        dayu_size: The size of push button
        dayu_type: The type of push button.
    """
    DefaultType = 'default'
    PrimaryType = 'primary'
    SuccessType = 'success'
    WarningType = 'warning'
    DangerType = 'danger'

    def __init__(self, icon=None, text='', parent=None):
        if icon is None:
            super(MPushButton, self).__init__(text=text, parent=parent)
        else:
            super(MPushButton, self).__init__(icon=icon, text=text, parent=parent)
        self._dayu_type = MPushButton.DefaultType
        self._dayu_size = dayu_theme.default_size

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

    def get_dayu_type(self):
        """
        Get the push button type.
        :return: string.
        """
        return self._dayu_type

    def set_dayu_type(self, value):
        """
        Set the push button type.
        :return: None
        """
        if value in [MPushButton.DefaultType,
                     MPushButton.PrimaryType,
                     MPushButton.SuccessType,
                     MPushButton.WarningType,
                     MPushButton.DangerType]:
            self._dayu_type = value
        else:
            raise ValueError("Input argument 'value' should be one of "
                             "default/primary/success/warning/danger string.")
        self.style().polish(self)

    @classmethod
    def primary(cls, text='', icon=None, parent=None):
        """Create a PrimaryType push button"""
        ins = cls(text=text, icon=icon, parent=parent)
        ins.set_dayu_type(cls.PrimaryType)
        return ins

    @classmethod
    def success(cls, text='', icon=None, parent=None):
        """Create a SuccessType push button"""
        ins = cls(text=text, icon=icon, parent=parent)
        ins.set_dayu_type(cls.SuccessType)
        return ins

    @classmethod
    def warning(cls, text='', icon=None, parent=None):
        """Create a WarningType push button"""
        ins = cls(text=text, icon=icon, parent=parent)
        ins.set_dayu_type(cls.WarningType)
        return ins

    @classmethod
    def danger(cls, text='', icon=None, parent=None):
        """Create a DangerType push button"""
        ins = cls(text=text, icon=icon, parent=parent)
        ins.set_dayu_type(cls.DangerType)
        return ins

    dayu_type = Property(str, get_dayu_type, set_dayu_type)
    dayu_size = Property(int, get_dayu_size, set_dayu_size)
