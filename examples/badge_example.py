#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.spin_box import MSpinBox
from dayu_widgets.avatar import MAvatar
from dayu_widgets.badge import MBadge
from dayu_widgets.MComboBox import MComboBox
from dayu_widgets.divider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.MMenu import MMenu
from dayu_widgets import dayu_theme
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.qt import QWidget, QHBoxLayout, MIcon, MPixmap, QVBoxLayout


class BadgeExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(BadgeExample, self).__init__(parent)
        self.setWindowTitle('Examples for MBadge')
        self._init_ui()

    def _init_ui(self):
        standalone_lay = QHBoxLayout()
        standalone_lay.addWidget(MBadge.count(0))
        standalone_lay.addWidget(MBadge.count(20))
        standalone_lay.addWidget(MBadge.count(100))
        standalone_lay.addWidget(MBadge.dot(True))
        standalone_lay.addWidget(MBadge.text('new'))
        standalone_lay.addStretch()

        button = MToolButton(icon=MIcon('trash_line.svg'))
        avatar = MAvatar.large(MPixmap('avatar.png'))
        button_alert = MToolButton(icon=MIcon('alert_fill.svg'), size=dayu_theme.large)
        badge_1 = MBadge.dot(True, widget=button)
        badge_2 = MBadge.dot(True, widget=avatar)
        badge_3 = MBadge.dot(True, widget=button_alert)
        button.clicked.connect(lambda: badge_1.set_dayu_dot(False))

        spin_box = MSpinBox()
        spin_box.setRange(0, 9999)
        spin_box.valueChanged.connect(badge_3.set_dayu_count)
        spin_box.setValue(1)

        self.register_field('button1_selected', u'北京')
        menu1 = MMenu()
        menu1.set_data([u'北京', u'上海', u'广州', u'深圳'])
        select1 = MComboBox()
        select1.set_menu(menu1)
        self.bind('button1_selected', select1, 'value', signal='sig_value_changed')

        badge_hot = MBadge.text('hot', widget=MLabel(u'你的理想城市  '))

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
        main_lay.addWidget(MDivider('use standalone'))
        main_lay.addLayout(standalone_lay)
        main_lay.addWidget(MDivider('different type'))
        main_lay.addLayout(sub_lay1)
        main_lay.addWidget(spin_box)
        main_lay.addWidget(MDivider('different type'))
        main_lay.addLayout(sub_lay2)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication
    app = QApplication(sys.argv)
    test = BadgeExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
