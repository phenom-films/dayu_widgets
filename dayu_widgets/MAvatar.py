#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MTheme import global_theme
from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import *


@property_mixin
class MAvatar(QLabel):
    '''
    自定义 props:
        size:
        image:
    '''

    def __init__(self, size=None, image=None, parent=None, flags=0):
        super(MAvatar, self).__init__(parent, flags)
        self._default_pix = MPixmap('user_fill.svg')
        self.setObjectName('avatar')
        self.set_button_size(size or MView.DefaultSize)
        self.set_image(image or '')

    def _set_image(self, value):
        fixed_height = global_theme.get(self.property('button_size') + '_size')
        if value and isinstance(value, QPixmap) and (not value.isNull()):
            self.setPixmap(value.scaledToWidth(fixed_height, Qt.SmoothTransformation))
        else:
            self.setPixmap(self._default_pix.scaledToWidth(fixed_height, Qt.SmoothTransformation))

    def _set_button_size(self, value):
        fixed_height = global_theme.get((value or MView.DefaultSize) + '_size')
        self.setFixedSize(QSize(fixed_height, fixed_height))

    def set_image(self, value):
        self.setProperty('image', value)

    def set_button_size(self, value):
        self.setProperty('button_size', value)
