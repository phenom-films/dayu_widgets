#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MButtonGroup import MPushButtonGroup
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MPushButton import MPushButton
from dayu_widgets.qt import *


class MPushButtonGroupTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MPushButtonGroupTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        button_config_list = [
            {'text': 'Delete', 'icon': MIcon('trash_fill.svg', '#dddddd'), 'type': MPushButton.ErrorType},
            {'text': 'PrimaryType', 'icon': MIcon('search_line.svg', '#dddddd'), 'type': MPushButton.PrimaryType},
            {'text': 'PrimaryType', 'icon': MIcon('folder_fill.svg', '#dddddd'), 'type': MPushButton.PrimaryType},
            {'text': 'Up', 'icon': MIcon('up_fill.svg', '#dddddd'), 'type': MPushButton.PrimaryType},
        ]
        button_group_h = MPushButtonGroup(size=MView.LargeSize)
        button_group_h.set_button_list(button_config_list)

        button_group_v = MPushButtonGroup(orientation=Qt.Vertical)
        button_group_v.set_button_list(button_config_list)

        main_lay = QVBoxLayout()
        main_lay.addWidget(
            MLabel(u'MPushButtonGroup is MPushButton or MToolButton collection. they are not exclusive.'))
        main_lay.addWidget(MDivider('MPushButton group: Horizontal & Large Size'))
        main_lay.addWidget(button_group_h)
        main_lay.addWidget(MDivider('MPushButton group: Vertical & Default Size'))
        main_lay.addWidget(button_group_v)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_change_button_type(self):
        import random
        self.set_field('button_type', random.choice(
            [MPushButton.DefaultType, MPushButton.PrimaryType, MPushButton.SuccessType, MPushButton.InfoType,
             MPushButton.WarningType, MPushButton.ErrorType]))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MPushButtonGroupTest()
    test.show()
    sys.exit(app.exec_())
