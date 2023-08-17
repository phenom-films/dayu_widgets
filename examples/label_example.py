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
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3.divider import MDivider
from dayu_widgets3.field_mixin import MFieldMixin
from dayu_widgets3.label import MLabel
from dayu_widgets3.push_button import MPushButton


class LabelExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(LabelExample, self).__init__(parent)
        self.setWindowTitle("Examples for MLabel")
        self._init_ui()

    def _init_ui(self):
        title_lay = QtWidgets.QGridLayout()
        title_lay.addWidget(MLabel("一级标题").h1(), 0, 0)
        title_lay.addWidget(MLabel("二级标题").h2(), 1, 0)
        title_lay.addWidget(MLabel("三级标题").h3(), 2, 0)
        title_lay.addWidget(MLabel("四级标题").h4(), 3, 0)
        title_lay.addWidget(MLabel("h1 Level").h1(), 0, 1)
        title_lay.addWidget(MLabel("h2 Level").h2(), 1, 1)
        title_lay.addWidget(MLabel("h3 Level").h3(), 2, 1)
        title_lay.addWidget(MLabel("h4 Level").h4(), 3, 1)

        text_type_lay = QtWidgets.QHBoxLayout()
        text_type_lay.addWidget(MLabel("MLabel: Normal"))
        text_type_lay.addWidget(MLabel("MLabel: Secondary").secondary())
        text_type_lay.addWidget(MLabel("MLabel: Warning").warning())
        text_type_lay.addWidget(MLabel("MLabel: Danger").danger())
        disable_text = MLabel("MLabel: Disabled")
        disable_text.setEnabled(False)
        text_type_lay.addWidget(disable_text)

        text_attr_lay = QtWidgets.QHBoxLayout()
        text_attr_lay.addWidget(MLabel("MLabel: Mark").mark())
        text_attr_lay.addWidget(MLabel("MLabel: Code").code())
        text_attr_lay.addWidget(MLabel("MLabel: Underline").underline())
        text_attr_lay.addWidget(MLabel("MLabel: Delete").delete())
        text_attr_lay.addWidget(MLabel("MLabel: Strong").strong())

        text_mix_lay = QtWidgets.QHBoxLayout()
        text_mix_lay.addWidget(
            MLabel("MLabel: Strong & Underline").strong().underline()
        )
        text_mix_lay.addWidget(MLabel("MLabel: Danger & Delete").danger().delete())
        text_mix_lay.addWidget(MLabel("MLabel: Warning & Strong").warning().strong())
        text_mix_lay.addWidget(MLabel("MLabel: H4 & Mark").h4().mark())

        data_bind_lay = QtWidgets.QHBoxLayout()
        data_bind_label = MLabel()
        button = MPushButton(text="Random An Animal").primary()
        button.clicked.connect(self.slot_change_text)
        data_bind_lay.addWidget(data_bind_label)
        data_bind_lay.addWidget(button)
        data_bind_lay.addStretch()
        self.register_field("show_text", "Guess")
        self.bind("show_text", data_bind_label, "text")

        lay_elide = QtWidgets.QVBoxLayout()
        label_none = MLabel(
            "This is a elide NONE mode label. "
            "Ellipsis should NOT appear in the text."
        )
        label_left = MLabel(
            "This is a elide LEFT mode label. "
            "The ellipsis should appear at the beginning of the text. "
            "xiao mao xiao gou xiao ci wei"
        )
        label_left.set_elide_mode(QtCore.Qt.ElideLeft)
        label_middle = MLabel(
            "This is a elide MIDDLE mode label. "
            "The ellipsis should appear in the middle of the text. "
            "xiao mao xiao gou xiao ci wei"
        )
        label_middle.set_elide_mode(QtCore.Qt.ElideMiddle)
        label_right = MLabel()
        label_right.setText(
            "This is a elide RIGHT mode label. "
            "The ellipsis should appear at the end of the text. "
            "Some text to fill the line bala bala bala."
        )
        label_right.set_elide_mode(QtCore.Qt.ElideRight)
        lay_elide.addWidget(label_none)
        lay_elide.addWidget(label_left)
        lay_elide.addWidget(label_middle)
        lay_elide.addWidget(label_right)

        hyper_label_1 = MLabel()
        hyper_label_1.set_link("https://baidu.com", text="baidu")
        hyper_label_2 = MLabel()
        hyper_label_2.set_link("https://baidu.com")
        hyper_label_3 = MLabel()
        hyper_label_3.set_link(
            "https://github.com/phenom-films/dayu_widgets", text="Dayu Widgets"
        )

        hyperlink_lay = QtWidgets.QVBoxLayout()
        hyperlink_lay.addWidget(hyper_label_1)
        hyperlink_lay.addWidget(hyper_label_2)
        hyperlink_lay.addWidget(hyper_label_3)
        # hyperlink_lay.addWidget()

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("different level"))
        main_lay.addLayout(title_lay)
        main_lay.addWidget(MDivider("different type"))
        main_lay.addLayout(text_type_lay)
        main_lay.addWidget(MDivider("different property"))
        main_lay.addLayout(text_attr_lay)
        main_lay.addWidget(MDivider("mix"))
        main_lay.addLayout(text_mix_lay)

        # main_lay.addWidget(MDivider('data bind'))
        # main_lay.addLayout(data_bind_lay)
        main_lay.addWidget(MDivider("elide mode"))
        main_lay.addLayout(lay_elide)
        main_lay.addWidget(MDivider("hyperlink"))
        main_lay.addLayout(hyperlink_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_change_text(self):
        # Import built-in modules
        import random

        self.set_field("show_text", random.choice(["Dog", "Cat", "Rabbit", "Cow"]))

    def slot_link_text(self):
        self.set_field("is_link", not self.field("is_link"))


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets3 import dayu_theme
    from dayu_widgets3.qt import application

    with application() as app:
        test = LabelExample()
        dayu_theme.apply(test)
        test.show()
