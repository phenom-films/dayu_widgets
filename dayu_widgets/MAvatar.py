#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from MTheme import global_theme
from qt import *
qss = '''
QLabel{{
    background-color: {background_dark};
}}

'''.format(**global_theme)

@property_mixin
class MAvatar(QLabel):
    '''
    自定义 props:
        size:
        image:
    '''
    LargeSize = 'large'
    DefaultSize = 'default'
    SmallSize = 'small'

    def __init__(self, size=None, image=None, parent=None, flags=0):
        super(MAvatar, self).__init__(parent, flags)
        self.setObjectName('avatar')
        self.set_size(size or MAvatar.DefaultSize)
        self.set_image(image or 'icon-user.png')
        self.setStyleSheet(qss)

    def _set_image(self, value):
        fixed_height = global_theme.get(self.property('button_size') + '_size')
        self.setPixmap(MPixmap(value or 'icon-user.png').scaledToWidth(fixed_height, Qt.SmoothTransformation))

    def _set_button_size(self, value):
        fixed_height = global_theme.get((value or MAvatar.DefaultSize) + '_size')
        self.setFixedSize(QSize(fixed_height, fixed_height))

    def set_image(self, value):
        assert isinstance(value, basestring)
        self.setProperty('image', value)

    def set_size(self, value):
        self.setProperty('button_size', value)
