#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import *
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MDivider import MDivider
from dayu_widgets.data_bind import FieldMixin
from dayu_widgets.MButton import MButton


class MLabelTest(QWidget, FieldMixin):
    def __init__(self, parent=None):
        super(MLabelTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        div1 = MLabel(text='Default')
        div2 = MLabel(text='Disabled')
        div2.setEnabled(False)

        grid_lay = QGridLayout()
        data_list = [
            (MLabel.MainHeadType, u'主标题', 'Main Head Type', True, False),
            (MLabel.SubHeadType, u'次级标题', 'Sub Head Type', True, False),
            (MLabel.SmallHeadType, u'小标题', 'Small Head Type', True, False),
            (MLabel.TextType, u'正文', 'Text Type', True, False),
            (MLabel.HelpType, u'辅助文字', 'Help Type', True, False),
        ]
        for row, data in enumerate(data_list):
            type, title1, title2, link1, link2 = data
            grid_lay.addWidget(MLabel(text=title1, type=type, link=link1), row, 0)
            grid_lay.addWidget(MLabel(text=title1, type=type, link=link2), row, 1)
            grid_lay.addWidget(MLabel(text=title2, type=type, link=link1), row, 2)
            grid_lay.addWidget(MLabel(text=title2, type=type, link=link2), row, 3)

        data_bind_label = MLabel(type=MLabel.SmallHeadType)
        self.register_field('show_text', 'Guess')
        self.register_field('is_link', True)
        self.bind('show_text', data_bind_label, 'text')
        self.bind('is_link', data_bind_label, 'link')

        button = MButton(text='Random An Animal', type=MButton.PrimaryType)
        button.clicked.connect(self.slot_change_text)
        link_button = MButton(text='Link', type=MButton.PrimaryType)
        link_button.clicked.connect(self.slot_link_text)

        main_lay = QVBoxLayout()
        main_lay.addWidget(div1)
        main_lay.addWidget(div2)
        main_lay.addWidget(MDivider('different type'))
        main_lay.addLayout(grid_lay)
        main_lay.addWidget(MDivider('data bind'))
        main_lay.addWidget(data_bind_label)
        main_lay.addWidget(button)
        main_lay.addWidget(link_button)
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
