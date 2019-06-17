#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
"""
MAlert class.
"""
import functools

from dayu_widgets.MAvatar import MAvatar
from dayu_widgets.MLabel import MLabel
from dayu_widgets import dayu_theme
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import QWidget, QHBoxLayout, MPixmap, Qt, MIcon


@property_mixin
class MAlert(QWidget):
    """
    Alert component for feedback.

    properties:
        dayu_type: The feedback type with different color container.
        text: The feedback string showed in container.
    """
    InfoType = 'info'
    SuccessType = 'success'
    WarningType = 'warning'
    ErrorType = 'error'

    def __init__(self, parent=None, flags=0):
        super(MAlert, self).__init__(parent, flags)
        self.setAttribute(Qt.WA_StyledBackground)
        self._icon_label = MAvatar(size=dayu_theme.tiny)
        self._content_label = MLabel.help()
        self._close_button = MToolButton(type=MToolButton.IconOnlyType,
                                         size=dayu_theme.tiny, icon=MIcon('close_line.svg'))
        self._close_button.clicked.connect(functools.partial(self.setVisible, False))

        self._main_lay = QHBoxLayout()
        self._main_lay.setContentsMargins(8, 8, 8, 8)
        self._main_lay.addWidget(self._icon_label)
        self._main_lay.addWidget(self._content_label)
        self._main_lay.addStretch()
        self._main_lay.addWidget(self._close_button)

        self.setLayout(self._main_lay)

        self.set_show_icon(True)
        self.set_closeable(False)
        self.set_dayu_type('info')
        self.set_text('')

    def set_closeable(self, closeable):
        """Display the close icon button or not."""
        self._close_button.setVisible(closeable)

    def set_show_icon(self, show_icon):
        """Display the information type icon or not."""
        self._icon_label.setVisible(show_icon)

    def _set_text(self, value):
        self._content_label.setProperty('text', value)
        self.setVisible(bool(value))

    def set_text(self, value):
        """Set the feedback content."""
        if isinstance(value, basestring):
            self.setProperty('text', value)
        else:
            raise TypeError("Input argument 'value' should be string type, "
                            "but get {}".format(type(value)))

    def _set_dayu_type(self, value):
        self._icon_label.set_image(MPixmap('{}_fill.svg'.format(value),
                                           vars(dayu_theme).get(value + '_color')))
        self.style().polish(self)

    def set_dayu_type(self, value):
        """Set feedback type."""
        if value in [MAlert.InfoType, MAlert.WarningType, MAlert.ErrorType, MAlert.SuccessType]:
            self.setProperty('dayu_type', value)
        else:
            raise ValueError("Input argument 'value' should be one of "
                             "info/success/warning/error string.")
