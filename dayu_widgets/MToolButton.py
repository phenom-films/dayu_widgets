#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MTheme import dayu_theme
from dayu_widgets.mixin import property_mixin, cursor_mixin
from dayu_widgets.qt import *


@property_mixin
@cursor_mixin
class MToolButton(QToolButton):
    NormalType = 'normal'
    TaoBaoType = 'taobao'
    IconOnlyType = 'icon'
    BarType = 'bar'
    BreadcrumbType = 'breadcrumb'

    def __init__(self, text='', icon=None, icon_checked=None, type=None, size=None, parent=None):
        super(MToolButton, self).__init__(parent=parent)
        self.setProperty('icon_unchecked', icon)
        self.setProperty('icon_checked', icon_checked or icon)
        self.setAutoExclusive(False)
        self.setAutoRaise(True)
        self._polish_icon()
        self.toggled.connect(self._polish_icon)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        size = size or dayu_theme.default_size
        self.setProperty('type', type or MToolButton.NormalType)
        self.setProperty('dayu_size', size)
        if type == MToolButton.IconOnlyType:
            self.setFixedSize(QSize(size, size))
            self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        else:
            self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            self.setText(text)
        if type == MToolButton.TaoBaoType:
            self.setCheckable(True)

    @Slot(bool)
    def _polish_icon(self, checked=None):
        icon = self.property('icon_checked') if self.isChecked() else self.property('icon_unchecked')
        if icon:
            self.setIcon(icon)
