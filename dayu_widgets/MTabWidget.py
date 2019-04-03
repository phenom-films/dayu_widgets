#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.mixin import cursor_mixin
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


class MTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(MTabWidget, self).__init__(parent=parent)
        self._previous_index = 0
        self.bar = MTabBar()
        self.setTabBar(self.bar)
        self.currentChanged.connect(self.play_anim)

        self.to_show_pos_ani = QPropertyAnimation()
        self.to_show_pos_ani.setDuration(400)
        self.to_show_pos_ani.setPropertyName('pos')
        self.to_show_pos_ani.setEndValue(QPoint(0, 0))
        self.to_show_pos_ani.setEasingCurve(QEasingCurve.OutCubic)

        self.to_hide_pos_ani = QPropertyAnimation()
        self.to_hide_pos_ani.setDuration(400)
        self.to_hide_pos_ani.setPropertyName('pos')
        self.to_hide_pos_ani.setEndValue(QPoint(0, 0))
        self.to_hide_pos_ani.setEasingCurve(QEasingCurve.OutCubic)

        self.opacity_eff = QGraphicsOpacityEffect()
        self.opacity_ani = QPropertyAnimation()
        self.opacity_ani.setDuration(400)
        self.opacity_ani.setEasingCurve(QEasingCurve.InCubic)
        self.opacity_ani.setPropertyName('opacity')
        self.opacity_ani.setStartValue(0.0)
        self.opacity_ani.setEndValue(1.0)
        self.opacity_ani.setTargetObject(self.opacity_eff)

    def play_anim(self, index):
        current_widget = self.widget(index)
        if self._previous_index < index:
            self.to_show_pos_ani.setStartValue(QPoint(self.width(), 0))
            self.to_show_pos_ani.setTargetObject(current_widget)
            self.to_show_pos_ani.start()
        else:
            self.to_hide_pos_ani.setStartValue(QPoint(-self.width(), 0))
            self.to_hide_pos_ani.setTargetObject(current_widget)
            self.to_hide_pos_ani.start()
        current_widget.setGraphicsEffect(self.opacity_eff)
        self.opacity_ani.start()
        self._previous_index = index
