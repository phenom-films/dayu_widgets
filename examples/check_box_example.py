#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from Qt import QtCore
from Qt import QtWidgets
from dayu_widgets.check_box import MCheckBox
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import MIcon


class CheckBoxExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(CheckBoxExample, self).__init__(parent)
        self.setWindowTitle("Example for MCheckBox")
        grid_lay = QtWidgets.QGridLayout()

        for index, (text, state) in enumerate(
            [
                ("Unchecked", QtCore.Qt.Unchecked),
                ("Checked", QtCore.Qt.Checked),
                ("Partially", QtCore.Qt.PartiallyChecked),
            ]
        ):
            check_box_normal = MCheckBox(text)
            check_box_normal.setCheckState(state)

            check_box_disabled = MCheckBox(text)
            check_box_disabled.setCheckState(state)
            check_box_disabled.setEnabled(False)

            grid_lay.addWidget(check_box_normal, 0, index)
            grid_lay.addWidget(check_box_disabled, 1, index)

        icon_lay = QtWidgets.QHBoxLayout()
        for text, icon in [
            ("Maya", MIcon("app-maya.png")),
            ("Nuke", MIcon("app-nuke.png")),
            ("Houdini", MIcon("app-houdini.png")),
        ]:
            check_box_icon = MCheckBox(text)
            check_box_icon.setIcon(icon)
            icon_lay.addWidget(check_box_icon)

        check_box_bind = MCheckBox("Data Bind")
        label = MLabel()
        button = MPushButton(text="Change State")
        button.clicked.connect(
            lambda: self.set_field("checked", not self.field("checked"))
        )
        self.register_field("checked", True)
        self.register_field(
            "checked_text", lambda: "Yes!" if self.field("checked") else "No!!"
        )
        self.bind("checked", check_box_bind, "checked", signal="stateChanged")
        self.bind("checked_text", label, "text")

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Basic"))
        main_lay.addLayout(grid_lay)
        main_lay.addWidget(MDivider("Icon"))
        main_lay.addLayout(icon_lay)
        main_lay.addWidget(MDivider("Data Bind"))
        main_lay.addWidget(check_box_bind)
        main_lay.addWidget(label)
        main_lay.addWidget(button)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import built-in modules
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test = CheckBoxExample()
    # Import third-party modules
    from dayu_widgets import dayu_theme

    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
