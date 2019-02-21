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
from dayu_widgets.MFieldMixin import FieldMixin


class MButtonTest(QWidget, FieldMixin):
    def __init__(self, parent=None):
        super(MButtonTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        button1 = MButton(text='Default')
        button2 = MButton(text='Primary', type=MButton.PrimaryType)
        button3 = MButton(text='Info', type=MButton.InfoType)
        button4 = MButton(text='Success', type=MButton.SuccessType)
        button5 = MButton(text='Warning', type=MButton.WarningType)
        button6 = MButton(text='Error', type=MButton.ErrorType)
        button7 = MButton(text='Icon', icon=MIcon('icon-delete.png'), type=MButton.IconType)
        button7.setCheckable(True)
        button_large = MButton(text='Large', type=MButton.PrimaryType, size=MButton.LargeSize)
        button_default = MButton(text='Default', type=MButton.PrimaryType)
        button_small = MButton(text='Small', type=MButton.WarningType, size=MButton.SmallSize)
        button_default.setDisabled(True)
        button_circle = MButton(icon=MIcon('icon-delete.png'), type=MButton.ErrorType, text='Delete')
        button_circle2 = MButton(icon=MIcon('icon-search.png'), type=MButton.PrimaryType, text='Search')
        button_circle3 = MButton(icon=MIcon('icon-browser.png'), type=MButton.PrimaryType, text='Browser')
        button_circle4 = MButton(icon=MIcon('icon-up.png'), type=MButton.PrimaryType, text='Up')

        self.register_field('button_type', MButton.PrimaryType)
        button_bind = MButton()
        button_bind.clicked.connect(self.slot_change_button_type)
        self.bind('button_type', button_bind, 'type')
        self.bind('button_type', button_bind, 'text')

        button_group_h = MButtonGroup()
        button_group_h.add_button(button_circle)
        button_group_h.add_button(button_circle2)
        button_group_h.add_button(button_circle3)
        button_group_h.add_button(button_circle4)

        button_v1 = MButton(icon=MIcon('icon-delete.png'), type=MButton.InfoType, text='Delete')
        button_v2 = MButton(icon=MIcon('icon-search.png'), type=MButton.InfoType, text='Search')
        button_v3 = MButton(icon=MIcon('icon-browser.png'), type=MButton.InfoType, text='Browser')
        button_v4 = MButton(icon=MIcon('icon-up.png'), type=MButton.InfoType, text='Up')
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
        sub_lay2.addWidget(button7)
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
        main_lay.addWidget(MDivider('data bind: click button to change type'))
        main_lay.addWidget(button_bind)

        self.setLayout(main_lay)

    def slot_change_button_type(self):
        import random
        self.set_field('button_type', random.choice([MButton.DefaultType, MButton.PrimaryType, MButton.SuccessType, MButton.InfoType, MButton.WarningType, MButton.ErrorType]))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MButtonTest()
    test.show()
    sys.exit(app.exec_())
