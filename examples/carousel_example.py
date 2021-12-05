#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.4
# Email : muyanru345@163.com
###################################################################

# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from dayu_widgets.carousel import MCarousel
from dayu_widgets.label import MLabel
from dayu_widgets.qt import *
from dayu_widgets.slider import MSlider
from dayu_widgets.switch import MSwitch


class CarouselExample(QWidget):
    def __init__(self, parent=None):
        super(CarouselExample, self).__init__(parent)
        self.setWindowTitle("Examples for MCarousel")
        self._init_ui()

    def _init_ui(self):
        switch = MSwitch()
        switch.setChecked(True)
        slider = MSlider()
        slider.setRange(1, 10)
        switch_lay = QFormLayout()
        switch_lay.addRow(MLabel("AutoPlay"), switch)
        switch_lay.addRow(MLabel("Interval"), slider)
        test = MCarousel(
            [MPixmap("app-{}.png".format(a)) for a in ["maya", "nuke", "houdini"]],
            width=300,
            height=300,
            autoplay=True,
        )
        switch.toggled.connect(test.set_autoplay)
        slider.valueChanged.connect(lambda x: test.set_interval(x * 1000))
        slider.setValue(3)

        main_lay = QVBoxLayout()
        main_lay.addWidget(test)
        main_lay.addLayout(switch_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import built-in modules
    import sys

    # Import third-party modules
    from dayu_widgets import dayu_theme

    app = QApplication(sys.argv)
    test = CarouselExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
