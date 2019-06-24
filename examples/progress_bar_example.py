#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.progress_bar import MProgressBar
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.qt import QWidget, Qt, QFormLayout, QVBoxLayout


class ProgressBarExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ProgressBarExample, self).__init__(parent)
        self.setWindowTitle('Examples for MProgressBar')
        self._init_ui()

    def _init_ui(self):
        progress_1 = MProgressBar()
        progress_1.setValue(1)
        progress_1.setAlignment(Qt.AlignCenter)
        progress_2 = MProgressBar()
        progress_2.setValue(80)

        progress_normal = MProgressBar()
        progress_normal.setValue(30)
        progress_success = MProgressBar(status=MProgressBar.SuccessStatus)
        progress_success.setValue(100)
        progress_error = MProgressBar(status=MProgressBar.ErrorStatus)
        progress_error.setValue(50)
        form_lay = QFormLayout()
        form_lay.addRow('Primary:', progress_normal)
        form_lay.addRow('Success:', progress_success)
        form_lay.addRow('Error:', progress_error)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('Basic'))

        main_lay.addWidget(progress_1)
        main_lay.addWidget(progress_2)
        main_lay.addWidget(MDivider('different type'))
        main_lay.addLayout(form_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication
    app = QApplication(sys.argv)
    test = ProgressBarExample()
    from dayu_widgets import dayu_theme

    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
