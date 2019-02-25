#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MAvatar import MAvatar
from dayu_widgets.MButton import MButton
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MLabel import MLabel
from dayu_widgets.qt import *


class MAvatarTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MAvatarTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different size'))

        size_list = [MView.LargeSize, MView.DefaultSize, MView.SmallSize, ]

        for size in size_list:
            h_lay = QHBoxLayout()
            h_lay.addWidget(MLabel(size))
            for image in ['', 'avatar.png', 'app-maya.png', 'app-nuke.png', 'app-houdini.png']:
                h_lay.addWidget(MAvatar(size=size, image=image))
            h_lay.addStretch()
            main_lay.addLayout(h_lay)
        self.register_field('image', '')
        main_lay.addWidget(MDivider('different image'))
        avatar = MAvatar()
        self.bind('image', avatar, 'image')
        button = MButton(text='Change Avatar Image', type=MButton.PrimaryType)
        button.clicked.connect(self.slot_change_image)

        main_lay.addLayout(h_lay)
        main_lay.addWidget(avatar)
        main_lay.addWidget(button)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_change_image(self):
        import random
        self.set_field('image', random.choice(['avatar.png', 'app-maya.png', 'app-nuke.png', 'app-houdini.png']))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MAvatarTest()
    test.show()
    sys.exit(app.exec_())
