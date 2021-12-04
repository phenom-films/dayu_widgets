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
from dayu_widgets import dayu_theme
from dayu_widgets.button_group import MPushButtonGroup
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import QHBoxLayout
from dayu_widgets.qt import QVBoxLayout
from dayu_widgets.qt import QWidget
from dayu_widgets.qt import Qt
from dayu_widgets.qt import get_scale_factor


class ProgressCircleExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ProgressCircleExample, self).__init__(parent)
        self.setWindowTitle("Examples for MProgressCircle")
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()
        self.setLayout(main_lay)
        main_lay.addWidget(MDivider("circle"))
        lay1 = QHBoxLayout()
        circle_1 = MProgressCircle(parent=self)
        circle_1.setFormat("%p Days")
        circle_1.setValue(80)
        circle_2 = MProgressCircle(parent=self)
        circle_2.set_dayu_color(dayu_theme.success_color)
        circle_2.setValue(100)
        circle_3 = MProgressCircle(parent=self)
        circle_3.set_dayu_color(dayu_theme.error_color)
        circle_3.setValue(40)

        dashboard_1 = MProgressCircle.dashboard(parent=self)
        dashboard_1.setFormat("%p Days")
        dashboard_1.setValue(80)
        dashboard_2 = MProgressCircle.dashboard(parent=self)
        dashboard_2.set_dayu_color(dayu_theme.success_color)
        dashboard_2.setValue(100)
        dashboard_3 = MProgressCircle.dashboard(parent=self)
        dashboard_3.set_dayu_color(dayu_theme.error_color)
        dashboard_3.setValue(40)

        lay1.addWidget(circle_1)
        lay1.addWidget(circle_2)
        lay1.addWidget(circle_3)

        dashboard_lay = QHBoxLayout()
        dashboard_lay.addWidget(dashboard_1)
        dashboard_lay.addWidget(dashboard_2)
        dashboard_lay.addWidget(dashboard_3)
        main_lay.addLayout(lay1)
        main_lay.addWidget(MDivider("dashboard"))
        main_lay.addLayout(dashboard_lay)
        main_lay.addWidget(MDivider("different radius"))

        scale_x, _ = get_scale_factor()
        circle_4 = MProgressCircle(parent=self)
        circle_4.set_dayu_width(100 * scale_x)
        circle_4.setValue(40)
        circle_5 = MProgressCircle(parent=self)
        circle_5.setValue(40)
        circle_6 = MProgressCircle(parent=self)
        circle_6.set_dayu_width(160 * scale_x)
        circle_6.setValue(40)
        lay2 = QHBoxLayout()
        lay2.addWidget(circle_4)
        lay2.addWidget(circle_5)
        lay2.addWidget(circle_6)

        main_lay.addLayout(lay2)
        main_lay.addWidget(MDivider("data bind"))

        self.register_field("percent", 0)
        self.register_field("color", self.get_color)
        self.register_field("format", self.get_format)
        circle = MProgressCircle(parent=self)

        self.bind("percent", circle, "value")
        self.bind("color", circle, "dayu_color")
        self.bind("format", circle, "format")
        lay3 = QHBoxLayout()
        button_grp = MPushButtonGroup()
        button_grp.set_dayu_type(MPushButton.DefaultType)
        button_grp.set_button_list(
            [
                {
                    "text": "+",
                    "clicked": functools.partial(self.slot_change_percent, 10),
                },
                {
                    "text": "-",
                    "clicked": functools.partial(self.slot_change_percent, -10),
                },
            ]
        )
        lay3.addWidget(circle)
        lay3.addWidget(button_grp)
        lay3.addStretch()
        main_lay.addLayout(lay3)

        custom_widget = QWidget()
        custom_layout = QVBoxLayout()
        custom_layout.setContentsMargins(20, 20, 20, 20)
        custom_layout.addStretch()
        custom_widget.setLayout(custom_layout)
        lab1 = MLabel(text="42,001,776").h3()
        lab2 = MLabel(text="消费人群规模").secondary()
        lab3 = MLabel(text="总占人数 75%").secondary()
        lab1.setAlignment(Qt.AlignCenter)
        lab2.setAlignment(Qt.AlignCenter)
        lab3.setAlignment(Qt.AlignCenter)
        custom_layout.addWidget(lab1)
        custom_layout.addWidget(lab2)
        custom_layout.addWidget(MDivider())
        custom_layout.addWidget(lab3)
        custom_layout.addStretch()
        custom_circle = MProgressCircle()
        custom_circle.set_dayu_width(180 * scale_x)
        custom_circle.setValue(75)
        custom_circle.set_widget(custom_widget)

        main_lay.addWidget(MDivider("custom circle"))
        main_lay.addWidget(custom_circle)
        main_lay.addStretch()

    def get_color(self):
        p = self.field("percent")
        if p < 30:
            return dayu_theme.error_color
        if p < 60:
            return dayu_theme.warning_color
        if p < 100:
            return dayu_theme.primary_color
        return dayu_theme.success_color

    def get_format(self):
        p = self.field("percent")
        if p < 30:
            return ">_<"
        if p < 60:
            return "0_0"
        if p < 100:
            return "^_^"
        return "^o^"

    def slot_change_percent(self, value):
        self.set_field("percent", max(0, min(self.field("percent") + value, 100)))


if __name__ == "__main__":
    # Import built-in modules
    import sys

    # Import third-party modules
    from dayu_widgets.qt import QApplication

    app = QApplication(sys.argv)
    test = ProgressCircleExample()

    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
