#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: TimmyLiang
# Date  : 2021.12
# Email : 820472580@qq.com
###################################################################
"""
Example code for MSplitter
"""
# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from Qt import QtCore
from Qt import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.splitter import MSplitter
from dayu_widgets.text_edit import MTextEdit


class SplitterExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SplitterExample, self).__init__(parent)

        main_splitter = MSplitter(QtCore.Qt.Vertical)
        main_splitter.setHandleWidth(20)

        container = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        container.setLayout(layout)
        splitter = MSplitter(QtCore.Qt.Vertical)
        splitter.addWidget(MTextEdit())
        splitter.addWidget(MTextEdit())
        splitter.addWidget(MTextEdit())
        layout.addWidget(splitter)
        main_splitter.addWidget(container)

        container = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        container.setLayout(layout)
        splitter = MSplitter()
        splitter.addWidget(MTextEdit())
        splitter.addWidget(MTextEdit())
        splitter.addWidget(MTextEdit())
        layout.addWidget(splitter)
        main_splitter.addWidget(container)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(main_splitter)
        self.setLayout(layout)

        self.resize(800, 800)


if __name__ == "__main__":
    # Import built-in modules
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test = SplitterExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
