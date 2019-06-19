#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.divider import MDivider
from dayu_widgets.label import MLabel
from dayu_widgets.qt import QWidget, QHBoxLayout, QVBoxLayout


class DividerExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(DividerExample, self).__init__(parent)
        self.setWindowTitle('Examples for MDivider')
        self._init_ui()

    def _init_ui(self):
        div1 = MDivider()
        div2 = MDivider('With Text')
        div3 = MDivider.left('Left Text')
        div4 = MDivider.center('Center Text')
        div5 = MDivider.right('Right Text')
        div6 = MDivider.vertical()
        div7 = MDivider.vertical()
        div8 = MDivider.left('orientation=Qt.Vertical')
        label1 = MLabel.strong('Maya')
        label2 = MLabel.underline('Nuke')
        label3 = MLabel.mark('Houdini')
        sub_lay = QHBoxLayout()
        sub_lay.addWidget(label1)
        sub_lay.addWidget(div6)
        sub_lay.addWidget(label2)
        sub_lay.addWidget(div7)
        sub_lay.addWidget(label3)
        sub_lay.addStretch()

        some_text = 'Steven Paul Jobs was an American entrepreneur and business magnate.'
        main_lay = QVBoxLayout()
        main_lay.addWidget(MLabel(some_text))
        main_lay.addWidget(div1)
        main_lay.addWidget(MLabel(some_text))
        main_lay.addWidget(div2)
        main_lay.addWidget(MLabel(some_text))
        main_lay.addWidget(div3)
        main_lay.addWidget(MLabel(some_text))
        main_lay.addWidget(div4)
        main_lay.addWidget(MLabel(some_text))
        main_lay.addWidget(div5)
        main_lay.addLayout(sub_lay)
        main_lay.addWidget(div8)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def computed_text(self):
        return 'Clicked: ' + str(self.field('count'))

    def slot_change_divider_text(self):
        self.set_field('count', self.field('count') + 1)


if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication
    from dayu_widgets import dayu_theme

    app = QApplication(sys.argv)
    test = DividerExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
