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
from Qt import QtCore
from Qt import QtWidgets

# Import local modules
from dayu_widgets.browser import MDragFileButton
from dayu_widgets.divider import MDivider
from dayu_widgets.sequence_file import MSequenceFile


class SequenceFileExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SequenceFileExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        browser = MDragFileButton(text="Click or drag files")
        browser.set_dayu_filters([".py", "pyc", ".jpg", ".mov", "exr"])
        browser.sig_file_changed.connect(self.slot_add_file)
        self.sequence_file_1 = MSequenceFile()

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("different size"))
        main_lay.addWidget(browser)
        main_lay.addWidget(self.sequence_file_1)
        main_lay.addStretch()
        self.setLayout(main_lay)

    @QtCore.Slot(str)
    def slot_add_file(self, f):
        self.sequence_file_1.set_path(f)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = SequenceFileExample()
        dayu_theme.apply(test)
        test.show()
