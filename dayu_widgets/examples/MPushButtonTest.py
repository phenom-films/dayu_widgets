#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MPushButton import MPushButton
from dayu_widgets.qt import *


class MPushButtonTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MPushButtonTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        button1 = MPushButton(text='Default')
        button2 = MPushButton(text='Primary', type=MPushButton.PrimaryType)
        button3 = MPushButton(text='Info', type=MPushButton.InfoType)
        button4 = MPushButton(text='Success', type=MPushButton.SuccessType)
        button5 = MPushButton(text='Warning', type=MPushButton.WarningType)
        button6 = MPushButton(text='Error', type=MPushButton.ErrorType)
        button7 = MPushButton(text='With Icon', icon=MIcon('trash_fill.svg'), type=MPushButton.DefaultType)
        button7.setCheckable(True)
        button_large = MPushButton(text='Large', type=MPushButton.PrimaryType, size=MView.LargeSize)
        button_default = MPushButton(text='Default', type=MPushButton.PrimaryType)
        button_small = MPushButton(text='Small', type=MPushButton.WarningType, size=MView.SmallSize)
        button_default.setDisabled(True)

        self.register_field('button_type', MPushButton.PrimaryType)
        button_bind = MPushButton()
        button_bind.clicked.connect(self.slot_change_button_type)
        self.bind('button_type', button_bind, 'type')
        self.bind('button_type', button_bind, 'text')

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
        main_lay.addWidget(MDivider('data bind: click button to change type'))
        main_lay.addWidget(button_bind)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_change_button_type(self):
        import random
        self.set_field('button_type', random.choice(
            [MPushButton.DefaultType, MPushButton.PrimaryType, MPushButton.SuccessType, MPushButton.InfoType,
             MPushButton.WarningType, MPushButton.ErrorType]))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MPushButtonTest()
    test.show()
    sys.exit(app.exec_())
