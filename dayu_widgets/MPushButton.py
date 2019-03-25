#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets import dayu_theme
from dayu_widgets.mixin import property_mixin, cursor_mixin
from dayu_widgets.qt import *


@property_mixin
@cursor_mixin
class MPushButton(QPushButton):
    DefaultType = 'default'
    PrimaryType = 'primary'
    InfoType = 'info'
    SuccessType = 'success'
    WarningType = 'warning'
    ErrorType = 'error'

    def __init__(self, icon=None, text='', type=None, size=None, parent=None):
        if icon:
            super(MPushButton, self).__init__(icon=icon, text=text, parent=parent)
        else:
            super(MPushButton, self).__init__(text=text, parent=parent)
        self.setProperty('dayu_size', size or dayu_theme.default_size)
        self.setProperty('type', type or MPushButton.DefaultType)
