# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.button_group import MToolButtonGroup
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets import dayu_theme
from dayu_widgets.qt import *


class ToolButtonGroupExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ToolButtonGroupExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        tool_group_h = MToolButtonGroup(size=dayu_theme.small)
        tool_group_h.set_button_list(['Apple', {'text': 'Banana'}, {'text': 'Pear'}])
        tool_1_lay = QHBoxLayout()
        tool_1_lay.addWidget(tool_group_h)
        tool_1_lay.addStretch()

        app_data = [
            {'text': 'Maya', 'icon': MIcon('app-maya.png'), 'checkable': True},
            {'text': 'Nuke', 'icon': MIcon('app-nuke.png'), 'checkable': True},
            {'text': 'Houdini', 'icon': MIcon('app-houdini.png'), 'checkable': True}
        ]

        tool_group_v = MToolButtonGroup(exclusive=True,
                                        size=dayu_theme.small,
                                        orientation=Qt.Vertical)
        tool_group_v.set_button_list(app_data)

        tool_group_button_h = MToolButtonGroup()
        tool_group_button_h.set_button_list(app_data)
        tool_2_lay = QHBoxLayout()
        tool_2_lay.addWidget(tool_group_button_h)
        tool_2_lay.addStretch()

        tool_grp_excl_true = MToolButtonGroup(orientation=Qt.Horizontal, exclusive=True)
        tool_grp_excl_true.set_button_list([
            {'svg': 'table_view.svg', 'checkable': True, 'tooltip': u'Table View'},
            {'svg': 'list_view.svg', 'checkable': True, 'tooltip': u'List View'},
            {'svg': 'tree_view.svg', 'checkable': True, 'tooltip': u'Tree View'},
            {'svg': 'big_view.svg', 'checkable': True, 'tooltip': u'Big View'},
        ])
        tool_grp_excl_true.set_dayu_checked(0)
        tool_excl_lay = QHBoxLayout()
        tool_excl_lay.addWidget(tool_grp_excl_true)
        tool_excl_lay.addStretch()

        tool_grp_excl_false = MToolButtonGroup(orientation=Qt.Horizontal,
                                               exclusive=False)
        tool_grp_excl_false.set_button_list(
            [
                {'tooltip': u'加粗', 'svg': 'bold.svg', 'checkable': True},
                {'tooltip': u'倾斜', 'svg': 'italic.svg', 'checkable': True},
                {'tooltip': u'下划线', 'svg': 'underline.svg', 'checkable': True},
            ])
        tool_excl_2_lay = QHBoxLayout()
        tool_excl_2_lay.addWidget(tool_grp_excl_false)
        tool_excl_2_lay.addStretch()

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('orientation=Qt.Horizontal '))
        main_lay.addLayout(tool_1_lay)
        main_lay.addWidget(MDivider('orientation=Qt.Vertical'))
        main_lay.addWidget(tool_group_v)
        main_lay.addWidget(MDivider('orientation=Qt.Horizontal'))
        main_lay.addLayout(tool_2_lay)
        main_lay.addWidget(MDivider('checkable=True; exclusive=True'))
        main_lay.addLayout(tool_excl_lay)
        main_lay.addWidget(MDivider('checkable=True; exclusive=False'))
        main_lay.addLayout(tool_excl_2_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = ToolButtonGroupExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
