#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MTheme import dayu_theme
from dayu_widgets.mixin import property_mixin, cursor_mixin, theme_mixin
from dayu_widgets.qt import *


@property_mixin
@cursor_mixin
@theme_mixin
class MSwitch(QRadioButton):
    def __init__(self, size=None, parent=None):
        super(MSwitch, self).__init__(parent)
        self.setProperty('dayu_size', size or dayu_theme.default_size)
        self.setAutoExclusive(False)

    def minimumSizeHint(self, *args, **kwargs):
        height = self.property('dayu_size') * 1.2
        return QSize(height, height / 2)
