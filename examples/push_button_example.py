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
        sub_lay1.addWidget(MPushButton(text='Default'))
        sub_lay1.addWidget(MPushButton.primary(text='Primary'))
        sub_lay1.addWidget(MPushButton.success(text='Success'))
        sub_lay1.addWidget(MPushButton.warning(text='Warning'))
        sub_lay1.addWidget(MPushButton.danger(text='Danger'))

        sub_lay2 = QHBoxLayout()
        sub_lay2.addWidget(MPushButton(text='Upload', icon=MIcon('cloud_line.svg')))
        sub_lay2.addWidget(
            MPushButton.primary(text='Submit', icon=MIcon('folder_line.svg', '#ddd')))
        sub_lay2.addWidget(
            MPushButton.success(text='Submit', icon=MIcon('success_line.svg', '#ddd')))
        sub_lay2.addWidget(MPushButton.warning(text='Edit', icon=MIcon('edit_line.svg', '#ddd')))
        sub_lay2.addWidget(MPushButton.danger(text='Delete', icon=MIcon('trash_line.svg', '#ddd')))

        sub_lay3 = QHBoxLayout()
        size_list = [('Large', dayu_theme.large),
                     ('Medium', dayu_theme.medium),
                     ('Small', dayu_theme.small)]
        for label, size in size_list:
            button = MPushButton(text=label)
            button.set_dayu_size(size)
            button.set_dayu_type(MPushButton.PrimaryType)
            sub_lay3.addWidget(button)

        disabled_button = MPushButton(text='Disabled')
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
