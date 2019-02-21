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
from dayu_widgets.MButton import MButton
from dayu_widgets.MFieldMixin import MFieldMixin
import functools

class MRadioGroupTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MRadioGroupTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        self.register_field('value1', -1)
        self.register_field('value2', -1)
        self.register_field('value3', -1)

        radio_group_h = MRadioGroup()
        radio_group_h.set_radio_list(['Apple', {'text': 'Banana'}, {'text': 'Pear'}])

        app_data = [
            {'text': 'Maya', 'icon': MIcon('app-maya.png')},
            {'text': 'Nuke', 'icon': MIcon('app-nuke.png')},
            {'text': 'Houdini', 'icon': MIcon('app-houdini.png')}
        ]

        radio_group_v = MRadioGroup(orientation=Qt.Vertical)
        radio_group_v.set_radio_list(app_data)

        radio_group_button_h = MRadioGroup(type='button')
        radio_group_button_h.set_radio_list(app_data)

        radio_group_button_v = MRadioGroup(type='button', orientation=Qt.Vertical)
        radio_group_button_v.set_radio_list(app_data)


        button1 = MButton(text='Group 1', type=MButton.PrimaryType)
        button2 = MButton(text='Group 2', type=MButton.PrimaryType)
        button3 = MButton(text='Group 3', type=MButton.PrimaryType)
        button1.clicked.connect(functools.partial(self.slot_change_value, 'value1'))
        button2.clicked.connect(functools.partial(self.slot_change_value, 'value2'))
        button3.clicked.connect(functools.partial(self.slot_change_value, 'value3'))

        self.bind('value1', radio_group_v, 'checked', signal='sig_checked_changed')
        self.bind('value2', radio_group_button_h, 'checked', signal='sig_checked_changed')
        self.bind('value3', radio_group_button_v, 'checked', signal='sig_checked_changed')
        self.bind('value1', button1, 'text')
        self.bind('value2', button2, 'text')
        self.bind('value3', button3, 'text')
        radio_group_button_h.set_checked(0)
        radio_group_button_h.set_radio_list(app_data)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('MRadioGroup: orientation=Qt.Horizontal '))
        main_lay.addWidget(radio_group_h)
        main_lay.addWidget(MDivider('MRadioGroup: orientation=Qt.Vertical'))
        main_lay.addWidget(radio_group_v)
        main_lay.addWidget(MDivider('MRadioGroup: orientation=Qt.Horizontal type=button'))
        main_lay.addWidget(radio_group_button_h)
        main_lay.addWidget(MDivider('MRadioGroup: orientation=Qt.Vertical, type=button'))
        main_lay.addWidget(radio_group_button_v)
        main_lay.addWidget(MDivider('data bind'))
        main_lay.addWidget(button1)
        main_lay.addWidget(button2)
        main_lay.addWidget(button3)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_change_value(self, attr):
        import random
        self.set_field(attr, random.randrange(0, 3))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MRadioGroupTest()
    test.show()
    sys.exit(app.exec_())
