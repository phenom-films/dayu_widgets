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
from dayu_widgets import dayu_theme
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

        sub_lay3 = QHBoxLayout()
        size_list = [('Huge', dayu_theme.size.huge),
                     ('Large', dayu_theme.size.large),
                     ('Medium', dayu_theme.size.medium),
                     ('Small', dayu_theme.size.small),
                     ('Tiny', dayu_theme.size.tiny)]
        for label, size in size_list:
            sub_lay3.addWidget(MPushButton(text=label, type=MPushButton.PrimaryType, size=size))

        disabled_button = MPushButton(text='Disabled')
        disabled_button.setEnabled(False)

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

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different type'))
        main_lay.addLayout(sub_lay1)
        main_lay.addLayout(sub_lay2)
        main_lay.addWidget(MDivider('different size'))
        main_lay.addLayout(sub_lay3)
        main_lay.addWidget(MDivider('disabled'))
        main_lay.addWidget(disabled_button)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MPushButtonTest()
    from dayu_widgets import dayu_theme
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
