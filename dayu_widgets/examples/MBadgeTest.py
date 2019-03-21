#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MAbstractSpinBox import MSpinBox
from dayu_widgets.MAvatar import MAvatar
from dayu_widgets.MBadge import MBadge
from dayu_widgets.MComboBox import MComboBox
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MMenu import MMenu
from dayu_widgets.MTheme import dayu_theme
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.mixin import theme_mixin
from dayu_widgets.qt import *


@theme_mixin
class MBadgeTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MBadgeTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        button = MToolButton(icon=MIcon('trash_line.svg'))
        avatar = MAvatar(size=dayu_theme.size.large, image=MPixmap('avatar.png'))
        button_alert = MToolButton(icon=MIcon('alert_fill.svg'), size=dayu_theme.size.large)
        badge_1 = MBadge(widget=button, dot=True)
        badge_2 = MBadge(widget=avatar, dot=True)
        badge_3 = MBadge(widget=button_alert)
        button.clicked.connect(lambda: badge_1.set_dot(False))

        spin_box = MSpinBox()
        spin_box.setRange(0, 9999)
        spin_box.valueChanged.connect(lambda x: badge_3.set_count(x))
        spin_box.setValue(1)

        self.register_field('button1_selected', u'北京')
        menu1 = MMenu()
        menu1.set_data([u'北京', u'上海', u'广州', u'深圳'])
        select1 = MComboBox()
        select1.set_menu(menu1)
        self.bind('button1_selected', select1, 'value', signal='sig_value_changed')

        badge_hot = MBadge(widget=MLabel(u'你的理想城市'), text='hot')

        sub_lay1 = QHBoxLayout()
        sub_lay1.addWidget(badge_1)
        sub_lay1.addWidget(badge_2)
        sub_lay1.addWidget(badge_3)
        sub_lay1.addStretch()

        sub_lay2 = QHBoxLayout()
        sub_lay2.addWidget(badge_hot)
        sub_lay2.addWidget(select1)
        sub_lay2.addStretch()

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different type'))
        main_lay.addLayout(sub_lay1)
        main_lay.addWidget(spin_box)
        main_lay.addWidget(MDivider('different type'))
        main_lay.addLayout(sub_lay2)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MBadgeTest()
    test.show()
    sys.exit(app.exec_())
