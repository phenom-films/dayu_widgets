#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
"""MSlider"""
from dayu_widgets.qt import QSlider, Qt, QToolTip


class MSlider(QSlider):
    """
    A Slider component for displaying current value and intervals in range.

    MSlider just apply qss for QSlider.
    """

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(MSlider, self).__init__(orientation, parent=parent)

    def mouseMoveEvent(self, event):
        """Override the mouseMoveEvent to show current value as a tooltip."""
        QToolTip.showText(event.globalPos(), str(self.value()), self)
        return super(MSlider, self).mouseMoveEvent(event)
