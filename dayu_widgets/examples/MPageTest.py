#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MPage import MPage
from dayu_widgets.qt import *


class MPageTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MPageTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        page_1 = MPage()
        page_1.set_total(255)

        main_lay = QVBoxLayout()
        self.setLayout(main_lay)
        main_lay.addWidget(MDivider('different type'))
        main_lay.addWidget(page_1)
        main_lay.addStretch()


if __name__ == '__main__':
    import sys
    from dayu_widgets import dayu_theme

    app = QApplication(sys.argv)
    test = MPageTest()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
