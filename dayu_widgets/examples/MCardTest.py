#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.4
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MCard import MCard
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFlowLayout import MFlowLayout
from dayu_widgets.qt import *
from dayu_widgets import dayu_theme


class MCardTest(QWidget):
    def __init__(self, parent=None):
        super(MCardTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):

        basic_card = MFlowLayout()
        basic_card.setSpacing(20)
        for setting in [
            {
                'title': '',
            },
            {
                'title': 'Card Title',
                'size': dayu_theme.small
            },
            {
                'title': 'Card Title',
                'image': MPixmap('app-houdini.png')
            },
            {
                'title': 'Card Title',
                'extra': 'More',
                'image': MPixmap('app-houdini.png')
            },
            {
                'title': 'Card Title',
                'extra': 'More',
            }
        ]:
            card_0 = MCard(**setting)
            content_widget_0 = QWidget()
            content_lay_0 = QVBoxLayout()
            content_lay_0.setContentsMargins(15, 15, 15, 15)
            content_widget_0.setLayout(content_lay_0)
            for i in range(4):
                content_lay_0.addWidget(MLabel('Card Content {}'.format(i + 1)))
            card_0.set_widget(content_widget_0)

            basic_card.addWidget(card_0)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('Basic'))
        main_lay.addLayout(basic_card)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MCardTest()
    from dayu_widgets import dayu_theme

    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
