#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

import functools

from dayu_widgets.MAvatar import MAvatar
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MTheme import dayu_theme
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.mixin import property_mixin, theme_mixin
from dayu_widgets.qt import *


@property_mixin
@theme_mixin
class MAlert(QWidget):
    '''
    自定义 props:
        text:
        type:
    '''
    InfoType = 'info'
    SuccessType = 'success'
    WarningType = 'warning'
    ErrorType = 'error'

    def __init__(self, text='', type=None, closable=False, show_icon=True, parent=None, flags=0):
        super(MAlert, self).__init__(parent, flags)
        self.setAttribute(Qt.WA_StyledBackground)
        self._icon_label = MAvatar(size=dayu_theme.size.tiny)
        self._content_label = MLabel()
        self._close_button = MToolButton(size=dayu_theme.size.tiny, icon=MIcon('close_line.svg'))
        self._close_button.clicked.connect(functools.partial(self.setVisible, False))

        self._main_lay = QHBoxLayout()
        self._main_lay.setContentsMargins(8, 8, 8, 8)
        self._main_lay.addWidget(self._icon_label)
        self._main_lay.addWidget(self._content_label)
        self._main_lay.addStretch()
        self._main_lay.addWidget(self._close_button)

        self.setLayout(self._main_lay)

        self._icon_label.setVisible(show_icon)
        self._close_button.setVisible(closable)
        self.set_type(type or MAlert.InfoType)
        self.set_text(text)

    def _set_text(self, value):
        self._content_label.setProperty('text', value)
        self.setVisible(bool(value))

    def set_text(self, value):
        self.setProperty('text', value)

    def _set_type(self, value):
        self._icon_label.set_image(
            MPixmap('{}_fill.svg'.format(self.property('type')), dayu_theme.color.get(self.property('type'))))
        self.polish()

    def set_type(self, value):
        self.setProperty('type', value or MAlert.InfoType)
