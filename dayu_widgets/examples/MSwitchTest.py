#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MSwitch import MSwitch
from dayu_widgets.MTheme import dayu_theme
from dayu_widgets.mixin import theme_mixin
from dayu_widgets.qt import *


@theme_mixin
class MSwitchTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MSwitchTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        check_box_1 = MSwitch()
        check_box_1.setChecked(True)
        check_box_2 = MSwitch()
        check_box_3 = MSwitch()
        check_box_3.setEnabled(False)
        lay = QHBoxLayout()
        lay.addWidget(check_box_1)
        lay.addWidget(check_box_2)
        lay.addWidget(check_box_3)

        size_lay = QVBoxLayout()
        size_list = [('Huge', dayu_theme.size.huge),
                     ('Large', dayu_theme.size.large),
                     ('Medium', dayu_theme.size.medium),
                     ('Small', dayu_theme.size.small),
                     ('Tiny', dayu_theme.size.tiny)]
        for label, size in size_list:
            lay2 = QHBoxLayout()
            lay2.addWidget(MLabel(label))
            lay2.addWidget(MSwitch(size=size))
            size_lay.addLayout(lay2)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('Basic'))
        main_lay.addLayout(lay)
        main_lay.addWidget(MDivider('different size'))
        main_lay.addLayout(size_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MSwitchTest()
    test.show()
    sys.exit(app.exec_())
