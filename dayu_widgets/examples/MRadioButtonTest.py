#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MPushButton import MPushButton
from dayu_widgets.MRadioButton import MRadioButton
from dayu_widgets.qt import *


class MRadioButtonTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MRadioButtonTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        check_box_1 = MRadioButton('Maya')
        check_box_2 = MRadioButton('Nuke')
        check_box_3 = MRadioButton('Houdini')
        check_box_2.setChecked(True)
        widget_1 = QWidget()
        lay_1 = QHBoxLayout()
        lay_1.addWidget(check_box_1)
        lay_1.addWidget(check_box_2)
        lay_1.addWidget(check_box_3)
        widget_1.setLayout(lay_1)

        check_box_icon_1 = MRadioButton('Folder')
        check_box_icon_1.setIcon(MIcon('folder_fill.svg'))
        check_box_icon_2 = MRadioButton('Media')
        check_box_icon_2.setIcon(MIcon('media_fill.svg'))
        check_box_icon_3 = MRadioButton('User')
        check_box_icon_3.setIcon(MIcon('user_fill.svg'))
        check_box_icon_3.setEnabled(False)
        check_box_icon_2.setChecked(True)
        widget_2 = QWidget()
        lay_2 = QHBoxLayout()
        lay_2.addWidget(check_box_icon_1)
        lay_2.addWidget(check_box_icon_2)
        lay_2.addWidget(check_box_icon_3)
        widget_2.setLayout(lay_2)

        check_box_single = MRadioButton(u'支付宝')
        check_box_single.setChecked(True)
        check_box_single.setEnabled(False)
        widget_3 = QWidget()
        lay_3 = QHBoxLayout()
        lay_3.addWidget(check_box_single)
        widget_3.setLayout(lay_3)

        check_box_b = MRadioButton('Data Bind')
        label = MLabel()
        button = MPushButton(text='Change State')
        button.clicked.connect(lambda: self.set_field('checked', not self.field('checked')))
        self.register_field('checked', True)
        self.register_field('checked_text', lambda: 'Yes!' if self.field('checked') else 'No!!')
        self.bind('checked', check_box_b, 'checked', signal='toggled')
        self.bind('checked_text', label, 'text')

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('Basic'))
        main_lay.addWidget(widget_1)
        main_lay.addWidget(widget_3)
        main_lay.addWidget(MDivider('Icon'))
        main_lay.addWidget(widget_2)
        main_lay.addWidget(MDivider('Data Bind'))
        main_lay.addWidget(check_box_b)
        main_lay.addWidget(label)
        main_lay.addWidget(button)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MRadioButtonTest()
    test.show()
    sys.exit(app.exec_())
