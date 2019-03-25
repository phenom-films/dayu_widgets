#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import *


@property_mixin
class MProgressBar(QProgressBar, MFieldMixin):
    '''
    props:
        status: str

    '''
    ErrorStatus = 'error'
    NormalStatus = 'primary'
    SuccessStatus = 'success'

    def __init__(self, status=None, parent=None):
        super(MProgressBar, self).__init__(parent=parent)
        self.setAlignment(Qt.AlignCenter)
        self.set_status(status or MProgressBar.NormalStatus)

    def set_status(self, value):
        self.setProperty('status', value)

    def _set_status(self, value):
        self.style().polish(self)
