#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import *


class MSlider(QSlider):
    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(MSlider, self).__init__(orientation, parent=parent)

    def mouseMoveEvent(self, event):
        QToolTip.showText(event.globalPos(), str(self.value()), self)
        return super(MSlider, self).mouseMoveEvent(event)
