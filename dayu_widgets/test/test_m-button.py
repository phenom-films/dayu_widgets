#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import *
from dayu_widgets.MButton import MButton


class MDividerTest(QWidget):
    def __init__(self, parent=None):
        super(MDividerTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        button1 = MButton(text='Default')
        button2 = MButton(text='Primary', type='primary')
        button3 = MButton(text='Info', type='info')
        button4 = MButton(text='Success', type='success')
        button5 = MButton(text='Warning', type='warning')
        button6 = MButton(text='Error', type='error')
        button_large = MButton(text='Large', type='primary', button_size='large')
        button_default = MButton(text='Default', type='primary')
        button_small = MButton(text='Small', type='warning', button_size='small')
        button_circle = MButton(button_icon='icon-delete', type='primary', text='Delete')
        button_circle2 = MButton(button_icon='icon-delete', type='primary', text='Delete')
        button_circle3 = MButton(button_icon='icon-delete', type='primary', text='Delete')
        button_circle4 = MButton(button_icon='icon-delete', type='primary', text='Delete')
        button_circle4.setDisabled(True)
        sub_lay1 = QHBoxLayout()
        sub_lay1.addWidget(button1)
        sub_lay1.addWidget(button2)
        sub_lay1.addWidget(button3)
        sub_lay1.addStretch()
        sub_lay2 = QHBoxLayout()
        sub_lay2.addWidget(button4)
        sub_lay2.addWidget(button5)
        sub_lay2.addWidget(button6)
        sub_lay3 = QHBoxLayout()
        sub_lay3.addWidget(button_large)
        sub_lay3.addWidget(button_default)
        sub_lay3.addWidget(button_small)

        sub_lay4 = QHBoxLayout()
        sub_lay4.addWidget(button_circle)
        sub_lay4.addWidget(button_circle2)
        sub_lay4.addWidget(button_circle3)
        sub_lay4.addWidget(button_circle4)
        main_lay = QVBoxLayout()
        main_lay.addLayout(sub_lay1)
        main_lay.addLayout(sub_lay2)
        main_lay.addLayout(sub_lay3)
        main_lay.addLayout(sub_lay4)
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MDividerTest()
    test.show()
    sys.exit(app.exec_())
