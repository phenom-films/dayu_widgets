#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.mixin import cursor_mixin, theme_mixin
from dayu_widgets.MTheme import dayu_theme
from dayu_widgets.qt import *


@cursor_mixin
@theme_mixin
class MSpinBox(QSpinBox):
    def __init__(self, size=None, parent=None):
        super(MSpinBox, self).__init__(parent=parent)
        self.setProperty('dayu_size', size or dayu_theme.default_size)


@cursor_mixin
@theme_mixin
class MDoubleSpinBox(QDoubleSpinBox):
    def __init__(self, size=None, parent=None):
        super(MDoubleSpinBox, self).__init__(parent=parent)
        self.setProperty('dayu_size', size or dayu_theme.default_size)


@cursor_mixin
@theme_mixin
class MDateTimeEdit(QDateTimeEdit):
    def __init__(self, size=None, parent=None):
        super(MDateTimeEdit, self).__init__(parent=parent)
        self.setProperty('dayu_size', size or dayu_theme.default_size)


@cursor_mixin
@theme_mixin
class MDateEdit(QDateEdit):
    def __init__(self, size=None, parent=None):
        super(MDateEdit, self).__init__(parent=parent)
        self.setProperty('dayu_size', size or dayu_theme.default_size)


@cursor_mixin
@theme_mixin
class MTimeEdit(QTimeEdit):
    def __init__(self, size=None, parent=None):
        super(MTimeEdit, self).__init__(parent=parent)
        self.setProperty('dayu_size', size or dayu_theme.default_size)
