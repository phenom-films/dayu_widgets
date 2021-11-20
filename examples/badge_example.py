#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.avatar import MAvatar
from dayu_widgets.badge import MBadge
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.menu import MMenu
from dayu_widgets.qt import MIcon
from dayu_widgets.qt import MPixmap
from dayu_widgets.qt import QHBoxLayout
from dayu_widgets.qt import QVBoxLayout
from dayu_widgets.qt import QWidget
from dayu_widgets.spin_box import MSpinBox
from dayu_widgets.tool_button import MToolButton


class BadgeExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(BadgeExample, self).__init__(parent)
        self.setWindowTitle("Examples for MBadge")
        self._init_ui()

    def _init_ui(self):
        standalone_lay = QHBoxLayout()
        standalone_lay.addWidget(MBadge.count(0))
        standalone_lay.addWidget(MBadge.count(20))
        standalone_lay.addWidget(MBadge.count(100))
        standalone_lay.addWidget(MBadge.dot(True))
        standalone_lay.addWidget(MBadge.text("new"))
        # standalone_lay.addStretch()

        button = MToolButton().svg("trash_line.svg")
        avatar = MAvatar.large(MPixmap("avatar.png"))
        button_alert = MToolButton().svg("alert_fill.svg").large()
        self.badge_1 = MBadge.dot(True, widget=button)
        self.badge_2 = MBadge.dot(True, widget=avatar)
        self.badge_3 = MBadge.dot(True, widget=button_alert)
        button.clicked.connect(lambda: self.badge_1.set_dayu_dot(False))

        spin_box = MSpinBox()
        spin_box.setRange(0, 9999)
        spin_box.valueChanged.connect(self.badge_3.set_dayu_count)
        spin_box.setValue(1)

        self.register_field("button1_selected", "北京")
        menu1 = MMenu()
        menu1.set_data(["北京", "上海", "广州", "深圳"])
        select1 = MComboBox()
        select1.set_menu(menu1)
        self.bind("button1_selected", select1, "value", signal="sig_value_changed")

        self.badge_hot = MBadge.text("hot", widget=MLabel("你的理想城市  "))

        sub_lay1 = QHBoxLayout()
        sub_lay1.addWidget(self.badge_1)
        sub_lay1.addWidget(self.badge_2)
        sub_lay1.addWidget(self.badge_3)
        sub_lay1.addStretch()

        sub_lay2 = QHBoxLayout()
        sub_lay2.addWidget(self.badge_hot)
        sub_lay2.addWidget(select1)
        sub_lay2.addStretch()

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider("use standalone"))
        main_lay.addLayout(standalone_lay)
        main_lay.addWidget(MDivider("different type"))
        main_lay.addLayout(sub_lay1)
        main_lay.addWidget(spin_box)
        main_lay.addWidget(MDivider("different type"))
        main_lay.addLayout(sub_lay2)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import built-in modules
    import sys

    # Import local modules
    from dayu_widgets.qt import QApplication

    app = QApplication(sys.argv)
    test = BadgeExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
