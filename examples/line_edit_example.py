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
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.divider import MDivider
from dayu_widgets.label import MLabel
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.menu import MMenu
from dayu_widgets.message import MMessage
from dayu_widgets.push_button import MPushButton
from dayu_widgets.tool_button import MToolButton


class LineEditExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LineEditExample, self).__init__(parent)
        self.setWindowTitle("Examples for MLineEdit")
        self._init_ui()

    def _init_ui(self):
        size_lay = QtWidgets.QHBoxLayout()
        line_edit_l = MLineEdit().large()
        line_edit_l.setPlaceholderText("large size")
        line_edit_m = MLineEdit().medium()
        line_edit_m.setPlaceholderText("default size")
        line_edit_s = MLineEdit().small()
        line_edit_s.setPlaceholderText("small size")
        size_lay.addWidget(line_edit_l)
        size_lay.addWidget(line_edit_m)
        size_lay.addWidget(line_edit_s)

        line_edit_tool_button = MLineEdit(text="MToolButton")
        line_edit_tool_button.set_prefix_widget(
            MToolButton().svg("user_line.svg").icon_only()
        )

        line_edit_label = MLineEdit(text="MLabel")
        tool_button = MLabel(text="User").mark().secondary()
        tool_button.setAlignment(QtCore.Qt.AlignCenter)
        tool_button.setFixedWidth(80)
        line_edit_label.set_prefix_widget(tool_button)

        line_edit_push_button = MLineEdit(text="MPushButton")
        push_button = MPushButton(text="Go").primary()
        push_button.setFixedWidth(40)
        line_edit_push_button.set_suffix_widget(push_button)

        search_engine_line_edit = MLineEdit().search_engine().large()
        search_engine_line_edit.returnPressed.connect(self.slot_search)

        line_edit_options = MLineEdit()
        combobox = MComboBox()
        option_menu = MMenu()
        option_menu.set_separator("|")
        option_menu.set_data([r"http://", r"https://"])
        combobox.set_menu(option_menu)
        combobox.set_value("http://")
        combobox.setFixedWidth(100)
        line_edit_options.set_prefix_widget(combobox)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("different size"))
        main_lay.addLayout(size_lay)
        main_lay.addWidget(MDivider("custom prefix and suffix widget"))
        main_lay.addWidget(line_edit_tool_button)
        main_lay.addWidget(line_edit_label)
        main_lay.addWidget(line_edit_push_button)
        main_lay.addWidget(MDivider("preset"))

        main_lay.addWidget(MLabel("error"))
        main_lay.addWidget(
            MLineEdit(text="waring: file d:/ddd/ccc.jpg not exists.").error()
        )
        main_lay.addWidget(MLabel("search"))
        main_lay.addWidget(MLineEdit().search().small())
        main_lay.addWidget(MLabel("search_engine"))
        main_lay.addWidget(search_engine_line_edit)
        main_lay.addWidget(MLabel("file"))
        main_lay.addWidget(MLineEdit().file().small())
        main_lay.addWidget(MLabel("folder"))
        main_lay.addWidget(MLineEdit().folder().small())
        main_lay.addWidget(MLabel("MLineEdit.options()"))
        main_lay.addWidget(line_edit_options)
        main_lay.addStretch()
        self.setLayout(main_lay)

    @QtCore.Slot()
    def slot_search(self):
        MMessage.info("查无此人", parent=self)


if __name__ == "__main__":
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = LineEditExample()
        dayu_theme.apply(test)
        test.show()
