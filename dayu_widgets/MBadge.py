#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import *


@property_mixin
class MBadge(QWidget):
    '''
    props:
        text: basestring
        count: basestring
    '''

    def __init__(self, widget, dot=False, count=None, text=None, overflow_count=99, parent=None):
        super(MBadge, self).__init__(parent)
        self._widget = widget
        self.overflow_count = overflow_count
        self._badge_button = QPushButton()
        self._badge_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self._main_lay = QGridLayout()
        self._main_lay.setContentsMargins(0, 0, 0, 0)
        self._main_lay.addWidget(widget, 0, 0)
        self._main_lay.addWidget(self._badge_button, 0, 0, Qt.AlignTop | Qt.AlignRight)
        self.setLayout(self._main_lay)
        self.setAttribute(Qt.WA_StyledBackground)
        if dot:
            self.set_dot(dot)
        else:
            if text is not None:
                self.set_text(text)
            if count is not None:
                self.set_count(count)

    def _set_text(self, value):
        if not self._badge_button.property('dot'):
            self._badge_button.setText(value)

    def set_text(self, value):
        self.setProperty('text', value)

    def _set_dot(self, value):
        self._badge_button.setVisible(value)
        self._badge_button.setProperty('dot', value)

    def set_dot(self, value):
        self.setProperty('dot', value)

    def _set_count(self, value):
        self._badge_button.setVisible(value > 0)
        if not self._badge_button.property('dot'):
            self._badge_button.setText(
                str(value) if value <= self.overflow_count else '{}+'.format(self.overflow_count))

    def set_count(self, value):
        self.setProperty('count', value)
