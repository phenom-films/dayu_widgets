# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3.field_mixin import MFieldMixin
from dayu_widgets3.label import MLabel
from dayu_widgets3.line_edit import MLineEdit
from dayu_widgets3.push_button import MPushButton
from dayu_widgets3.qt import MPixmap


class FieldMixinExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(FieldMixinExample, self).__init__(parent)
        self.register_field("my_name", "xiaoming")
        self.register_field("thumbnail_path", "")
        self.register_field("is_enable", True)
        self.register_field("status", "waiting")
        self.register_field("str_enable", self.computed_str_enable)
        self.register_field("thumbnail_pix_map", self.computed_thumbnail_pix_map)
        self.register_field("email", self.computed_email)

        name2_label = MLabel()
        email_label = MLabel()
        thumbnail_label = MLabel()
        enable_button = MPushButton().primary()
        self.bind("my_name", name2_label, "dayu_text")
        self.bind("email", email_label, "dayu_text")
        self.bind("is_enable", enable_button, "enabled")
        self.bind("thumbnail_pix_map", thumbnail_label, "pixmap")
        self.bind("str_enable", enable_button, "text")

        button = MPushButton(text="Change Data").primary()
        button.clicked.connect(self.slot_change_data)
        main_lay = QtWidgets.QGridLayout()
        main_lay.addWidget(MLabel("Avatar:"), 0, 0)
        main_lay.addWidget(thumbnail_label, 0, 1)
        main_lay.addWidget(MLabel("Name:"), 1, 0)
        main_lay.addWidget(self.bind("my_name", MLineEdit(), "text", signal="textEdited"), 1, 1)
        main_lay.addWidget(MLabel("Email:"), 2, 0)
        main_lay.addWidget(email_label, 2, 1)
        main_lay.addWidget(MLabel("Enabled:"), 3, 0)
        main_lay.addWidget(enable_button, 3, 1)
        # for index, i in enumerate(self.field('my_name')):
        #     main_lay.addRow('name{}:'.format(index), self.bind('my_name', QLabel(), 'text', index=index))
        main_lay.addWidget(button, 4, 1)

        temp_lay = QtWidgets.QVBoxLayout()
        temp_lay.addLayout(main_lay)
        temp_lay.addStretch()
        self.setLayout(temp_lay)

    def computed_str_enable(self):
        return "Enabled" if self.field("is_enable") else "Disabled"

    def computed_thumbnail_pix_map(self):
        return MPixmap(self.field("thumbnail_path"))

    def computed_email(self):
        return "{}@phenom-films.com".format(self.field("my_name"))

    def slot_change_data(self):
        # Import built-in modules
        import random

        self.set_field(
            "my_name",
            random.choice(["xiaoming", "xiaohua", "xiaohong", "hahaha", "lalalala"]),
        )
        self.set_field(
            "thumbnail_path",
            "app-{}.png".format(random.choice(["maya", "nuke", "houdini"])),
        )
        self.set_field("is_enable", bool(random.randint(0, 1)))
        self.set_field("status", "haha")


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets3 import dayu_theme
    from dayu_widgets3.qt import application

    with application() as app:
        test = FieldMixinExample()
        dayu_theme.apply(test)
        test.show()
