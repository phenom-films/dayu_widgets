#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import *
from dayu_widgets.MButton import MButton
from dayu_widgets.MButtonGroup import MButtonGroup
from dayu_widgets.MDivider import MDivider

class MButtonTest(QWidget):
    def __init__(self, parent=None):
        super(MButtonTest, self).__init__(parent)
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
        button_default.setDisabled(True)
        button_circle = MButton(button_icon='icon-delete', type='primary', text='Delete')
        button_circle2 = MButton(button_icon='icon-search', type='primary', text='Search')
        button_circle3 = MButton(button_icon='icon-browser', type='primary', text='Browser')
        button_circle4 = MButton(button_icon='icon-up', type='primary', text='Up')

        button_group_h = MButtonGroup()
        button_group_h.add_button(button_circle)
        button_group_h.add_button(button_circle2)
        button_group_h.add_button(button_circle3)
        button_group_h.add_button(button_circle4)


        button_v1 = MButton(button_icon='icon-delete', type='info',text='Delete')
        button_v2 = MButton(button_icon='icon-search', type='info',text='Search')
        button_v3 = MButton(button_icon='icon-browser',type='info', text='Browser')
        button_v4 = MButton(button_icon='icon-up', type='info',text='Up')
        button_group_v = MButtonGroup(orientation=Qt.Vertical)
        button_group_v.add_button(button_v1)
        button_group_v.add_button(button_v2)
        button_group_v.add_button(button_v3)
        button_group_v.add_button(button_v4)

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

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different type'))
        main_lay.addLayout(sub_lay1)
        main_lay.addLayout(sub_lay2)
        main_lay.addWidget(MDivider('different button_size'))
        main_lay.addLayout(sub_lay3)
        main_lay.addWidget(MDivider('orientation=Qt.Horizontal'))
        main_lay.addWidget(button_group_h)
        main_lay.addWidget(MDivider('orientation=Qt.Vertical'))
        main_lay.addWidget(button_group_v)
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MButtonTest()
    test.show()
    sys.exit(app.exec_())
