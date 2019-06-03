#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets import dayu_theme
from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import *


@property_mixin
class MAvatar(QLabel):
    """
    Property:
    image: avatar image, should be QPixmap.
    """

    def __init__(self, size=None, image=None, parent=None, flags=0):
        super(MAvatar, self).__init__(parent, flags)
        self._default_pix = MPixmap('user_fill.svg')
        size = size or dayu_theme.default_size
        self.setFixedSize(QSize(size, size))
        self.set_image(image)

    def _set_image(self, value):
        self.setPixmap(value.scaledToWidth(self.height(), Qt.SmoothTransformation))

    def set_image(self, value):
        if value is None:
            self.setProperty('image', self._default_pix)
        elif isinstance(value, QPixmap) and (not value.isNull()):
            self.setProperty('image', value)
        else:
            raise TypeError("Input argument 'value' should be QPixmap or None, but get {}".format(type(value)))
