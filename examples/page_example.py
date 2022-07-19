#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from Qt import QtWidgets

# Import local modules
from dayu_widgets.divider import MDivider
from dayu_widgets.page import MPage


class PageExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PageExample, self).__init__(parent)
        self.setWindowTitle("Examples for MPage")
        self._init_ui()

    def _init_ui(self):
        page_1 = MPage()
        page_1.set_total(255)
        page_1.sig_page_changed.connect(print)

        page_2 = MPage()
        page_2.set_total(100)

        main_lay = QtWidgets.QVBoxLayout()
        self.setLayout(main_lay)
        main_lay.addWidget(MDivider())
        main_lay.addWidget(page_1)
        main_lay.addWidget(MDivider())
        main_lay.addWidget(page_2)
        main_lay.addStretch()


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = PageExample()
        dayu_theme.apply(test)
        test.show()
