#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from qt import *


@property_mixin
class MButtonGroup(QWidget):
    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(MButtonGroup, self).__init__(parent=parent)
        self._main_layout = QBoxLayout(
            QBoxLayout.LeftToRight if orientation == Qt.Horizontal else QBoxLayout.TopToBottom)
        if orientation == Qt.Horizontal:
            self._main_layout.addStretch()
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self._main_layout.setSpacing(0)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._main_layout)
        self.setProperty('type', 'MButtonGroup')
        self.setProperty('orientation', 'horizontal' if orientation == Qt.Horizontal else 'vertical')

    def add_button(self, button):
        button.setProperty('combine', self.property('orientation'))
        self._main_layout.insertWidget(self._main_layout.count() - 1, button)
