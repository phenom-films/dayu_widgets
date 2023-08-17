#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3.divider import MDivider
from dayu_widgets3.field_mixin import MFieldMixin
from dayu_widgets3.progress_bar import MProgressBar
from dayu_widgets3.push_button import MPushButton


class ProgressBarExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ProgressBarExample, self).__init__(parent)
        self.setWindowTitle("Examples for MProgressBar")
        self._init_ui()

    def _init_ui(self):
        progress_1 = MProgressBar()
        progress_1.setValue(10)
        progress_1.setAlignment(QtCore.Qt.AlignCenter)
        progress_2 = MProgressBar()
        progress_2.setValue(80)

        progress_normal = MProgressBar()
        progress_normal.setValue(30)
        progress_success = MProgressBar().success()
        progress_success.setValue(100)
        progress_error = MProgressBar().error()
        progress_error.setValue(50)
        form_lay = QtWidgets.QFormLayout()
        form_lay.addRow("Primary:", progress_normal)
        form_lay.addRow("Success:", progress_success)
        form_lay.addRow("Error:", progress_error)

        self.progress_count = 0
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.slot_timeout)
        run_button = MPushButton(text="Run Something")
        run_button.clicked.connect(self.slot_run)
        self.auto_color_progress = MProgressBar().auto_color()
        auto_color_lay = QtWidgets.QVBoxLayout()
        auto_color_lay.addWidget(run_button)
        auto_color_lay.addWidget(self.auto_color_progress)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Basic"))

        main_lay.addWidget(progress_1)
        main_lay.addWidget(progress_2)
        main_lay.addWidget(MDivider("different type"))
        main_lay.addLayout(form_lay)
        main_lay.addWidget(MDivider("auto color"))
        main_lay.addLayout(auto_color_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_run(self):
        self.timer.start()
        self.auto_color_progress.setValue(0)

    def slot_timeout(self):
        if self.auto_color_progress.value() > 99:
            self.timer.stop()
        else:
            self.auto_color_progress.setValue(self.auto_color_progress.value() + 1)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets3 import dayu_theme
    from dayu_widgets3.qt import application

    with application() as app:
        test = ProgressBarExample()
        dayu_theme.apply(test)
        test.show()
