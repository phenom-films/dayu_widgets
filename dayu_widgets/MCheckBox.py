#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.mixin import property_mixin, cursor_mixin, theme_mixin
from dayu_widgets.qt import *


@property_mixin
@cursor_mixin
@theme_mixin
class MCheckBox(QCheckBox):
    def __init__(self, text='', icon=None, parent=None):
        super(MCheckBox, self).__init__(text=text, parent=parent)
        if icon:
            self.setIcon(icon)
