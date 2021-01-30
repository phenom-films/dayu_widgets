# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.button_group import MPushButtonGroup
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.push_button import MPushButton
from dayu_widgets import dayu_theme
from dayu_widgets.qt import *


class PushButtonGroupExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(PushButtonGroupExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        button_config_list = [
            {'text': 'Add', 'icon': MIcon('add_line.svg', '#fff'), 'type': MPushButton.PrimaryType},
            {'text': 'Edit', 'icon': MIcon('edit_fill.svg', '#fff'), 'type': MPushButton.WarningType},
            {'text': 'Delete', 'icon': MIcon('trash_line.svg', '#fff'), 'type': MPushButton.DangerType},
        ]
        button_group_h = MPushButtonGroup()
        button_group_h.set_dayu_size(dayu_theme.large)
        button_group_h.set_button_list(button_config_list)
        h_lay = QHBoxLayout()
        h_lay.addWidget(button_group_h)
        h_lay.addStretch()

        button_group_v = MPushButtonGroup(orientation=Qt.Vertical)
        button_group_v.set_button_list(button_config_list)
        h_lay_2 = QHBoxLayout()
        h_lay_2.addWidget(button_group_v)
        h_lay_2.addStretch()

        main_lay = QVBoxLayout()
        main_lay.addWidget(
            MLabel(u'MPushButtonGroup is MPushButton collection. they are not exclusive.'))
        main_lay.addWidget(MDivider('MPushButton group: Horizontal & Small Size'))
        main_lay.addLayout(h_lay)
        main_lay.addWidget(MDivider('MPushButton group: Vertical & Default Size'))
        main_lay.addLayout(h_lay_2)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = PushButtonGroupExample()
    from dayu_widgets import dayu_theme
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
