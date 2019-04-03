#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.4
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MCarousel import MCarousel
from dayu_widgets.MSwitch import MSwitch
from dayu_widgets.MLabel import MLabel
from dayu_widgets.qt import *


class MCarouselTest(QWidget):
    def __init__(self, parent=None):
        super(MCarouselTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        switch = MSwitch()
        switch.setChecked(True)
        switch_lay = QHBoxLayout()
        switch_lay.addWidget(MLabel('AutoPlay'))
        switch_lay.addWidget(switch)
        switch_lay.addStretch()
        test = MCarousel([MPixmap('app-{}.png'.format(a)) for a in ['maya', 'nuke', 'houdini']],
                         width=300,
                         height=300,
                         autoplay=True)
        switch.toggled.connect(test.set_autoplay)

        main_lay = QVBoxLayout()
        main_lay.addWidget(test)
        main_lay.addLayout(switch_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':

    import sys
    from dayu_widgets import dayu_theme
    app = QApplication(sys.argv)
    test = MCarouselTest()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
