#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
"""MDockWidget"""
from dayu_widgets.qt import QDockWidget,Qt


class MDockWidget(QDockWidget):
    """
    Just apply the qss. No more extend.
    """

    def __init__(self, title='', parent=None, flags=Qt.Widget):
        super(MDockWidget, self).__init__(title, parent=parent, flags=flags)
