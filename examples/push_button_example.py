#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import QHBoxLayout, QVBoxLayout, QWidget, MIcon
from dayu_widgets import dayu_theme


class PushButtonExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(PushButtonExample, self).__init__(parent)
        self.setWindowTitle('Example for MPushButton')

        sub_lay1 = QHBoxLayout()
        sub_lay1.addWidget(MPushButton('Default'))
        sub_lay1.addWidget(MPushButton('Primary').primary())
        sub_lay1.addWidget(MPushButton('Success').success())
        sub_lay1.addWidget(MPushButton('Warning').warning())
        sub_lay1.addWidget(MPushButton('Danger').danger())

        sub_lay2 = QHBoxLayout()
        sub_lay2.addWidget(MPushButton('Upload', MIcon('cloud_line.svg')))
        sub_lay2.addWidget(
            MPushButton('Submit', MIcon('folder_line.svg', '#ddd')).primary())
        sub_lay2.addWidget(
            MPushButton('Submit', MIcon('success_line.svg', '#ddd')).success())
        sub_lay2.addWidget(MPushButton('Edit', MIcon('edit_line.svg', '#ddd')).warning())
        sub_lay2.addWidget(MPushButton('Delete', MIcon('trash_line.svg', '#ddd')).danger())

        sub_lay3 = QHBoxLayout()
        sub_lay3.addWidget(MPushButton('Large').large().primary())
        sub_lay3.addWidget(MPushButton('Medium').medium().primary())
        sub_lay3.addWidget(MPushButton('Small').small().primary())

        disabled_button = MPushButton('Disabled')
        disabled_button.setEnabled(False)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different type'))
        main_lay.addLayout(sub_lay1)
        main_lay.addLayout(sub_lay2)
        main_lay.addWidget(MDivider('different size'))
        main_lay.addLayout(sub_lay3)
        main_lay.addWidget(MDivider('disabled'))
        main_lay.addWidget(disabled_button)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication

    app = QApplication(sys.argv)
    test = PushButtonExample()
    # dayu_theme.set_theme('light')
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
