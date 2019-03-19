#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################


from dayu_widgets.MPushButton import MPushButton
from dayu_widgets.MButtonGroup import MCheckBoxGroup
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MLabel import MLabel
from dayu_widgets.qt import *


class MCheckBoxGroupTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MCheckBoxGroupTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        self.app_data = [
            {'text': 'Maya', 'icon': 'app-maya'},
            {'text': 'Nuke', 'icon': 'app-nuke'},
            {'text': 'Houdini', 'icon': 'app-houdini'}
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
        self.bind('checked_app', radio_group_b, 'value', signal='sig_checked_changed')
        self.bind('checked_app_text', label, 'text')

        radio_group_tri = MCheckBoxGroup()
        radio_group_tri.set_button_list(self.app_data)
        self.register_field('check_grp', [u'Maya'])
        self.bind('check_grp', radio_group_tri, 'value', signal='sig_checked_changed')

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
    test = MCheckBoxGroupTest()
    test.show()
    sys.exit(app.exec_())
