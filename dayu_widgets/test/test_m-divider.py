#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import *
from dayu_widgets.MDivider import MDivider


class MDividerTest(QWidget):
    def __init__(self, parent=None):
        super(MDividerTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        div1 = MDivider()
        div2 = MDivider(text='With Text')
        div3 = MDivider(text='Left Text', alignment=Qt.AlignLeft)
        div4 = MDivider(text='Center Text', alignment=Qt.AlignCenter)
        div5 = MDivider(text='Right Text', alignment=Qt.AlignRight)
        div6 = MDivider(orientation=Qt.Vertical)
        div7 = MDivider(orientation=Qt.Vertical)
        div8 = MDivider(text=u'垂直分割线', alignment=Qt.AlignLeft)
        label1 = QLabel('Maya')
        label2 = QLabel('Nuke')
        label3 = QLabel('Houdini')
        sub_lay = QHBoxLayout()
        sub_lay.addWidget(label1)
        sub_lay.addWidget(div6)
        sub_lay.addWidget(label2)
        sub_lay.addWidget(div7)
        sub_lay.addWidget(label3)
        sub_lay.addStretch()

        main_lay = QVBoxLayout()
        main_lay.addWidget(QLabel('Steven Paul Jobs was an American entrepreneur and business magnate.'))
        main_lay.addWidget(div1)
        main_lay.addWidget(QLabel('Steven Paul Jobs was an American entrepreneur and business magnate.'))
        main_lay.addWidget(div2)
        main_lay.addWidget(QLabel('Steven Paul Jobs was an American entrepreneur and business magnate.'))
        main_lay.addWidget(div3)
        main_lay.addWidget(QLabel('Steven Paul Jobs was an American entrepreneur and business magnate.'))
        main_lay.addWidget(div4)
        main_lay.addWidget(QLabel('Steven Paul Jobs was an American entrepreneur and business magnate.'))
        main_lay.addWidget(div5)
        main_lay.addLayout(sub_lay)
        main_lay.addWidget(div8)
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MDividerTest()
    test.show()
    sys.exit(app.exec_())
