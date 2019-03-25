#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import *

class MDockWidget(QDockWidget):
    def __init__(self, title='', parent=None, flags=0):
        super(MDockWidget, self).__init__(title, parent=parent, flags=flags)
