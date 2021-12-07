#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: TimmyLiang
# Date  : 2021.12
# Email : 820472580@qq.com
###################################################################
# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.mixin import property_mixin


@property_mixin
class MSplitter(QtWidgets.QSplitter):
    def __init__(self, Orientation=QtCore.Qt.Horizontal, parent=None):
        super(MSplitter, self).__init__(Orientation, parent=parent)
        self.setHandleWidth(10)
        dayu_theme.apply(self)

    def slot_splitter_click(self, next, first=True):
        size_list = self.sizes()
        prev = next - 1

        size = 100
        prev_size = size_list[prev]
        next_size = size_list[next]
        if not prev_size:
            size_list[prev] = size
            size_list[next] -= size
        elif not next_size:
            size_list[next] = size
            size_list[prev] -= size
        else:

            if first:
                size_list[next] += prev_size
                size_list[prev] = 0
            else:
                size_list[prev] += next_size
                size_list[next] = 0

        self.setSizes(size_list)

    def createHandle(self):
        count = self.count()

        orient = self.orientation()
        is_horizontal = orient is QtCore.Qt.Horizontal
        handle = QtWidgets.QSplitterHandle(orient, self)

        # NOTES: double click average size
        handle.mouseDoubleClickEvent = lambda e: self.setSizes(
            [1 for i in range(self.count())]
        )

        layout = QtWidgets.QVBoxLayout() if is_horizontal else QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        handle.setLayout(layout)

        button = QtWidgets.QToolButton(handle)
        button.setArrowType(QtCore.Qt.LeftArrow if is_horizontal else QtCore.Qt.UpArrow)
        button.clicked.connect(lambda: self.slot_splitter_click(count, True))
        layout.addWidget(button)
        button = QtWidgets.QToolButton(handle)
        arrow = QtCore.Qt.RightArrow if is_horizontal else QtCore.Qt.DownArrow
        button.setArrowType(arrow)
        button.clicked.connect(lambda: self.slot_splitter_click(count, False))
        layout.addWidget(button)

        return handle
