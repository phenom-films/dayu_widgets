#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import *
from dayu_widgets import utils


@property_mixin
class MBadge(QWidget):
    """
    Badge normally appears in proximity to notifications or user avatars with eye-catching appeal,
    typically displaying unread messages count.

    Properties:
        content: String/Number/Boolean content to show in badge.

    """

    def __init__(self, widget=None, content=0, overflow_count=99, parent=None):
        super(MBadge, self).__init__(parent)
        self._widget = widget
        self.overflow_count = overflow_count
        self._badge_button = QPushButton()
        self._badge_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self._main_lay = QGridLayout()
        self._main_lay.setContentsMargins(0, 0, 0, 0)
        if widget is not None:
            self._main_lay.addWidget(widget, 0, 0)
        self._main_lay.addWidget(self._badge_button, 0, 0, Qt.AlignTop | Qt.AlignRight)
        self.setLayout(self._main_lay)
        self.setAttribute(Qt.WA_StyledBackground)
        self.set_content(content)

    def set_content(self, value):
        if isinstance(value, (int, bool, basestring)):
            self.setProperty('content', value)
        else:
            raise TypeError(
                "Input argument 'value' should be int or bool or string type, but get {}".format(type(value)))

    def _set_content(self, value):
        # first, polish the qss
        self._badge_button.setProperty('dot', value if isinstance(value, bool) else False)
        self.style().polish(self)

        if isinstance(value, bool):
            self._badge_button.setText('')
        elif isinstance(value, int):
            self._badge_button.setText(utils.overflow_format(value, self.overflow_count))
        else:
            self._badge_button.setText(value)
        self._badge_button.setVisible(bool(value))
