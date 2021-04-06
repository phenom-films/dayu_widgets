#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: TimmyLiang
# Date  : 2021-4-6
# Email : 820472580@qq.com
###################################################################
from dayu_widgets.qt import QWidget,QPushButton

import os
from functools import partial


class OverlayExample(QWidget):
    def __init__(self, parent=None):
        super(OverlayExample, self).__init__(parent)
        from Qt.QtCompat import load_ui
        self.setWindowTitle('Examples for OverlayWidget')
        DIR, file_name = os.path.split(__file__)
        file_name = os.path.splitext(file_name)[0]
        load_ui(os.path.join(DIR, "%s.ui" % file_name), self)
        for btn in self.findChildren(QPushButton):
            btn.clicked.connect(partial(print, btn.objectName()))

if __name__ == '__main__':
    import sys
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import QApplication

    app = QApplication(sys.argv)
    test = OverlayExample()
    dayu_theme.apply(test)

    test.show()
    sys.exit(app.exec_())
