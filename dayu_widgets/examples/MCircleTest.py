#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

import functools

from dayu_widgets.MButtonGroup import MPushButtonGroup
from dayu_widgets.MCircle import MCircle
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MLabel import MLabel
from dayu_widgets.mixin import theme_mixin
from dayu_widgets.MTheme import dayu_theme
from dayu_widgets.qt import *


@theme_mixin
class MCircleTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MCircleTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()
        self.setLayout(main_lay)
        main_lay.addWidget(MDivider('different color/percent'))
        lay1 = QHBoxLayout()
        lay1.addWidget(MCircle(color=dayu_theme.color.get('primary'), percent=80, parent=self))
        lay1.addWidget(MCircle(color=dayu_theme.color.get('success'), percent=100, parent=self))
        lay1.addWidget(MCircle(color=dayu_theme.color.get('error'), percent=40, parent=self))
        main_lay.addLayout(lay1)
        main_lay.addWidget(MLabel(u'基础用法'))
        main_lay.addWidget(MDivider('different radius'))

        lay2 = QHBoxLayout()
        lay2.addWidget(MCircle(radius=100, percent=100, parent=self))
        lay2.addWidget(MCircle(parent=self))
        lay2.addWidget(MCircle(radius=160, parent=self))

        main_lay.addLayout(lay2)
        main_lay.addWidget(MDivider('data bind'))

        self.register_field('percent', 0)
        self.register_field('color', self.get_color)
        circle = MCircle(percent=0, parent=self)

        self.bind('percent', circle, 'percent')
        self.bind('color', circle, 'color')
        lay3 = QHBoxLayout()
        button_grp = MPushButtonGroup()
        button_grp.set_button_list([
            {'text': '+', 'clicked': functools.partial(self.slot_change_alert, 10)},
            {'text': '-', 'clicked': functools.partial(self.slot_change_alert, -10)},
        ])
        lay3.addWidget(circle)
        lay3.addWidget(button_grp)
        lay3.addStretch()
        main_lay.addLayout(lay3)

        custom_widget = QWidget()
        custom_layout = QVBoxLayout()
        custom_layout.setContentsMargins(40, 40, 40, 40)
        custom_layout.addStretch()
        custom_widget.setLayout(custom_layout)
        lab1 = MLabel(text='42,001,776', type=MLabel.H1Type)
        lab2 = MLabel(text=u'消费人群规模', type=MLabel.TextType)
        lab3 = MLabel(text=u'总占人数 75%', type=MLabel.TextType)
        lab1.setAlignment(Qt.AlignCenter)
        lab2.setAlignment(Qt.AlignCenter)
        lab3.setAlignment(Qt.AlignCenter)
        custom_layout.addWidget(lab1)
        custom_layout.addWidget(lab2)
        custom_layout.addWidget(MDivider())
        custom_layout.addWidget(lab3)
        custom_layout.addStretch()
        custom_circle = MCircle(radius=180, percent=75)
        custom_circle.set_widget(custom_widget)

        main_lay.addWidget(MDivider('custom circle'))
        main_lay.addWidget(custom_circle)
        main_lay.addStretch()

    def get_color(self):
        p = self.field('percent')
        if p < 30:
            return dayu_theme.color.get('error')
        if p < 60:
            return dayu_theme.color.get('warning')
        if p < 100:
            return dayu_theme.color.get('primary')
        return dayu_theme.color.get('success')

    def slot_change_alert(self, value):
        self.set_field('percent', max(0, min(self.field('percent') + value, 100)))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MCircleTest()
    test.show()
    sys.exit(app.exec_())
