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

# Import built-in modules
import functools

# Import third-party modules
from dayu_widgets.button_group import MRadioButtonGroup
from dayu_widgets.check_box import MCheckBox
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import MIcon
from dayu_widgets.qt import QFormLayout
from dayu_widgets.qt import QHBoxLayout
from dayu_widgets.qt import QVBoxLayout
from dayu_widgets.qt import QWidget
from dayu_widgets.qt import Qt
from dayu_widgets.slider import MSlider
from dayu_widgets.spin_box import MDateEdit
from dayu_widgets.spin_box import MSpinBox
from dayu_widgets.switch import MSwitch


class ThemeExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ThemeExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        form_lay = QFormLayout()
        form_lay.setLabelAlignment(Qt.AlignRight)
        gender_grp = MRadioButtonGroup()
        gender_grp.set_button_list(
            [
                {"text": "Female", "icon": MIcon("female.svg")},
                {"text": "Male", "icon": MIcon("male.svg")},
            ]
        )

        country_combo_box = MComboBox().small()
        country_combo_box.addItems(["China", "France", "Japan", "US"])
        date_edit = MDateEdit().small()
        date_edit.setCalendarPopup(True)

        form_lay.addRow("Name:", MLineEdit().small())
        form_lay.addRow("Gender:", gender_grp)
        form_lay.addRow("Age:", MSpinBox().small())
        form_lay.addRow("Password:", MLineEdit().small().password())
        form_lay.addRow("Country:", country_combo_box)
        form_lay.addRow("Birthday:", date_edit)
        switch = MSwitch()
        switch.setChecked(True)
        form_lay.addRow("Switch:", switch)
        slider = MSlider()
        slider.setValue(30)
        form_lay.addRow("Slider:", slider)

        button_lay = QHBoxLayout()
        button_lay.addStretch()
        button_lay.addWidget(MPushButton(text="Submit").primary())
        button_lay.addWidget(MPushButton(text="Cancel"))

        main_lay = QVBoxLayout()
        main_lay.addLayout(form_lay)
        main_lay.addWidget(MCheckBox("I accept the terms and conditions"))
        main_lay.addStretch()
        main_lay.addWidget(MDivider())
        main_lay.addLayout(button_lay)
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import built-in modules
    import sys

    # Import third-party modules
    from dayu_widgets.qt import QApplication

    app = QApplication(sys.argv)
    test = ThemeExample()
    # Import third-party modules
    from dayu_widgets import dayu_theme

    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
