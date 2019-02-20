#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import *
from dayu_widgets.MRadioGroup import MRadioGroup
from dayu_widgets.MDivider import MDivider


class MRadioGroupTest(QWidget):
    def __init__(self, parent=None):
        super(MRadioGroupTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        radio_group_h = MRadioGroup()
        radio_group_h.add_radio_list(['Apple', {'text': 'Banana'}, {'text': 'Pear'}])

        app_data = [
            {'text': 'Maya', 'icon': 'app-maya'},
            {'text': 'Nuke', 'icon': 'app-nuke'},
            {'text': 'Houdini', 'icon': 'app-houdini'}
        ]

        radio_group_v = MRadioGroup(orientation=Qt.Vertical)
        radio_group_v.add_radio_list(app_data)

        radio_group_button_h = MRadioGroup(type='button')
        radio_group_button_h.add_radio_list(app_data)
        radio_group_button_h.set_checked(0)

        radio_group_button_v = MRadioGroup(type='button', orientation=Qt.Vertical)
        radio_group_button_v.add_radio_list(app_data)
        radio_group_button_v.set_checked(0)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('MRadioGroup: orientation=Qt.Horizontal '))
        main_lay.addWidget(radio_group_h)
        main_lay.addWidget(MDivider('MRadioGroup: orientation=Qt.Vertical'))
        main_lay.addWidget(radio_group_v)
        main_lay.addWidget(MDivider('MRadioGroup: orientation=Qt.Horizontal type=button'))
        main_lay.addWidget(radio_group_button_h)
        main_lay.addWidget(MDivider('MRadioGroup: orientation=Qt.Vertical, type=button'))
        main_lay.addWidget(radio_group_button_v)
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MRadioGroupTest()
    test.show()
    sys.exit(app.exec_())
