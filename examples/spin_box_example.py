# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
"""
Example code for MDateTimeEdit, MDoubleSpinBox, MSpinBox, MTimeEdit, MDateEdit
"""
from dayu_widgets.spin_box import MDateTimeEdit, MDoubleSpinBox, MSpinBox, MTimeEdit, MDateEdit
from dayu_widgets.divider import MDivider
from dayu_widgets.qt import QWidget, QVBoxLayout, QHBoxLayout


class SpinBoxExample(QWidget):
    def __init__(self, parent=None):
        super(SpinBoxExample, self).__init__(parent)
        self.setWindowTitle('Examples for Spin Box')

        main_lay = QVBoxLayout()
        class_list = [MSpinBox, MDoubleSpinBox, MDateTimeEdit, MDateEdit, MTimeEdit]
        for cls in class_list:
            main_lay.addWidget(MDivider(cls.__name__))
            lay = QHBoxLayout()
            lay.addWidget(cls().large())
            lay.addWidget(cls().medium())
            lay.addWidget(cls().small())
            main_lay.addLayout(lay)

        main_lay.addWidget(MDivider('Pop Calendar Widget'))
        date_time_edit = MDateTimeEdit()
        date_time_edit.setCalendarPopup(True)
        date_edit = MDateEdit()
        date_edit.setCalendarPopup(True)
        time_edit = MTimeEdit()
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
    from dayu_widgets.qt import QApplication
    app = QApplication(sys.argv)
    test = SpinBoxExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
