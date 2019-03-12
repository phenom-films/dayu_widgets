#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MProgressBar import MProgress
from dayu_widgets.qt import *


class MProgressBarTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MProgressBarTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        progress_1 = MProgress()
        progress_1.setValue(10)
        progress_1.setAlignment(Qt.AlignCenter)
        progress_2 = MProgress()
        progress_2.setValue(80)

        progress_normal = MProgress()
        progress_normal.setValue(30)
        progress_success = MProgress(status=MProgress.SuccessStatus)
        progress_success.setValue(100)
        progress_error = MProgress(status=MProgress.ErrorStatus)
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

    def slot_change_text(self):
        import random
        self.set_field('show_text', random.choice(['Dog', 'Cat', 'Rabbit', 'Cow']))

    def slot_link_text(self):
        self.set_field('is_link', not self.field('is_link'))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MProgressBarTest()
    test.show()
    sys.exit(app.exec_())
