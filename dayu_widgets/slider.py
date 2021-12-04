#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
"""MSlider"""
# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from dayu_widgets.qt import QSlider
from dayu_widgets.qt import QToolTip
from dayu_widgets.qt import Qt


class MSlider(QSlider):
    """
    A Slider component for displaying current value and intervals in range.

    MSlider just apply qss for QSlider.
    """

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(MSlider, self).__init__(orientation, parent=parent)
        self._show_text_when_move = True

    def disable_show_text(self):
        self._show_text_when_move = False

    def mouseMoveEvent(self, event):
        """Override the mouseMoveEvent to show current value as a tooltip."""
        if self._show_text_when_move:
            QToolTip.showText(event.globalPos(), str(self.value()), self)
        return super(MSlider, self).mouseMoveEvent(event)
