#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MTheme import dayu_theme
from dayu_widgets.mixin import property_mixin, theme_mixin
from dayu_widgets.qt import *


@property_mixin
@theme_mixin
class MAvatar(QLabel):
    '''
    自定义 props:
        image:
    '''

    def __init__(self, size=None, image=None, parent=None, flags=0):
        super(MAvatar, self).__init__(parent, flags)
        self._default_pix = MPixmap('user_fill.svg')
        size = size or dayu_theme.default_size
        self.setFixedSize(QSize(size, size))
        self.set_image(image or '')

    def _set_image(self, value):
        fixed_height = self.height()
        if value and isinstance(value, QPixmap) and (not value.isNull()):
            self.setPixmap(value.scaledToWidth(fixed_height, Qt.SmoothTransformation))
        else:
            self.setPixmap(self._default_pix.scaledToWidth(fixed_height, Qt.SmoothTransformation))

    def set_image(self, value):
        self.setProperty('image', value)
