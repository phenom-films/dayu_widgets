#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MSlider import MSlider
from dayu_widgets.qt import *


class MSliderTest(QWidget):
    def __init__(self, parent=None):
        super(MSliderTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different size'))
        for orn in [Qt.Horizontal, Qt.Vertical]:
            line_edit_hor = MSlider(orn)
            line_edit_hor.setRange(1, 100)
            line_edit_hor.setValue(20)
            line_edit_hor.setProperty('line_size', MView.LargeSize)
            lay = QVBoxLayout()
            lay.addWidget(line_edit_hor)
            main_lay.addLayout(lay)

        main_lay.addStretch()
        self.setLayout(main_lay)

    @Slot()
    def slot_prefix_button_clicked(self):
        print 'prefix button clicked'


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MSliderTest()
    test.show()
    sys.exit(app.exec_())
