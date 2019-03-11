#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MLabel import MLabel
from dayu_widgets.qt import *
from dayu_widgets.MTheme import global_theme


qss = '''
QSlider::groove {{
    border-radius: 3px;
    height: 4px; 
}}

QSlider::handle {{
    background: white;
    border: 2px solid {primary};
    width: 8px;
    height: 8px;
    border-radius: 6px;
    margin: -4px 0; 
}}

QSlider::add-page {{
    background: {border};
}}

QSlider::sub-page {{
    background: {primary};
}}

'''.format(**global_theme)


class QAbstractSliderTest(QWidget):
    def __init__(self, parent=None):
        super(QAbstractSliderTest, self).__init__(parent)
        # self.setStyleSheet(qss)
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different size'))
        class_list = [QSlider]
        for cls in class_list:
            line_edit_large = cls(Qt.Horizontal)

            line_edit_large.setRange(1, 100)
            line_edit_large.setTickInterval(20)
            line_edit_large.setProperty('line_size', MView.LargeSize)
            lay = QHBoxLayout()
            lay.addWidget(MLabel(str(cls.__name__)))
            lay.addWidget(line_edit_large)
            main_lay.addLayout(lay)

        main_lay.addStretch()
        self.setLayout(main_lay)

    @Slot()
    def slot_prefix_button_clicked(self):
        print 'prefix button clicked'


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = QAbstractSliderTest()
    test.show()
    sys.exit(app.exec_())
