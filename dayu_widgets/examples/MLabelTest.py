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
from dayu_widgets.MPushButton import MPushButton
from dayu_widgets.mixin import theme_mixin
from dayu_widgets.qt import *


@theme_mixin
class MLabelTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MLabelTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        div1 = MLabel(text='Default')
        div2 = MLabel(text='Disabled')
        div2.setEnabled(False)

        grid_lay = QGridLayout()
        data_list = [
            (MLabel.H1Type, u'主标题', 'H1 Type', True, False),
            (MLabel.H2Type, u'次级标题', 'H2 Type', True, False),
            (MLabel.H3Type, u'小标题', 'H3 Type', True, False),
            (MLabel.TextType, u'正文', 'Text Type', True, False),
            (MLabel.HelpType, u'辅助文字', 'Help Type', True, False),
        ]
        for row, data in enumerate(data_list):
            type, title1, title2, link1, link2 = data
            grid_lay.addWidget(MLabel(text=title1, type=type, link=link1), row, 0)
            grid_lay.addWidget(MLabel(text=title1, type=type, link=link2), row, 1)
            grid_lay.addWidget(MLabel(text=title2, type=type, link=link1), row, 2)
            grid_lay.addWidget(MLabel(text=title2, type=type, link=link2), row, 3)

        data_bind_label = MLabel(type=MLabel.H3Type)
        self.register_field('show_text', 'Guess')
        self.register_field('is_link', True)
        self.bind('show_text', data_bind_label, 'text')
        self.bind('is_link', data_bind_label, 'link')

        button = MPushButton(text='Random An Animal', type=MPushButton.PrimaryType)
        button.clicked.connect(self.slot_change_text)
        link_button = MPushButton(text='Link', type=MPushButton.PrimaryType)
        link_button.clicked.connect(self.slot_link_text)

        lay_elide = QVBoxLayout()
        label_none = MLabel('This is a elide NONE mode label. Ellipsis should NOT appear in the text.')
        label_left = MLabel(
            'This is a elide LEFT mode label. The ellipsis should appear at the beginning of the text. xiao mao xiao gou xiao ci wei')
        label_left.set_elide_mode(Qt.ElideLeft)
        label_middle = MLabel(
            'This is a elide MIDDLE mode label. The ellipsis should appear in the middle of the text. xiao mao xiao gou xiao ci wei')
        label_middle.set_elide_mode(Qt.ElideMiddle)
        label_right = MLabel(
            'This is a elide RIGHT mode label. The ellipsis should appear at the end of the text. xiao mao xiao gou xiao ci wei')
        label_right.set_elide_mode(Qt.ElideRight)
        lay_elide.addWidget(label_none)
        lay_elide.addWidget(label_left)
        lay_elide.addWidget(label_middle)
        lay_elide.addWidget(label_right)

        main_lay = QVBoxLayout()
        main_lay.addWidget(div1)
        main_lay.addWidget(div2)
        main_lay.addWidget(MDivider('different type'))
        main_lay.addLayout(grid_lay)
        main_lay.addWidget(MDivider('data bind'))
        main_lay.addWidget(data_bind_label)
        main_lay.addWidget(button)
        main_lay.addWidget(link_button)
        main_lay.addWidget(MDivider('elide mode'))
        main_lay.addLayout(lay_elide)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_change_text(self):
        import random
        self.set_field('show_text', random.choice(['Dog', 'Cat', 'Rabbit', 'Cow']))

    def slot_link_text(self):
        self.set_field('is_link', not self.field('is_link'))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MLabelTest()
    test.show()
    sys.exit(app.exec_())
