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

from dayu_widgets.avatar import MAvatar
from dayu_widgets.label import MLabel
from dayu_widgets import dayu_theme
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import QWidget, QHBoxLayout, MPixmap, Qt, MIcon, Property


@property_mixin
class MAlert(QWidget):
    """
    Alert component for feedback.

    Property:
        dayu_type: The feedback type with different color container.
        dayu_text: The feedback string showed in container.
    """
    InfoType = 'info'
    SuccessType = 'success'
    WarningType = 'warning'
    ErrorType = 'error'

    def __init__(self, text='', parent=None, flags=0):
        super(MAlert, self).__init__(parent, flags)
        self.setAttribute(Qt.WA_StyledBackground)
        self._icon_label = MAvatar()
        self._icon_label.set_dayu_size(dayu_theme.tiny)
        self._content_label = MLabel().secondary()
        self._close_button = MToolButton().svg('close_line.svg').tiny().icon_only()
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
        self._dayu_type = None
        self._dayu_text = None
        self.set_dayu_type(MAlert.InfoType)
        self.set_dayu_text(text)

    def set_closeable(self, closeable):
        """Display the close icon button or not."""
        self._close_button.setVisible(closeable)

    def set_show_icon(self, show_icon):
        """Display the information type icon or not."""
        self._icon_label.setVisible(show_icon)

    def _set_dayu_text(self):
        self._content_label.setText(self._dayu_text)
        self.setVisible(bool(self._dayu_text))

    def set_dayu_text(self, value):
        """Set the feedback content."""
        if isinstance(value, basestring):
            self._dayu_text = value
        else:
            raise TypeError("Input argument 'value' should be string type, "
                            "but get {}".format(type(value)))
        self._set_dayu_text()

    def _set_dayu_type(self):
        self._icon_label.set_dayu_image(MPixmap('{}_fill.svg'.format(self._dayu_type),
                                                vars(dayu_theme).get(self._dayu_type + '_color')))
        self.style().polish(self)

    def set_dayu_type(self, value):
        """Set feedback type."""
        if value in [MAlert.InfoType, MAlert.SuccessType, MAlert.WarningType, MAlert.ErrorType]:
            self._dayu_type = value
        else:
            raise ValueError("Input argument 'value' should be one of "
                             "info/success/warning/error string.")
        self._set_dayu_type()

    def get_dayu_type(self):
        """
        Get MAlert feedback type.
        :return: str
        """
        return self._dayu_type

    def get_dayu_text(self):
        """
        Get MAlert feedback message.
        :return: basestring
        """
        return self._dayu_text

    dayu_text = Property(unicode, get_dayu_text, set_dayu_text)
    dayu_type = Property(str, get_dayu_type, set_dayu_type)

    def info(self):
        """Set MAlert to InfoType"""
        self.set_dayu_type(MAlert.InfoType)
        return self

    def success(self):
        """Set MAlert to SuccessType"""
        self.set_dayu_type(MAlert.SuccessType)
        return self

    def warning(self):
        """Set MAlert to  WarningType"""
        self.set_dayu_type(MAlert.WarningType)
        return self

    def error(self):
        """Set MAlert to ErrorType"""
        self.set_dayu_type(MAlert.ErrorType)
        return self

    def closable(self):
        """Set MAlert closebale is True"""
        self.set_closeable(True)
        return self
