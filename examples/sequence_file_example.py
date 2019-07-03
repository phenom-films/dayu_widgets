#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.browser import MDragFileButton
from dayu_widgets.divider import MDivider
from dayu_widgets.sequence_file import MSequenceFile
from dayu_widgets.qt import *


class SequenceFileExample(QWidget):
    def __init__(self, parent=None):
        super(SequenceFileExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        browser = MDragFileButton(text='Click or drag files')
        browser.set_dayu_filters(['.py', 'pyc', '.jpg', '.mov', 'exr'])
        browser.sig_file_changed.connect(self.slot_add_file)
        self.sequence_file_1 = MSequenceFile()

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different size'))
        main_lay.addWidget(browser)
        main_lay.addWidget(self.sequence_file_1)
        main_lay.addStretch()
        self.setLayout(main_lay)

    @Slot(str)
    def slot_add_file(self, f):
        self.sequence_file_1.set_path(f)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = SequenceFileExample()
    from dayu_widgets import dayu_theme
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
