#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import *
from dayu_widgets.MDivider import MDivider
from dayu_widgets.data_bind import FieldMixin
from dayu_widgets.MButton import MButton


class MDividerTest(QWidget, FieldMixin):
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
        div8 = MDivider(text='orientation=Qt.Vertical', alignment=Qt.AlignLeft)
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

        self.register_field('count', 0)
        self.register_field('show_text', self.computed_text)
        divider = MDivider(alignment=Qt.AlignCenter)
        button = MButton(type=MButton.PrimaryType, text='Change Divider text')
        button.clicked.connect(self.slot_change_divider_text)
        self.bind('show_text', divider, 'text')

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
        main_lay.addWidget(divider)
        main_lay.addWidget(button)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def computed_text(self):
        return 'Clicked: ' + str(self.field('count'))

    def slot_change_divider_text(self):
        self.set_field('count', self.field('count') + 1)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MDividerTest()
    test.show()
    sys.exit(app.exec_())
