# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.6
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.text_edit import MTextEdit
from dayu_widgets.label import MLabel
from dayu_widgets.divider import MDivider
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import *



class TextEditExample(QWidget):
    def __init__(self, parent=None):
        super(TextEditExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()

        main_lay.addWidget(MDivider('no size grip'))
        main_lay.addWidget(MTextEdit(self))
        main_lay.addWidget(MDivider('size grip'))
        main_lay.addWidget(MTextEdit(self).resizeable())
        main_lay.addWidget(MPushButton('text').primary())

        self.setLayout(main_lay)

if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication
    from dayu_widgets import dayu_theme
    app = QApplication(sys.argv)
    test = TextEditExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
