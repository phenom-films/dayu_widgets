#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.qt import QWidget, QVBoxLayout, QHBoxLayout
from dayu_widgets.tool_button import MToolButton


class ToolButtonExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ToolButtonExample, self).__init__(parent)
        self.setWindowTitle('Examples for MToolButton')
        self._init_ui()

    def _init_ui(self):
        size_lay = QVBoxLayout()
        sub_lay1 = QHBoxLayout()
        sub_lay1.addWidget(MToolButton().svg('left_line.svg').icon_only())
        sub_lay1.addWidget(MToolButton().svg('right_line.svg').icon_only())
        sub_lay1.addWidget(MToolButton().svg('up_line.svg').icon_only())
        sub_lay1.addWidget(MToolButton().svg('down_line.svg').icon_only())
        sub_lay1.addStretch()
        size_lay.addLayout(sub_lay1)

        button2 = MToolButton().svg('detail_line.svg').icon_only()
        button2.setEnabled(False)
        button7 = MToolButton().svg('trash_line.svg').icon_only()
        button7.setCheckable(True)
        state_lay = QHBoxLayout()
        state_lay.addWidget(button2)
        state_lay.addWidget(button7)
        state_lay.addStretch()

        button_trash = MToolButton().svg('trash_line.svg').text_beside_icon()
        button_trash.setText('Delete')
        button_login = MToolButton().svg('user_line.svg').text_beside_icon()
        button_login.setText('Login')

        button_lay = QHBoxLayout()
        button_lay.addWidget(button_trash)
        button_lay.addWidget(button_login)

        sub_lay2 = QHBoxLayout()
        sub_lay2.addWidget(button2)
        sub_lay2.addWidget(button7)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different button_size'))
        main_lay.addLayout(size_lay)
        main_lay.addWidget(MDivider('disabled & checkable'))
        main_lay.addLayout(state_lay)
        main_lay.addWidget(MDivider('type=normal'))
        main_lay.addLayout(button_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication
    from dayu_widgets import dayu_theme

    app = QApplication(sys.argv)
    test = ToolButtonExample()

    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
