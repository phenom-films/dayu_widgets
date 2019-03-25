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
from dayu_widgets import dayu_theme
from dayu_widgets.qt import *


class MPushButtonGroupTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MPushButtonGroupTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        button_config_list = [
            {'text': 'Add', 'icon': MIcon('add_line.svg', '#fff'), 'type': MPushButton.PrimaryType},
            {'text': 'Edit', 'icon': MIcon('edit_fill.svg', '#fff'), 'type': MPushButton.InfoType},
            {'text': 'Delete', 'icon': MIcon('trash_line.svg', '#fff'), 'type': MPushButton.ErrorType},
        ]
        button_group_h = MPushButtonGroup(size=dayu_theme.size.small)
        button_group_h.set_button_list(button_config_list)

        button_group_v = MPushButtonGroup(orientation=Qt.Vertical)
        button_group_v.set_button_list(button_config_list)

        main_lay = QVBoxLayout()
        main_lay.addWidget(
            MLabel(u'MPushButtonGroup is MPushButton collection. they are not exclusive.'))
        main_lay.addWidget(MDivider('MPushButton group: Horizontal & Small Size'))
        main_lay.addWidget(button_group_h)
        main_lay.addWidget(MDivider('MPushButton group: Vertical & Default Size'))
        main_lay.addWidget(button_group_v)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MPushButtonGroupTest()
    from dayu_widgets import dayu_theme
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())