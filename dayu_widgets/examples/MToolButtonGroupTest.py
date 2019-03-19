#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

import functools

from dayu_widgets.MButtonGroup import MToolButtonGroup
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MPushButton import MPushButton
from dayu_widgets.MTheme import global_theme
from dayu_widgets.qt import *


class MToolButtonGroupTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MToolButtonGroupTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        tool_group_h = MToolButtonGroup(icon_only=False, size=MView.SmallSize)
        tool_group_h.set_button_list(['Apple', {'text': 'Banana'}, {'text': 'Pear'}])

        app_data = [
            {'text': 'Maya', 'icon': MIcon('app-maya.png')},
            {'text': 'Nuke', 'icon': MIcon('app-nuke.png')},
            {'text': 'Houdini', 'icon': MIcon('app-houdini.png')}
        ]

        tool_group_v = MToolButtonGroup(icon_only=False, size=MView.SmallSize, orientation=Qt.Vertical, checkable=True)
        tool_group_v.set_button_list(app_data)

        tool_group_button_h = MToolButtonGroup()
        tool_group_button_h.set_button_list(app_data)


        tool_grp_excl_true = MToolButtonGroup(orientation=Qt.Horizontal, checkable=True)
        tool_grp_excl_true.set_button_list([
            {'icon': MIcon('table_view.svg'),
             'icon_checked': MIcon('table_view.svg', global_theme.get('primary')),
             'tooltip': u'Table View'},
            {'icon': MIcon('list_view.svg'),
             'icon_checked': MIcon('list_view.svg', global_theme.get('primary')),
             'tooltip': u'List View'},
            {'icon': MIcon('tree_view.svg'),
             'icon_checked': MIcon('tree_view.svg', global_theme.get('primary')),
             'tooltip': u'Tree View'},
            {'icon': MIcon('big_view.svg'),
             'icon_checked': MIcon('big_view.svg', global_theme.get('primary')),
             'tooltip': u'Big View'},
        ])
        tool_grp_excl_true.set_checked(0)

        tool_grp_excl_false = MToolButtonGroup(orientation=Qt.Horizontal, checkable=True, icon_only=False)
        tool_grp_excl_false.set_button_list(app_data)
        # self.register_field('value1', -1)
        # self.register_field('value1_text', functools.partial(self.value_to_text, 'value1', app_data))
        # self.register_field('value2', 0)
        # self.register_field('value2_text', functools.partial(self.value_to_text, 'value2', app_data))
        # self.register_field('value3', -1)
        # self.register_field('value3_text', functools.partial(self.value_to_text, 'value3', app_data))

        button1 = MPushButton(text='Group 1', type=MPushButton.PrimaryType)
        button2 = MPushButton(text='Group 2', type=MPushButton.PrimaryType)
        button3 = MPushButton(text='Group 3', type=MPushButton.PrimaryType)
        button1.clicked.connect(functools.partial(self.slot_change_value, 'value1'))
        button2.clicked.connect(functools.partial(self.slot_change_value, 'value2'))
        button3.clicked.connect(functools.partial(self.slot_change_value, 'value3'))

        # self.bind('value1', tool_group_v, 'checked', signal='sig_checked_changed')
        # self.bind('value2', tool_group_button_h, 'checked', signal='sig_checked_changed')
        # self.bind('value3', tool_group_button_v, 'checked', signal='sig_checked_changed')
        # self.bind('value1_text', button1, 'text')
        # self.bind('value2_text', button2, 'text')
        # self.bind('value3_text', button3, 'text')

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('orientation=Qt.Horizontal '))
        main_lay.addWidget(tool_group_h)
        main_lay.addWidget(MDivider('orientation=Qt.Vertical'))
        main_lay.addWidget(tool_group_v)
        main_lay.addWidget(button1)
        main_lay.addWidget(MDivider('orientation=Qt.Horizontal'))
        main_lay.addWidget(tool_group_button_h)
        main_lay.addWidget(button2)
        main_lay.addWidget(MDivider('checkable=True; exclusive=True'))
        main_lay.addWidget(tool_grp_excl_true)
        main_lay.addWidget(MDivider('checkable=True; exclusive=False'))
        main_lay.addWidget(tool_grp_excl_false)
        main_lay.addWidget(button3)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def value_to_text(self, field, data_list):
        return 'Please Select One' if self.field(field) < 0 else \
            'You Selected [{}]'.format(data_list[self.field(field)].get('text'))

    def slot_change_value(self, attr):
        import random
        self.set_field(attr, random.randrange(0, 3))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MToolButtonGroupTest()
    test.show()
    sys.exit(app.exec_())
