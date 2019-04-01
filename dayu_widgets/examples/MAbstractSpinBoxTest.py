#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MAbstractSpinBox import MDateTimeEdit, MDoubleSpinBox, MSpinBox, MTimeEdit, MDateEdit
from dayu_widgets.MDivider import MDivider
from dayu_widgets import dayu_theme
from dayu_widgets.qt import *


class MAbstractSpinBoxTest(QWidget):
    def __init__(self, parent=None):
        super(MAbstractSpinBoxTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()
        class_list = [MSpinBox, MDoubleSpinBox, MDateTimeEdit, MDateEdit, MTimeEdit]
        size_list = [dayu_theme.large, dayu_theme.medium, dayu_theme.small]
        for cls in class_list:
            main_lay.addWidget(MDivider(cls.__name__))
            lay = QHBoxLayout()
            for size in size_list:
                line_edit_large = cls(size=size)
                lay.addWidget(line_edit_large)
            main_lay.addLayout(lay)

        main_lay.addWidget(MDivider('Pop Calendar Widget'))
        date_time_edit = MDateTimeEdit(size=dayu_theme.small)
        date_time_edit.setCalendarPopup(True)
        date_edit = MDateEdit(size=dayu_theme.small)
        date_edit.setCalendarPopup(True)
        time_edit = MTimeEdit(size=dayu_theme.small)
        time_edit.setCalendarPopup(True)
        date_lay = QHBoxLayout()
        date_lay.addWidget(date_time_edit)
        date_lay.addWidget(date_edit)
        date_lay.addWidget(time_edit)
        main_lay.addLayout(date_lay)

        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys
    from dayu_widgets import dayu_theme
    app = QApplication(sys.argv)
    test = MAbstractSpinBoxTest()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
