#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from qt import *
from MTheme import global_theme

qss = '''
MButtonGroup[orientation=horizontal] QPushButton {{
    border-radius: 0;
    border-left: 1px solid {border};
}}
MButtonGroup[orientation=vertical] QPushButton {{
    border-radius: 0;
    border-top: 1px solid {border};
}}
'''.format(**global_theme)


@property_mixin
class MButtonGroup(QWidget):
    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(MButtonGroup, self).__init__(parent=parent)
        self._main_layout = QBoxLayout(
            QBoxLayout.LeftToRight if orientation == Qt.Horizontal else QBoxLayout.TopToBottom)
        self._main_layout.addStretch()
        self._main_layout.setSpacing(0)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._main_layout)
        self.setProperty('type', 'MButtonGroup')
        self.setProperty('orientation', 'horizontal' if orientation == Qt.Horizontal else 'vertical')
        self.setStyleSheet(qss)

    def add_button(self, button):
        button.setStyleSheet(button.styleSheet() + qss)
        self._main_layout.insertWidget(self._main_layout.count() - 1, button)
