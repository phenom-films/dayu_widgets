#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.MButtonGroup import MToolButtonGroup
from dayu_widgets.MTheme import dayu_theme
from dayu_widgets.mixin import theme_mixin
from dayu_widgets.qt import *

@theme_mixin
class MToolButtonTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MToolButtonTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        size_list = [('Huge', dayu_theme.size.huge),
                     ('Large', dayu_theme.size.large),
                     ('Medium', dayu_theme.size.medium),
                     ('Small', dayu_theme.size.small),
                     ('Tiny', dayu_theme.size.tiny)]

        size_lay = QVBoxLayout()
        for label, size in size_list:
            sub_lay1 = QHBoxLayout()
            sub_lay1.addWidget(MToolButton(icon=MIcon('left_line.svg'), size=size, type=MToolButton.IconOnlyType))
            sub_lay1.addWidget(MToolButton(icon=MIcon('right_line.svg'), size=size, type=MToolButton.IconOnlyType))
            sub_lay1.addWidget(MToolButton(icon=MIcon('up_line.svg'), size=size, text='Up'))
            sub_lay1.addWidget(MToolButton(icon=MIcon('down_line.svg'), size=size, text='Down'))
            sub_lay1.addStretch()
            size_lay.addLayout(sub_lay1)

        button2 = MToolButton(icon=MIcon('detail_line.svg'), type=MToolButton.IconOnlyType)
        button2.setEnabled(False)
        button7 = MToolButton(icon=MIcon('trash_line.svg'),
                              icon_checked=MIcon('trash_line.svg', dayu_theme.color.primary), type=MToolButton.IconOnlyType)
        button7.setCheckable(True)

        button_trash = MToolButton(icon=MIcon('trash_line.svg'))
        button_trash.setText('Delete')
        button_login = MToolButton(icon=MIcon('user_line.svg'))
        button_login.setText('Login')
        button_grp = MToolButtonGroup(exclusive=True, type=MToolButton.TaoBaoType)
        button_grp.set_button_list([
            {
                'icon': MIcon('male.svg'),
                'icon_checked': MIcon('male.svg', dayu_theme.color.male),
                'checkable': True,
                'text': u'男款 (37~42均码)',
                'type': MToolButton.TaoBaoType},
            {
                'icon': MIcon('female.svg'),
                'icon_checked': MIcon('female.svg', dayu_theme.color.female),
                'checkable': True,
                'text': u'女款 (35~39均码)',
                'type': MToolButton.TaoBaoType
            }
        ])

        button_lay = QHBoxLayout()
        button_lay.addWidget(button_trash)
        button_lay.addWidget(button_login)

        sub_lay2 = QHBoxLayout()
        sub_lay2.addWidget(button2)
        sub_lay2.addWidget(button7)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different button_size'))
        main_lay.addLayout(size_lay)
        main_lay.addWidget(MDivider('disabled'))
        main_lay.addWidget(button2)
        main_lay.addWidget(MDivider('checkable'))
        main_lay.addWidget(button7)
        main_lay.addWidget(MDivider('type=normal'))
        main_lay.addLayout(button_lay)
        main_lay.addWidget(MDivider('type=taobao'))
        main_lay.addWidget(button_grp)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MToolButtonTest()
    test.show()
    sys.exit(app.exec_())
