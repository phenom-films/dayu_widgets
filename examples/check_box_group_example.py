#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################


from dayu_widgets.push_button import MPushButton
from dayu_widgets.button_group import MCheckBoxGroup
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.qt import *


class CheckBoxGroupExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(CheckBoxGroupExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        self.app_data = [
            {'text': 'Maya', 'icon': MIcon('app-maya.png')},
            {'text': 'Nuke', 'icon': MIcon('app-nuke.png')},
            {'text': 'Houdini', 'icon': MIcon('app-houdini.png')}
        ]
        radio_group_h = MCheckBoxGroup()
        radio_group_v = MCheckBoxGroup(orientation=Qt.Vertical)

        radio_group_h.set_button_list(self.app_data)
        radio_group_v.set_button_list(self.app_data)

        self.data_list = [u'北京', u'上海', u'广州', u'深圳', u'郑州', u'石家庄']
        radio_group_b = MCheckBoxGroup()
        radio_group_b.set_button_list(self.data_list)

        button = MPushButton(text='Change Value')
        button.clicked.connect(self.slot_button_clicked)

        label = MLabel()
        self.register_field('checked_app', [u'北京', u'郑州'])
        self.register_field('checked_app_text', lambda: u' & '.join(self.field('checked_app')))
        self.bind('checked_app', radio_group_b, 'dayu_checked', signal='sig_checked_changed')
        self.bind('checked_app_text', label, 'text')

        radio_group_tri = MCheckBoxGroup()
        radio_group_tri.set_button_list(self.app_data)
        self.register_field('check_grp', [u'Maya'])
        self.bind('check_grp', radio_group_tri, 'dayu_checked', signal='sig_checked_changed')

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('Orientation Qt.Horizontal'))
        main_lay.addWidget(radio_group_h)
        main_lay.addWidget(MDivider('Orientation Qt.Vertical'))
        main_lay.addWidget(radio_group_v)

        main_lay.addWidget(MDivider('Data Bind'))
        main_lay.addWidget(radio_group_b)
        main_lay.addWidget(label)
        main_lay.addWidget(button)

        main_lay.addWidget(MDivider('Try Context Menu'))
        main_lay.addWidget(radio_group_tri)
        main_lay.addStretch()
        self.setLayout(main_lay)

    @Slot()
    def slot_button_clicked(self):
        import random
        start = random.randint(0, len(self.data_list))
        end = random.randint(start, len(self.data_list))
        self.set_field('checked_app', self.data_list[start:end])


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = CheckBoxGroupExample()
    from dayu_widgets import dayu_theme
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
