#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.switch import MSwitch
from dayu_widgets import dayu_theme
from dayu_widgets.qt import QWidget, QHBoxLayout, QVBoxLayout, QFormLayout


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

        size_lay = QFormLayout()
        size_lay.addRow('Huge', MSwitch().huge())
        size_lay.addRow('Large', MSwitch().large())
        size_lay.addRow('Medium', MSwitch().medium())
        size_lay.addRow('Small', MSwitch().small())
        size_lay.addRow('Tiny', MSwitch().tiny())

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
