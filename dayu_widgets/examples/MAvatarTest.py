#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MAvatar import MAvatar
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MPushButton import MPushButton
from dayu_widgets.MTheme import dayu_theme
from dayu_widgets.mixin import theme_mixin
from dayu_widgets.qt import *


@theme_mixin
class MAvatarTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MAvatarTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different size'))

        size_list = [('Huge', dayu_theme.size.huge),
                     ('Large', dayu_theme.size.large),
                     ('Medium', dayu_theme.size.medium),
                     ('Small', dayu_theme.size.small),
                     ('Tiny', dayu_theme.size.tiny)]

        self.pix_map_list = ['', MPixmap('avatar.png'), MPixmap('app-maya.png'), MPixmap('app-nuke.png'),
                             MPixmap('app-houdini.png')]
        for label, size in size_list:
            h_lay = QHBoxLayout()
            h_lay.addWidget(MLabel(label))
            for image in self.pix_map_list:
                h_lay.addWidget(MAvatar(size=size, image=image))
            h_lay.addStretch()
            main_lay.addLayout(h_lay)
        self.register_field('image', '')
        main_lay.addWidget(MDivider('different image'))
        avatar = MAvatar()
        self.bind('image', avatar, 'image')
        button = MPushButton(text='Change Avatar Image', type=MPushButton.PrimaryType)
        button.clicked.connect(self.slot_change_image)

        main_lay.addWidget(avatar)
        main_lay.addWidget(button)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_change_image(self):
        import random
        self.set_field('image', random.choice(self.pix_map_list))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MAvatarTest()
    test.show()
    sys.exit(app.exec_())
