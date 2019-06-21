#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.4
# Email : muyanru345@163.com
###################################################################
"""MStackedWidget"""

from dayu_widgets.mixin import stacked_animation_mixin
from dayu_widgets.qt import QStackedWidget


@stacked_animation_mixin
class MStackedWidget(QStackedWidget):
    """Just active animation when current index changed."""

    def __init__(self, parent=None):
        super(MStackedWidget, self).__init__(parent)
