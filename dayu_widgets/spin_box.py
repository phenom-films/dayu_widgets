#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
"""
Custom Stylesheet for QSpinBox, QDoubleSpinBox, QDateTimeEdit, QDateEdit, QTimeEdit.
Only add size arg for their __init__.
"""

from dayu_widgets.mixin import cursor_mixin
from dayu_widgets.qt import QSpinBox, QDoubleSpinBox, QDateTimeEdit, QDateEdit, QTimeEdit, Property
from dayu_widgets import dayu_theme


@cursor_mixin
class MSpinBox(QSpinBox):
    """
    MSpinBox just use stylesheet and add dayu_size. No more extend.
    Property:
        dayu_size: The height of MSpinBox
    """

    def __init__(self, parent=None):
        super(MSpinBox, self).__init__(parent=parent)
        self._dayu_size = dayu_theme.default_size

    def get_dayu_size(self):
        """
        Get the MSpinBox height
        :return: integer
        """
        return self._dayu_size

    def set_dayu_size(self, value):
        """
        Set the MSpinBox size.
        :param value: integer
        :return: None
        """
        self._dayu_size = value
        self.style().polish(self)

    dayu_size = Property(int, get_dayu_size, set_dayu_size)


@cursor_mixin
class MDoubleSpinBox(QDoubleSpinBox):
    """
    MDoubleSpinBox just use stylesheet and add dayu_size. No more extend.
    Property:
        dayu_size: The height of MDoubleSpinBox
    """

    def __init__(self, parent=None):
        super(MDoubleSpinBox, self).__init__(parent=parent)
        self._dayu_size = dayu_theme.default_size

    def get_dayu_size(self):
        """
        Get the MDoubleSpinBox height
        :return: integer
        """
        return self._dayu_size

    def set_dayu_size(self, value):
        """
        Set the MDoubleSpinBox size.
        :param value: integer
        :return: None
        """
        self._dayu_size = value
        self.style().polish(self)

    dayu_size = Property(int, get_dayu_size, set_dayu_size)


@cursor_mixin
class MDateTimeEdit(QDateTimeEdit):
    """
    MDateTimeEdit just use stylesheet and add dayu_size. No more extend.
    Property:
        dayu_size: The height of MDateTimeEdit
    """

    def __init__(self, datetime=None, parent=None):
        if datetime is None:
            super(MDateTimeEdit, self).__init__(parent=parent)
        else:
            super(MDateTimeEdit, self).__init__(datetime, parent=parent)
        self._dayu_size = dayu_theme.default_size

    def get_dayu_size(self):
        """
        Get the MDateTimeEdit height
        :return: integer
        """
        return self._dayu_size

    def set_dayu_size(self, value):
        """
        Set the MDateTimeEdit size.
        :param value: integer
        :return: None
        """
        self._dayu_size = value
        self.style().polish(self)

    dayu_size = Property(int, get_dayu_size, set_dayu_size)


@cursor_mixin
class MDateEdit(QDateEdit):
    """
    MDateEdit just use stylesheet and add dayu_size. No more extend.
    Property:
        dayu_size: The height of MDateEdit
    """

    def __init__(self, date=None, parent=None):
        if date is None:
            super(MDateEdit, self).__init__(parent=parent)
        else:
            super(MDateEdit, self).__init__(date, parent=parent)
        self._dayu_size = dayu_theme.default_size

    def get_dayu_size(self):
        """
        Get the MDateEdit height
        :return: integer
        """
        return self._dayu_size

    def set_dayu_size(self, value):
        """
        Set the MDateEdit size.
        :param value: integer
        :return: None
        """
        self._dayu_size = value
        self.style().polish(self)

    dayu_size = Property(int, get_dayu_size, set_dayu_size)


@cursor_mixin
class MTimeEdit(QTimeEdit):
    """
    MTimeEdit just use stylesheet and add dayu_size. No more extend.
    Property:
        dayu_size: The height of MTimeEdit
    """

    def __init__(self, time=None, parent=None):
        if time is None:
            super(MTimeEdit, self).__init__(parent=parent)
        else:
            super(MTimeEdit, self).__init__(time, parent=parent)
        self._dayu_size = dayu_theme.default_size

    def get_dayu_size(self):
        """
        Get the MTimeEdit height
        :return: integer
        """
        return self._dayu_size

    def set_dayu_size(self, value):
        """
        Set the MTimeEdit size.
        :param value: integer
        :return: None
        """
        self._dayu_size = value
        self.style().polish(self)

    dayu_size = Property(int, get_dayu_size, set_dayu_size)
