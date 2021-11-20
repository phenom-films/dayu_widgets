#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.avatar import MAvatar
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import MPixmap
from dayu_widgets.qt import QFormLayout
from dayu_widgets.qt import QHBoxLayout
from dayu_widgets.qt import QVBoxLayout
from dayu_widgets.qt import QWidget
from dayu_widgets.qt import Qt


class AvatarExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(AvatarExample, self).__init__(parent)
        self.setWindowTitle("Example for MAvatar")
        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider("different size"))

        size_list = [
            ("Huge", MAvatar.huge),
            ("Large", MAvatar.large),
            ("Medium", MAvatar.medium),
            ("Small", MAvatar.small),
            ("Tiny", MAvatar.tiny),
        ]

        self.pix_map_list = [
            None,
            MPixmap("avatar.png"),
            MPixmap("app-maya.png"),
            MPixmap("app-nuke.png"),
            MPixmap("app-houdini.png"),
        ]
        form_lay = QFormLayout()
        form_lay.setLabelAlignment(Qt.AlignRight)

        for label, cls in size_list:
            h_lay = QHBoxLayout()
            for image in self.pix_map_list:
                avatar_tmp = cls(image)
                h_lay.addWidget(avatar_tmp)
            h_lay.addStretch()
            form_lay.addRow(MLabel(label), h_lay)
        main_lay.addLayout(form_lay)
        self.register_field("image", None)
        main_lay.addWidget(MDivider("different image"))
        self.avatar = MAvatar()
        self.bind("image", self.avatar, "dayu_image")
        button = MPushButton(text="Change Avatar Image").primary()
        button.clicked.connect(self.slot_change_image)

        main_lay.addWidget(self.avatar)
        main_lay.addWidget(button)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_change_image(self):
        """Set the Avatar image random by data bind."""
        # Import built-in modules
        import random

        self.set_field("image", random.choice(self.pix_map_list))


if __name__ == "__main__":
    # Import built-in modules
    import sys

    # Import local modules
    from dayu_widgets.qt import QApplication

    app = QApplication(sys.argv)
    test = AvatarExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
