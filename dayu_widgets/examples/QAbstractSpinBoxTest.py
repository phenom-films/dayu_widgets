#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MSpinBox import qss
from dayu_widgets.MLabel import MLabel
from dayu_widgets.qt import *


class QAbstractSpinBoxTest(QWidget):
    def __init__(self, parent=None):
        super(QAbstractSpinBoxTest, self).__init__(parent)
        self.setStyleSheet(qss)
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different size'))
        class_list = [QDateTimeEdit, QDoubleSpinBox, QSpinBox]
        for cls in class_list:
            line_edit_large = cls()
            line_edit_large.setProperty('line_size', MView.LargeSize)
            line_edit_default = cls()
            line_edit_default.setProperty('line_size', MView.DefaultSize)
            line_edit_small = cls()
            line_edit_small.setProperty('line_size', MView.SmallSize)
            lay = QHBoxLayout()
            lay.addWidget(MLabel(str(cls.__name__)))
            lay.addWidget(line_edit_large)
            lay.addWidget(line_edit_default)
            lay.addWidget(line_edit_small)
            main_lay.addLayout(lay)

        main_lay.addStretch()
        self.setLayout(main_lay)

    @Slot()
    def slot_prefix_button_clicked(self):
        print 'prefix button clicked'


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = QAbstractSpinBoxTest()
    test.show()
    sys.exit(app.exec_())
