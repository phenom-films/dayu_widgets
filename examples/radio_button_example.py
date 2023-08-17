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
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3.divider import MDivider
from dayu_widgets3.field_mixin import MFieldMixin
from dayu_widgets3.label import MLabel
from dayu_widgets3.push_button import MPushButton
from dayu_widgets3.qt import MIcon
from dayu_widgets3.radio_button import MRadioButton


class RadioButtonExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(RadioButtonExample, self).__init__(parent)
        self.setWindowTitle("Example for MRadioButton")
        widget_1 = QtWidgets.QWidget()
        lay_1 = QtWidgets.QHBoxLayout()
        lay_1.addWidget(MRadioButton("Maya"))
        lay_1.addWidget(MRadioButton("Nuke"))
        lay_1.addWidget(MRadioButton("Houdini"))
        widget_1.setLayout(lay_1)

        check_box_icon_1 = MRadioButton("Folder")
        check_box_icon_1.setIcon(MIcon("folder_fill.svg"))
        check_box_icon_2 = MRadioButton("Media")
        check_box_icon_2.setIcon(MIcon("media_fill.svg"))
        check_box_icon_3 = MRadioButton("User")
        check_box_icon_3.setIcon(MIcon("user_fill.svg"))
        check_box_icon_2.setChecked(True)
        widget_2 = QtWidgets.QWidget()
        lay_2 = QtWidgets.QHBoxLayout()
        lay_2.addWidget(check_box_icon_1)
        lay_2.addWidget(check_box_icon_2)
        lay_2.addWidget(check_box_icon_3)
        widget_2.setLayout(lay_2)

        check_box_single = MRadioButton("支付宝")
        check_box_single.setChecked(True)
        check_box_single.setEnabled(False)

        check_box_bind = MRadioButton("Data Bind")
        label = MLabel()
        button = MPushButton(text="Change State")
        button.clicked.connect(
            lambda: self.set_field("checked", not self.field("checked"))
        )
        self.register_field("checked", True)
        self.register_field(
            "checked_text", lambda: "Yes!" if self.field("checked") else "No!!"
        )
        self.bind("checked", check_box_bind, "checked", signal="toggled")
        self.bind("checked_text", label, "text")

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Basic"))
        main_lay.addWidget(widget_1)
        main_lay.addWidget(check_box_single)
        main_lay.addWidget(MDivider("Icon"))
        main_lay.addWidget(widget_2)
        main_lay.addWidget(MDivider("Data Bind"))
        main_lay.addWidget(check_box_bind)
        main_lay.addWidget(label)
        main_lay.addWidget(button)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets3 import dayu_theme
    from dayu_widgets3.qt import application

    with application() as app:
        test = RadioButtonExample()
        dayu_theme.apply(test)
        test.show()
