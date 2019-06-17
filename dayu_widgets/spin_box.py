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

from dayu_widgets import dayu_theme
from dayu_widgets.mixin import cursor_mixin
from dayu_widgets.qt import QSpinBox, QDoubleSpinBox, QDateTimeEdit, QDateEdit, QTimeEdit


@cursor_mixin
class MSpinBox(QSpinBox):
    def __init__(self, size=None, parent=None):
        super(MSpinBox, self).__init__(parent=parent)
        self.setProperty('dayu_size', size or dayu_theme.default_size)


@cursor_mixin
class MDoubleSpinBox(QDoubleSpinBox):
    def __init__(self, size=None, parent=None):
        super(MDoubleSpinBox, self).__init__(parent=parent)
        self.setProperty('dayu_size', size or dayu_theme.default_size)


@cursor_mixin
class MDateTimeEdit(QDateTimeEdit):
    def __init__(self, datetime=None, size=None, parent=None):
        if datetime:
            super(MDateTimeEdit, self).__init__(datetime, parent=parent)
        else:
            super(MDateTimeEdit, self).__init__(parent=parent)
        self.setProperty('dayu_size', size or dayu_theme.default_size)


@cursor_mixin
class MDateEdit(QDateEdit):
    def __init__(self, date=None, size=None, parent=None):
        if date:
            super(MDateEdit, self).__init__(date, parent=parent)
        else:
            super(MDateEdit, self).__init__(parent=parent)
        self.setProperty('dayu_size', size or dayu_theme.default_size)


@cursor_mixin
class MTimeEdit(QTimeEdit):
    def __init__(self, time=None, size=None, parent=None):
        if time:
            super(MTimeEdit, self).__init__(time, parent=parent)
        else:
            super(MTimeEdit, self).__init__(parent=parent)
        self.setProperty('dayu_size', size or dayu_theme.default_size)
