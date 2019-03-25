#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MLineEdit import MLineEdit
from dayu_widgets.MPushButton import MPushButton
from dayu_widgets.qt import *


class MFieldMixinTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MFieldMixinTest, self).__init__(parent)
        self.register_field('my_name', 'xiaoming')
        self.register_field('thumbnail_path', '')
        self.register_field('is_enable', True)
        self.register_field('status', 'waiting')
        self.register_field('str_enable', self.computed_str_enable)
        self.register_field('thumbnail_pix_map', self.computed_thumbnail_pix_map)
        self.register_field('email', self.computed_email)

        name2_label = MLabel()
        email_label = MLabel(link=True)
        thumbnail_label = MLabel()
        enable_button = MPushButton(type=MPushButton.PrimaryType)
        self.bind('my_name', name2_label, 'text')
        self.bind('email', email_label, 'text')
        self.bind('is_enable', enable_button, 'enabled')
        self.bind('thumbnail_pix_map', thumbnail_label, 'pixmap')
        self.bind('str_enable', enable_button, 'text')

        button = MPushButton(text='Change Data', type=MPushButton.PrimaryType)
        button.clicked.connect(self.slot_change_data)
        main_lay = QGridLayout()
        main_lay.addWidget(MLabel('Avatar:'), 0, 0)
        main_lay.addWidget(thumbnail_label, 0, 1)
        main_lay.addWidget(MLabel('Name:'), 1, 0)
        main_lay.addWidget(self.bind('my_name', MLineEdit(), 'text', signal='textEdited'), 1, 1)
        main_lay.addWidget(MLabel('Email:'), 2, 0)
        main_lay.addWidget(email_label, 2, 1)
        main_lay.addWidget(MLabel('Enabled:'), 3, 0)
        main_lay.addWidget(enable_button, 3, 1)
        # for index, i in enumerate(self.field('my_name')):
        #     main_lay.addRow('name{}:'.format(index), self.bind('my_name', QLabel(), 'text', index=index))
        main_lay.addWidget(button, 4, 1)

        temp_lay = QVBoxLayout()
        temp_lay.addLayout(main_lay)
        temp_lay.addStretch()
        self.setLayout(temp_lay)

    def computed_str_enable(self):
        print 'computed_str_enable'
        return 'Enabled' if self.field('is_enable') else 'Disabled'

    def computed_thumbnail_pix_map(self):
        print 'computed_thumbnail_pix_map'
        return MPixmap(self.field('thumbnail_path'))

    def computed_email(self):
        print 'computed_email'
        return '{}@phenom-films.com'.format(self.field('my_name'))

    def slot_change_data(self):
        import random
        self.set_field('my_name', random.choice(['xiaoming', 'xiaohua', 'xiaohong', 'hahaha', 'lalalala']))
        self.set_field('thumbnail_path', 'app-{}.png'.format(random.choice(['maya', 'nuke', 'houdini'])))
        self.set_field('is_enable', bool(random.randint(0, 1)))
        self.set_field('status', 'haha')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MFieldMixinTest()
    from dayu_widgets.MTheme import apply_theme
    apply_theme(test)
    test.show()
    sys.exit(app.exec_())
