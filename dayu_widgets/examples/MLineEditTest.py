#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MLineEdit import MLineEdit
from dayu_widgets.qt import *


class MLineEditTest(QWidget):
    def __init__(self, parent=None):
        super(MLineEditTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        line_edit_large = MLineEdit(size=MLineEdit.LargeSize)
        line_edit_large.setPlaceholderText('Large Size')
        line_edit_default = MLineEdit()
        line_edit_default.setPlaceholderText('Default Size')
        line_edit_small = MLineEdit(size=MLineEdit.SmallSize)
        line_edit_small.setPlaceholderText('Small Size')

        line_edit_icon = MLineEdit(suffix_icon='icon-browser', text='Browser')
        line_edit_error = MLineEdit(type=MLineEdit.ErrorType, size=MLineEdit.SmallSize)
        line_edit_error.setText('waring: file d:/ddd/ccc.jpg not exists.')
        line_edit_error2 = MLineEdit(type=MLineEdit.ErrorType, size=MLineEdit.SmallSize)

        line_edit_search = MLineEdit(type=MLineEdit.SearchType, size=MLineEdit.SmallSize)
        line_edit_search_engine = MLineEdit(prefix_icon='icon-filter', type=MLineEdit.SearchEngineType, size=MLineEdit.LargeSize)
        line_edit_search_engine.sig_prefix_button_clicked.connect(self.slot_prefix_button_clicked)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different size'))
        main_lay.addWidget(line_edit_large)
        main_lay.addWidget(line_edit_default)
        main_lay.addWidget(line_edit_small)
        main_lay.addWidget(MDivider('icon'))
        main_lay.addWidget(line_edit_icon)
        main_lay.addWidget(line_edit_error)
        main_lay.addWidget(line_edit_error2)
        main_lay.addWidget(line_edit_search)
        main_lay.addWidget(line_edit_search_engine)
        main_lay.addStretch()
        self.setLayout(main_lay)

    @Slot()
    def slot_prefix_button_clicked(self):
        print 'prefix button clicked'

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MLineEditTest()
    test.show()
    sys.exit(app.exec_())
