#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.divider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.switch import MSwitch
from dayu_widgets import dayu_theme
from dayu_widgets.qt import QWidget, QHBoxLayout, QVBoxLayout


class SwitchExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(SwitchExample, self).__init__(parent)
        self.setWindowTitle('Examples for MSwitch')
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
        size_list = [
            ('Huge', MSwitch.huge),
            ('Large', MSwitch.large),
            ('Medium', MSwitch.medium),
            ('Small', MSwitch.small),
            ('Tiny', MSwitch.tiny),
        ]
        for label, cls in size_list:
            lay2 = QHBoxLayout()
            lay2.addWidget(MLabel(label))
            lay2.addWidget(cls())
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
    from dayu_widgets.qt import QApplication

    app = QApplication(sys.argv)
    test = SwitchExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
