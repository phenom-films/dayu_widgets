#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.6
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import QWidget, QVBoxLayout, QHBoxLayout, MIcon, QGridLayout, QFormLayout
from dayu_widgets.push_button import MPushButton
from dayu_widgets.drawer import MDrawer
from dayu_widgets.divider import MDivider
from dayu_widgets.label import MLabel
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.spin_box import MSpinBox, MDateEdit
from dayu_widgets.button_group import MRadioButtonGroup


class DrawerExample(QWidget):
    def __init__(self, parent=None):
        super(DrawerExample, self).__init__(parent)
        self.setWindowTitle('Examples for MDrawer')
        self._init_ui()

    def _init_ui(self):
        self.button_grp = MRadioButtonGroup()
        self.button_grp.set_button_list(['top', {'text': 'right', 'checked': True}, 'bottom', 'left'])

        open_button_2 = MPushButton('Open').primary()
        open_button_2.clicked.connect(self.slot_open_button_2)
        placement_lay = QHBoxLayout()
        placement_lay.addWidget(self.button_grp)
        placement_lay.addSpacing(20)
        placement_lay.addWidget(open_button_2)
        placement_lay.addStretch()

        new_account_button = MPushButton(text='New account', icon=MIcon('add_line.svg', '#fff')).primary()
        new_account_button.clicked.connect(self.slot_new_account)
        new_account_lay = QHBoxLayout()
        new_account_lay.addWidget(MLabel('Submit form in drawer'))
        new_account_lay.addWidget(new_account_button)
        new_account_lay.addStretch()


        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('Custom Placement'))
        main_lay.addLayout(placement_lay)
        main_lay.addWidget(MDivider('Submit form in drawer'))
        main_lay.addLayout(new_account_lay)

        main_lay.addWidget(MDivider('Preview drawer'))
        self.setLayout(main_lay)


    def slot_open_button(self):
        custom_widget = QWidget()
        custom_lay = QVBoxLayout()
        custom_lay.addWidget(MLabel('Some contents...'))
        custom_lay.addWidget(MLabel('Some contents...'))
        custom_lay.addWidget(MLabel('Some contents...'))
        custom_widget.setLayout(custom_lay)

        drawer = MDrawer('Basic Drawer', parent=self).left()
        drawer.setFixedWidth(200)
        drawer.set_widget(custom_widget)
        drawer.show()

    def slot_open_button_2(self):
        custom_widget = QWidget()
        custom_lay = QVBoxLayout()
        custom_lay.addWidget(MLabel('Some contents...'))
        custom_lay.addWidget(MLabel('Some contents...'))
        custom_lay.addWidget(MLabel('Some contents...'))
        custom_widget.setLayout(custom_lay)

        drawer = MDrawer('Basic Drawer', parent=self)
        drawer.set_dayu_position(self.button_grp.get_button_group().checkedButton().text())

        drawer.setFixedWidth(200)
        drawer.set_widget(custom_widget)
        drawer.show()

    def slot_new_account(self):
        custom_widget = QWidget()
        custom_lay = QFormLayout()
        custom_lay.addRow('Name', MLineEdit())
        custom_lay.addRow('Age', MSpinBox())
        custom_lay.addRow('Birth', MDateEdit())
        custom_widget.setLayout(custom_lay)

        drawer = MDrawer('New account', parent=self)
        submit_button = MPushButton('Submit').primary()
        submit_button.clicked.connect(drawer.close)
        drawer.add_button(MPushButton('Cancel'))
        drawer.add_button(submit_button)

        drawer.setFixedWidth(200)
        drawer.set_widget(custom_widget)
        drawer.show()



if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication
    from dayu_widgets import dayu_theme

    app = QApplication(sys.argv)
    test = DrawerExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
