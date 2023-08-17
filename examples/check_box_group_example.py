#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################


# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3.button_group import MCheckBoxGroup
from dayu_widgets3.divider import MDivider
from dayu_widgets3.field_mixin import MFieldMixin
from dayu_widgets3.label import MLabel
from dayu_widgets3.push_button import MPushButton
from dayu_widgets3.qt import MIcon


class CheckBoxGroupExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(CheckBoxGroupExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        self.app_data = [
            {"text": "Maya", "icon": MIcon("app-maya.png")},
            {"text": "Nuke", "icon": MIcon("app-nuke.png")},
            {"text": "Houdini", "icon": MIcon("app-houdini.png")},
        ]
        radio_group_h = MCheckBoxGroup()
        radio_group_v = MCheckBoxGroup(orientation=QtCore.Qt.Vertical)

        radio_group_h.set_button_list(self.app_data)
        radio_group_v.set_button_list(self.app_data)

        self.data_list = ["北京", "上海", "广州", "深圳", "郑州", "石家庄"]
        radio_group_b = MCheckBoxGroup()
        radio_group_b.set_button_list(self.data_list)

        button = MPushButton(text="Change Value")
        button.clicked.connect(self.slot_button_clicked)

        label = MLabel()
        self.register_field("checked_app", ["北京", "郑州"])
        self.register_field(
            "checked_app_text", lambda: " & ".join(self.field("checked_app"))
        )
        self.bind(
            "checked_app", radio_group_b, "dayu_checked", signal="sig_checked_changed"
        )
        self.bind("checked_app_text", label, "text")

        radio_group_tri = MCheckBoxGroup()
        radio_group_tri.set_button_list(self.app_data)
        self.register_field("check_grp", ["Maya"])
        self.bind(
            "check_grp", radio_group_tri, "dayu_checked", signal="sig_checked_changed"
        )

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Orientation Qt.Horizontal"))
        main_lay.addWidget(radio_group_h)
        main_lay.addWidget(MDivider("Orientation Qt.Vertical"))
        main_lay.addWidget(radio_group_v)

        main_lay.addWidget(MDivider("Data Bind"))
        main_lay.addWidget(radio_group_b)
        main_lay.addWidget(label)
        main_lay.addWidget(button)

        main_lay.addWidget(MDivider("Try Context Menu"))
        main_lay.addWidget(radio_group_tri)
        main_lay.addStretch()
        self.setLayout(main_lay)

    @QtCore.Slot()
    def slot_button_clicked(self):
        # Import built-in modules
        import random

        start = random.randint(0, len(self.data_list))
        end = random.randint(start, len(self.data_list))
        self.set_field("checked_app", self.data_list[start:end])


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets3 import dayu_theme
    from dayu_widgets3.qt import application

    with application() as app:
        test = CheckBoxGroupExample()
        dayu_theme.apply(test)
        test.show()
