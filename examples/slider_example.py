#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

import functools

from dayu_widgets.spin_box import MSpinBox
from dayu_widgets.MButtonGroup import MPushButtonGroup
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.slider import MSlider
from dayu_widgets.qt import QWidget, QVBoxLayout, Qt, QHBoxLayout


class SliderExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(SliderExample, self).__init__(parent)
        self.setWindowTitle('Examples for MSlider')
        self._init_ui()

    def _init_ui(self):
        self.register_field('percent', 20)
        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different orientation'))
        for orn in [Qt.Horizontal, Qt.Vertical]:
            line_edit_hor = MSlider(orn)
            line_edit_hor.setRange(1, 100)
            self.bind('percent', line_edit_hor, 'value')
            lay = QVBoxLayout()
            lay.addWidget(line_edit_hor)
            main_lay.addLayout(lay)
        spin_box = MSpinBox()
        spin_box.setRange(1, 100)
        self.bind('percent', spin_box, 'value', signal='valueChanged')

        lay3 = QHBoxLayout()
        button_grp = MPushButtonGroup()
        button_grp.set_button_list([
            {'text': '+', 'clicked': functools.partial(self.slot_change_value, 10)},
            {'text': '-', 'clicked': functools.partial(self.slot_change_value, -10)},
        ])
        lay3.addWidget(spin_box)
        lay3.addWidget(button_grp)
        lay3.addStretch()
        main_lay.addWidget(MDivider('data bind'))
        main_lay.addLayout(lay3)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_change_value(self, value):
        self.set_field('percent', max(0, min(self.field('percent') + value, 100)))


if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication
    app = QApplication(sys.argv)
    test = SliderExample()
    from dayu_widgets import dayu_theme
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
