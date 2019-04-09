#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.4
# Email : muyanru345@163.com
###################################################################


from dayu_widgets.mixin import stacked_animation_mixin
from dayu_widgets.qt import *


@stacked_animation_mixin
class MStackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        super(MStackedWidget, self).__init__(parent)
