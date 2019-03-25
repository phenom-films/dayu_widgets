#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MProgressBar import MProgressBar
from dayu_widgets.qt import *


class MProgressBarTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MProgressBarTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        progress_1 = MProgressBar()
        progress_1.setValue(10)
        progress_1.setAlignment(Qt.AlignCenter)
        progress_2 = MProgressBar()
        progress_2.setValue(80)

        progress_normal = MProgressBar()
        progress_normal.setValue(30)
        progress_success = MProgressBar(status=MProgressBar.SuccessStatus)
        progress_success.setValue(100)
        progress_error = MProgressBar(status=MProgressBar.ErrorStatus)
        progress_error.setValue(50)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('Basic'))

        main_lay.addWidget(progress_1)
        main_lay.addWidget(progress_2)
        main_lay.addWidget(MDivider('different type'))
        main_lay.addWidget(progress_normal)
        main_lay.addWidget(progress_success)
        main_lay.addWidget(progress_error)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MProgressBarTest()
    from dayu_widgets import dayu_theme
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
