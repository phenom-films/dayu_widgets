#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.mixin import cursor_mixin, stacked_animation_mixin
from dayu_widgets.qt import *


@cursor_mixin
class MTabBar(QTabBar):
    def __init__(self, parent=None):
        super(MTabBar, self).__init__(parent=parent)
        self.setDrawBase(False)

    def tabSizeHint(self, index):
        tab_text = self.tabText(index)
        if self.tabsClosable():
            return QSize(self.fontMetrics().width(tab_text) + 70, self.fontMetrics().height() + 20)
        else:
            return QSize(self.fontMetrics().width(tab_text) + 50, self.fontMetrics().height() + 20)


@stacked_animation_mixin
class MTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(MTabWidget, self).__init__(parent=parent)
        self.bar = MTabBar()
        self.setTabBar(self.bar)

    def disable_animation(self):
        self.currentChanged.disconnect(self._play_anim)
